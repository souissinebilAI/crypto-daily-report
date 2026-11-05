# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-05

- **Total crypto market cap:** €2.35 T (▼ -2.49% in 24h, measured in USD)
- **Bitcoin dominance:** 59.4%
- **Best of the tracked coins (24h):** BNB ▼ -0.91%
- **Weakest of the tracked coins (24h):** Cardano ▼ -3.45%
- **Week:** 1 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €69,625.00 | ▼ -1.31% | ▼ -2.53% | €67,942.27 – €72,840.29 | €1.40 T |
| Ethereum (ETH) | €2,083.60 | ▼ -1.93% | ▲ +0.67% | €1,954.17 – €2,171.04 | €254.8 B |
| BNB (BNB) | €625.24 | ▼ -0.91% | ▼ -5.66% | €611.05 – €668.17 | €82.3 B |
| XRP (XRP) | €1.14 | ▼ -2.97% | ▼ -0.78% | €1.08 – €1.18 | €72.3 B |
| Solana (SOL) | €82.75 | ▼ -2.43% | ▼ -7.60% | €81.09 – €91.46 | €48.9 B |
| Dogecoin (DOGE) | €0.0660 | ▼ -3.43% | ▼ -6.32% | €0.0653 – €0.0718 | €10.3 B |
| Cardano (ADA) | €0.1689 | ▼ -3.45% | ▼ -5.95% | €0.1653 – €0.1839 | €6.4 B |

![7-day performance](charts/2026-11-05.svg)

**Recent reports:** [2026-11-05](reports/2026/11/2026-11-05.md) · [2026-11-04](reports/2026/11/2026-11-04.md) · [2026-11-03](reports/2026/11/2026-11-03.md) · [2026-11-02](reports/2026/11/2026-11-02.md) · [2026-11-01](reports/2026/11/2026-11-01.md) · [2026-10-31](reports/2026/10/2026-10-31.md) · [2026-10-30](reports/2026/10/2026-10-30.md)
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
