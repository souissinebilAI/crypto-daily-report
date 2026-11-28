# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-28

- **Total crypto market cap:** €1.89 T (▼ -2.71% in 24h, measured in USD)
- **Bitcoin dominance:** 57.7%
- **Best of the tracked coins (24h):** BNB ▼ -0.17%
- **Weakest of the tracked coins (24h):** Cardano ▼ -2.14%
- **Week:** 4 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €54,330.00 | ▼ -0.95% | ▼ -2.06% | €52,997.18 – €58,190.28 | €1.09 T |
| Ethereum (ETH) | €1,506.96 | ▼ -1.32% | ▼ -3.21% | €1,489.14 – €1,648.98 | €184.2 B |
| BNB (BNB) | €504.65 | ▼ -0.17% | ▲ +0.62% | €487.22 – €526.87 | €66.4 B |
| XRP (XRP) | €0.8599 | ▼ -1.05% | ▲ +0.95% | €0.8163 – €0.9056 | €54.6 B |
| Solana (SOL) | €64.54 | ▼ -1.89% | ▼ -0.30% | €61.01 – €69.79 | €38.2 B |
| Dogecoin (DOGE) | €0.0516 | ▼ -2.13% | ▲ +2.32% | €0.0483 – €0.0539 | €8.1 B |
| Cardano (ADA) | €0.1329 | ▼ -2.14% | ▲ +1.42% | €0.1254 – €0.1407 | €5.0 B |

![7-day performance](charts/2026-11-28.svg)

**Recent reports:** [2026-11-28](reports/2026/11/2026-11-28.md) · [2026-11-27](reports/2026/11/2026-11-27.md) · [2026-11-26](reports/2026/11/2026-11-26.md) · [2026-11-25](reports/2026/11/2026-11-25.md) · [2026-11-24](reports/2026/11/2026-11-24.md) · [2026-11-23](reports/2026/11/2026-11-23.md) · [2026-11-22](reports/2026/11/2026-11-22.md)
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
