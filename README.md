# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-25

- **Total crypto market cap:** €1.88 T (▼ -2.58% in 24h, measured in USD)
- **Bitcoin dominance:** 57.8%
- **Best of the tracked coins (24h):** XRP ▼ -0.44%
- **Weakest of the tracked coins (24h):** Cardano ▼ -1.86%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €54,186.00 | ▼ -0.92% | ▼ -7.29% | €50,719.11 – €58,245.02 | €1.09 T |
| Ethereum (ETH) | €1,520.34 | ▼ -0.94% | ▼ -7.05% | €1,419.30 – €1,649.16 | €185.9 B |
| BNB (BNB) | €497.91 | ▼ -0.55% | ▼ -7.44% | €463.69 – €539.61 | €65.5 B |
| XRP (XRP) | €0.8376 | ▼ -0.44% | ▼ -7.22% | €0.7927 – €0.9034 | €53.2 B |
| Solana (SOL) | €62.81 | ▼ -0.90% | ▼ -7.74% | €59.50 – €69.55 | €37.2 B |
| Dogecoin (DOGE) | €0.0498 | ▼ -1.40% | ▼ -8.78% | €0.0468 – €0.0544 | €7.8 B |
| Cardano (ADA) | €0.1301 | ▼ -1.86% | ▼ -7.18% | €0.1226 – €0.1417 | €4.9 B |

![7-day performance](charts/2026-11-25.svg)

**Recent reports:** [2026-11-25](reports/2026/11/2026-11-25.md) · [2026-11-24](reports/2026/11/2026-11-24.md) · [2026-11-23](reports/2026/11/2026-11-23.md) · [2026-11-22](reports/2026/11/2026-11-22.md) · [2026-11-21](reports/2026/11/2026-11-21.md) · [2026-11-20](reports/2026/11/2026-11-20.md) · [2026-11-19](reports/2026/11/2026-11-19.md)
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
