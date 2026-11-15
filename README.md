# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-15

- **Total crypto market cap:** €2.02 T (▼ -4.78% in 24h, measured in USD)
- **Bitcoin dominance:** 58.7%
- **Best of the tracked coins (24h):** Bitcoin ▼ -1.20%
- **Weakest of the tracked coins (24h):** Dogecoin ▼ -3.63%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €59,252.00 | ▼ -1.20% | ▼ -13.76% | €56,801.64 – €68,934.59 | €1.19 T |
| Ethereum (ETH) | €1,652.55 | ▼ -1.81% | ▼ -18.09% | €1,568.72 – €2,031.28 | €202.0 B |
| BNB (BNB) | €538.90 | ▼ -1.29% | ▼ -14.48% | €518.13 – €632.61 | €70.9 B |
| XRP (XRP) | €0.8774 | ▼ -1.42% | ▼ -16.57% | €0.8147 – €1.05 | €55.7 B |
| Solana (SOL) | €65.49 | ▼ -2.96% | ▼ -18.77% | €61.56 – €81.29 | €38.7 B |
| Dogecoin (DOGE) | €0.0536 | ▼ -3.63% | ▼ -16.73% | €0.0509 – €0.0647 | €8.4 B |
| Cardano (ADA) | €0.1403 | ▼ -2.28% | ▼ -13.72% | €0.1304 – €0.1654 | €5.3 B |

![7-day performance](charts/2026-11-15.svg)

**Recent reports:** [2026-11-15](reports/2026/11/2026-11-15.md) · [2026-11-14](reports/2026/11/2026-11-14.md) · [2026-11-13](reports/2026/11/2026-11-13.md) · [2026-11-12](reports/2026/11/2026-11-12.md) · [2026-11-11](reports/2026/11/2026-11-11.md) · [2026-11-10](reports/2026/11/2026-11-10.md) · [2026-11-09](reports/2026/11/2026-11-09.md)
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
