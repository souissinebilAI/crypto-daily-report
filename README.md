# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-10-31

- **Total crypto market cap:** €2.35 T (▼ -2.49% in 24h, measured in USD)
- **Bitcoin dominance:** 59.2%
- **Best of the tracked coins (24h):** Ethereum ▲ +0.67%
- **Weakest of the tracked coins (24h):** Solana ▼ -0.97%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €69,155.00 | ▲ +0.08% | ▼ -3.78% | €68,182.32 – €72,942.90 | €1.39 T |
| Ethereum (ETH) | €2,005.52 | ▲ +0.67% | ▼ -4.77% | €1,956.92 – €2,116.17 | €245.0 B |
| BNB (BNB) | €629.77 | ▲ +0.62% | ▼ -3.51% | €620.38 – €678.62 | €82.8 B |
| XRP (XRP) | €1.11 | ▲ +0.14% | ▼ -2.48% | €1.08 – €1.19 | €70.5 B |
| Solana (SOL) | €85.51 | ▼ -0.97% | ▼ -5.36% | €83.74 – €91.89 | €50.5 B |
| Dogecoin (DOGE) | €0.0672 | ▼ -0.65% | ▼ -2.87% | €0.0660 – €0.0719 | €10.5 B |
| Cardano (ADA) | €0.1719 | ▼ -0.21% | ▼ -7.45% | €0.1668 – €0.1865 | €6.5 B |

![7-day performance](charts/2026-10-31.svg)

**Recent reports:** [2026-10-31](reports/2026/10/2026-10-31.md) · [2026-10-30](reports/2026/10/2026-10-30.md) · [2026-10-29](reports/2026/10/2026-10-29.md) · [2026-10-28](reports/2026/10/2026-10-28.md)
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
