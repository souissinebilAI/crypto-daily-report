"""Build the daily crypto market report.

Fetches prices from the public CoinGecko API, then writes:
  reports/YYYY/MM/YYYY-MM-DD.md   the report for the day
  charts/YYYY-MM-DD.svg           7-day performance chart
  data/history.csv                one row per coin per day
  README.md                       the "latest report" section

Standard library only. Runs once per day; a second run on the same day
does nothing unless FORCE=1 is set.
"""

import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
API = "https://api.coingecko.com/api/v3"
CURRENCY = "eur"
COINS = ["bitcoin", "ethereum", "solana", "binancecoin", "ripple", "cardano", "dogecoin"]
COLORS = ["#f7931a", "#627eea", "#14b8a6", "#d4a106", "#334155", "#2563eb", "#c2a633"]
README_START = "<!-- LATEST:START -->"
README_END = "<!-- LATEST:END -->"


def berlin_now():
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("Europe/Berlin"))
    except Exception:
        # Windows without the tzdata package: fall back to the machine's local time.
        return datetime.now().astimezone()


def fetch(path, params):
    query = "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(f"{API}{path}?{query}", headers={"Accept": "application/json",
                                                                   "User-Agent": "crypto-daily-report"})
    key = os.environ.get("COINGECKO_API_KEY")
    if key:
        req.add_header("x-cg-demo-api-key", key)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            # 429 = rate limited; shared CI runners hit this now and then.
            if err.code not in (429, 500, 502, 503, 504) or attempt == 3:
                raise
        except urllib.error.URLError:
            if attempt == 3:
                raise
        time.sleep(15 * (attempt + 1))


def fmt_eur(value):
    if value >= 1_000_000_000_000:
        return f"€{value / 1e12:.2f} T"
    if value >= 1_000_000_000:
        return f"€{value / 1e9:.1f} B"
    if value >= 1:
        return f"€{value:,.2f}"
    return f"€{value:.4f}"


def fmt_pct(value):
    if value is None:
        return "n/a"
    arrow = "▲" if value > 0 else "▼" if value < 0 else "•"
    return f"{arrow} {value:+.2f}%"


def chart_svg(coins, width=720, height=320):
    """Line chart of the last 7 days, each coin indexed to 100 at the start."""
    pad_l, pad_r, pad_t, pad_b = 48, 120, 20, 30
    series = []
    for coin in coins:
        prices = [p for p in coin["sparkline_in_7d"]["price"] if p]
        if len(prices) > 1:
            series.append((coin["symbol"].upper(), [p / prices[0] * 100 for p in prices]))
    lo = min(min(v) for _, v in series)
    hi = max(max(v) for _, v in series)
    lo, hi = min(lo, 100) - 1, max(hi, 100) + 1
    plot_w, plot_h = width - pad_l - pad_r, height - pad_t - pad_b

    def y(v):
        return pad_t + (hi - v) / (hi - lo) * plot_h

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
           f'font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="12">',
           f'<rect width="{width}" height="{height}" fill="#ffffff"/>']
    for v in (lo + (hi - lo) * i / 4 for i in range(5)):
        out.append(f'<line x1="{pad_l}" x2="{pad_l + plot_w}" y1="{y(v):.1f}" y2="{y(v):.1f}" '
                   f'stroke="{"#94a3b8" if abs(v - 100) < 1e-9 else "#e2e8f0"}"/>')
        out.append(f'<text x="{pad_l - 6}" y="{y(v) + 4:.1f}" text-anchor="end" fill="#64748b">{v:.0f}</text>')
    out.append(f'<line x1="{pad_l}" x2="{pad_l + plot_w}" y1="{y(100):.1f}" y2="{y(100):.1f}" stroke="#94a3b8" stroke-dasharray="4 3"/>')
    out.append(f'<text x="{pad_l}" y="{height - 8}" fill="#64748b">7 days ago</text>')
    out.append(f'<text x="{pad_l + plot_w}" y="{height - 8}" text-anchor="end" fill="#64748b">now</text>')

    labels = []
    for (symbol, values), color in zip(series, COLORS):
        step = plot_w / (len(values) - 1)
        points = " ".join(f"{pad_l + i * step:.1f},{y(v):.1f}" for i, v in enumerate(values))
        out.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="1.8"/>')
        labels.append([y(values[-1]), symbol, values[-1], color])
    # Push end labels apart so they don't overlap.
    labels.sort()
    for i in range(1, len(labels)):
        labels[i][0] = max(labels[i][0], labels[i - 1][0] + 14)
    for ly, symbol, last, color in labels:
        out.append(f'<text x="{pad_l + plot_w + 8}" y="{ly + 4:.1f}" fill="{color}" font-weight="600">'
                   f'{symbol} {last - 100:+.1f}%</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def coin_table(coins, usd_to_eur):
    rows = ["| Coin | Price | 24h | 7d | 7d range | Market cap |",
            "|---|---:|---:|---:|---:|---:|"]
    for c in coins:
        # CoinGecko returns the 7-day sparkline in USD even when vs_currency is EUR.
        week = [p * usd_to_eur for p in c["sparkline_in_7d"]["price"] if p]
        rows.append(f"| {c['name']} ({c['symbol'].upper()}) | {fmt_eur(c['current_price'])} "
                    f"| {fmt_pct(c.get('price_change_percentage_24h_in_currency'))} "
                    f"| {fmt_pct(c.get('price_change_percentage_7d_in_currency'))} "
                    f"| {fmt_eur(min(week))} – {fmt_eur(max(week))} | {fmt_eur(c['market_cap'])} |")
    return "\n".join(rows)


def summary(coins, market):
    by_24h = sorted(coins, key=lambda c: c.get("price_change_percentage_24h_in_currency") or 0)
    best, worst = by_24h[-1], by_24h[0]
    data = market["data"]
    lines = [
        f"- **Total crypto market cap:** {fmt_eur(data['total_market_cap'][CURRENCY])} "
        f"({fmt_pct(data.get('market_cap_change_percentage_24h_usd'))} in 24h, measured in USD)",
        f"- **Bitcoin dominance:** {data['market_cap_percentage']['btc']:.1f}%",
        f"- **Best of the tracked coins (24h):** {best['name']} "
        f"{fmt_pct(best.get('price_change_percentage_24h_in_currency'))}",
        f"- **Weakest of the tracked coins (24h):** {worst['name']} "
        f"{fmt_pct(worst.get('price_change_percentage_24h_in_currency'))}",
    ]
    up = sum(1 for c in coins if (c.get("price_change_percentage_7d_in_currency") or 0) > 0)
    lines.append(f"- **Week:** {up} of {len(coins)} tracked coins are up over 7 days.")
    return "\n".join(lines)


def write_report(day, stamp, coins, market, usd_to_eur):
    chart = ROOT / "charts" / f"{day}.svg"
    chart.parent.mkdir(exist_ok=True)
    chart.write_text(chart_svg(coins), encoding="utf-8")

    report = ROOT / "reports" / day[:4] / day[5:7] / f"{day}.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    rel_chart = os.path.relpath(chart, report.parent).replace(os.sep, "/")
    report.write_text(
        f"# Crypto market review: {day}\n\n"
        f"Snapshot taken {stamp} (Europe/Berlin). Prices in EUR from CoinGecko.\n\n"
        f"## Summary\n\n{summary(coins, market)}\n\n"
        f"## Tracked coins\n\n{coin_table(coins, usd_to_eur)}\n\n"
        f"## Last 7 days (indexed to 100)\n\n![7-day performance]({rel_chart})\n\n"
        f"---\n*Automated data summary. Not financial advice.*\n",
        encoding="utf-8")
    return report, chart


def append_history(day, coins, path=None):
    path = path or ROOT / "data" / "history.csv"
    path.parent.mkdir(exist_ok=True)
    # Drop rows for this day first, so a forced rerun replaces them instead of adding duplicates.
    rows = []
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            rows = [r for r in list(csv.reader(f))[1:] if r and r[0] != day]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "coin", "price_eur", "change_24h_pct", "change_7d_pct", "market_cap_eur"])
        w.writerows(rows)
        for c in coins:
            w.writerow([day, c["id"], c["current_price"],
                        round(c.get("price_change_percentage_24h_in_currency") or 0, 4),
                        round(c.get("price_change_percentage_7d_in_currency") or 0, 4),
                        c["market_cap"]])


def update_readme(day, report, chart, coins, market, usd_to_eur):
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    start, end = text.index(README_START), text.index(README_END)
    rel = lambda p: p.relative_to(ROOT).as_posix()
    recent = sorted((ROOT / "reports").rglob("*.md"), reverse=True)[:7]
    block = (f"{README_START}\n### {day}\n\n{summary(coins, market)}\n\n{coin_table(coins, usd_to_eur)}\n\n"
             f"![7-day performance]({rel(chart)})\n\n"
             f"**Recent reports:** " + " · ".join(f"[{p.stem}]({rel(p)})" for p in recent) + "\n")
    path.write_text(text[:start] + block + text[end:], encoding="utf-8")


def main():
    now = berlin_now()
    day = now.strftime("%Y-%m-%d")
    if (ROOT / "reports" / day[:4] / day[5:7] / f"{day}.md").exists() and os.environ.get("FORCE") != "1":
        print(f"Report for {day} already exists, nothing to do.")
        return 0

    coins = fetch("/coins/markets", {"vs_currency": CURRENCY, "ids": ",".join(COINS),
                                     "order": "market_cap_desc", "sparkline": "true",
                                     "price_change_percentage": "24h,7d"})
    market = fetch("/global", {})
    btc = fetch("/simple/price", {"ids": "bitcoin", "vs_currencies": "eur,usd"})["bitcoin"]
    usd_to_eur = btc["eur"] / btc["usd"]
    if len(coins) != len(COINS):
        print(f"Expected {len(COINS)} coins, got {len(coins)}", file=sys.stderr)
        return 1

    report, chart = write_report(day, now.strftime("%Y-%m-%d %H:%M"), coins, market, usd_to_eur)
    append_history(day, coins)
    update_readme(day, report, chart, coins, market, usd_to_eur)
    print(f"Wrote {report.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
