# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-10-30

- **Total crypto market cap:** €2.34 T (▼ -5.85% in 24h, measured in USD)
- **Bitcoin dominance:** 59.2%
- **Best of the tracked coins (24h):** Bitcoin ▼ -3.92%
- **Weakest of the tracked coins (24h):** BNB ▼ -6.46%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €69,079.00 | ▼ -3.92% | ▼ -5.28% | €68,682.08 – €73,365.66 | €1.39 T |
| Ethereum (ETH) | €1,993.22 | ▼ -4.34% | ▼ -7.02% | €1,963.39 – €2,160.08 | €243.5 B |
| BNB (BNB) | €624.69 | ▼ -6.46% | ▼ -6.24% | €622.43 – €680.86 | €82.2 B |
| XRP (XRP) | €1.11 | ▼ -4.17% | ▼ -5.54% | €1.08 – €1.20 | €70.3 B |
| Solana (SOL) | €85.43 | ▼ -5.28% | ▼ -7.34% | €84.01 – €94.01 | €50.4 B |
| Dogecoin (DOGE) | €0.0676 | ▼ -4.78% | ▼ -5.41% | €0.0662 – €0.0722 | €10.6 B |
| Cardano (ADA) | €0.1716 | ▼ -5.07% | ▼ -10.94% | €0.1673 – €0.1951 | €6.4 B |

![7-day performance](charts/2026-10-30.svg)

**Recent reports:** [2026-10-30](reports/2026/10/2026-10-30.md) · [2026-10-29](reports/2026/10/2026-10-29.md) · [2026-10-28](reports/2026/10/2026-10-28.md)
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
