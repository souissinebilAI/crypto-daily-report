# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-12

- **Total crypto market cap:** €2.17 T (▼ -5.23% in 24h, measured in USD)
- **Bitcoin dominance:** 59.5%
- **Best of the tracked coins (24h):** Bitcoin ▼ -3.43%
- **Weakest of the tracked coins (24h):** Dogecoin ▼ -5.67%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €64,477.00 | ▼ -3.43% | ▼ -10.16% | €65,486.31 – €70,678.06 | €1.30 T |
| Ethereum (ETH) | €1,804.73 | ▼ -3.59% | ▼ -16.08% | €1,817.70 – €2,115.55 | €220.5 B |
| BNB (BNB) | €588.90 | ▼ -4.44% | ▼ -8.24% | €592.48 – €634.43 | €77.4 B |
| XRP (XRP) | €0.9218 | ▼ -4.62% | ▼ -21.51% | €0.9340 – €1.16 | €58.5 B |
| Solana (SOL) | €73.18 | ▼ -4.30% | ▼ -14.89% | €73.55 – €83.90 | €43.3 B |
| Dogecoin (DOGE) | €0.0587 | ▼ -5.67% | ▼ -14.29% | €0.0592 – €0.0670 | €9.2 B |
| Cardano (ADA) | €0.1523 | ▼ -5.65% | ▼ -13.00% | €0.1541 – €0.1715 | €5.7 B |

![7-day performance](charts/2026-11-12.svg)

**Recent reports:** [2026-11-12](reports/2026/11/2026-11-12.md) · [2026-11-11](reports/2026/11/2026-11-11.md) · [2026-11-10](reports/2026/11/2026-11-10.md) · [2026-11-09](reports/2026/11/2026-11-09.md) · [2026-11-08](reports/2026/11/2026-11-08.md) · [2026-11-07](reports/2026/11/2026-11-07.md) · [2026-11-06](reports/2026/11/2026-11-06.md)
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
