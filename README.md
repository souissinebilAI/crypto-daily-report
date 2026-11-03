# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-03

- **Total crypto market cap:** €2.34 T (▼ -3.15% in 24h, measured in USD)
- **Bitcoin dominance:** 59.2%
- **Best of the tracked coins (24h):** XRP ▲ +2.38%
- **Weakest of the tracked coins (24h):** Solana ▼ -0.64%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €69,108.00 | ▼ -0.37% | ▼ -3.63% | €68,374.55 – €73,025.92 | €1.39 T |
| Ethereum (ETH) | €2,044.65 | ▲ +0.26% | ▼ -1.98% | €1,959.15 – €2,118.58 | €249.8 B |
| BNB (BNB) | €623.64 | ▼ -0.62% | ▼ -5.95% | €618.11 – €679.39 | €82.0 B |
| XRP (XRP) | €1.14 | ▲ +2.38% | ▼ -2.14% | €1.08 – €1.20 | €72.4 B |
| Solana (SOL) | €83.48 | ▼ -0.64% | ▼ -7.53% | €81.72 – €91.99 | €49.3 B |
| Dogecoin (DOGE) | €0.0672 | ▲ +0.26% | ▼ -3.42% | €0.0658 – €0.0720 | €10.5 B |
| Cardano (ADA) | €0.1704 | ▲ +0.45% | ▼ -7.01% | €0.1666 – €0.1857 | €6.4 B |

![7-day performance](charts/2026-11-03.svg)

**Recent reports:** [2026-11-03](reports/2026/11/2026-11-03.md) · [2026-11-02](reports/2026/11/2026-11-02.md) · [2026-11-01](reports/2026/11/2026-11-01.md) · [2026-10-31](reports/2026/10/2026-10-31.md) · [2026-10-30](reports/2026/10/2026-10-30.md) · [2026-10-29](reports/2026/10/2026-10-29.md) · [2026-10-28](reports/2026/10/2026-10-28.md)
<!-- LATEST:END -->

## How it works

**Trigger:** a scheduled workflow ([`.github/workflows/daily-report.yml`](.github/workflows/daily-report.yml))
starts at 07:00 and 08:00 UTC. A gate step only lets the run continue from 09:00 Berlin time, which
keeps the time right in both summer and winter. It can also be started by hand under *Actions → Run workflow*.

**Inputs:** current prices, 24h and 7-day changes and 7-day price curves for Bitcoin, Ethereum,
Solana, BNB, XRP, Cardano and Dogecoin in EUR, plus total market data.

**What happens:** the unit tests run first. Then [`report.py`](report.py) (Python standard library
only) fetches the data, builds the summary and table and draws the chart as an SVG. A second run
on the same day does nothing.

**Outputs:**

| Path | Content |
|---|---|
| `reports/YYYY/MM/YYYY-MM-DD.md` | the day's report |
| `charts/YYYY-MM-DD.svg` | 7-day performance, each coin indexed to 100 |
| `data/history.csv` | one row per coin per day, for later analysis |
| `README.md` | the latest report section above |

## Run it locally

```bash
python -m unittest discover tests
python report.py          # FORCE=1 python report.py to rebuild today's report
```

An optional free CoinGecko demo key can be added as the repository secret `COINGECKO_API_KEY`
if the public API starts rate-limiting the runner.

## Disclaimer

This is an automated data summary for learning purposes. It is not financial advice.

## License

[MIT](LICENSE)
