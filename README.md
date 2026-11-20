# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-20

- **Total crypto market cap:** €1.87 T (▼ -8.47% in 24h, measured in USD)
- **Bitcoin dominance:** 58.0%
- **Best of the tracked coins (24h):** Bitcoin ▼ -5.30%
- **Weakest of the tracked coins (24h):** Cardano ▼ -8.12%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €54,190.00 | ▼ -5.30% | ▼ -11.28% | €55,900.34 – €62,749.28 | €1.09 T |
| Ethereum (ETH) | €1,504.27 | ▼ -6.89% | ▼ -11.48% | €1,569.27 – €1,775.04 | €183.9 B |
| BNB (BNB) | €497.43 | ▼ -6.57% | ▼ -11.60% | €515.53 – €580.28 | €65.4 B |
| XRP (XRP) | €0.8233 | ▼ -6.31% | ▼ -8.75% | €0.8168 – €0.9388 | €52.3 B |
| Solana (SOL) | €61.88 | ▼ -7.59% | ▼ -12.96% | €61.71 – €73.38 | €36.6 B |
| Dogecoin (DOGE) | €0.0488 | ▼ -8.10% | ▼ -14.77% | €0.0510 – €0.0598 | €7.7 B |
| Cardano (ADA) | €0.1270 | ▼ -8.12% | ▼ -15.70% | €0.1307 – €0.1575 | €4.8 B |

![7-day performance](charts/2026-11-20.svg)

**Recent reports:** [2026-11-20](reports/2026/11/2026-11-20.md) · [2026-11-19](reports/2026/11/2026-11-19.md) · [2026-11-18](reports/2026/11/2026-11-18.md) · [2026-11-17](reports/2026/11/2026-11-17.md) · [2026-11-16](reports/2026/11/2026-11-16.md) · [2026-11-15](reports/2026/11/2026-11-15.md) · [2026-11-14](reports/2026/11/2026-11-14.md)
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
