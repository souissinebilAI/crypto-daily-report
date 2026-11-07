# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-07

- **Total crypto market cap:** €2.30 T (▼ -2.83% in 24h, measured in USD)
- **Bitcoin dominance:** 59.3%
- **Best of the tracked coins (24h):** Ethereum ▲ +0.58%
- **Weakest of the tracked coins (24h):** Cardano ▼ -1.86%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €68,040.00 | ▲ +0.27% | ▼ -2.20% | €67,697.19 – €72,372.04 | €1.37 T |
| Ethereum (ETH) | €2,010.52 | ▲ +0.58% | ▼ -0.30% | €1,994.57 – €2,184.44 | €245.7 B |
| BNB (BNB) | €623.39 | ▲ +0.09% | ▼ -1.53% | €614.82 – €647.22 | €82.0 B |
| XRP (XRP) | €1.04 | ▼ -1.45% | ▼ -6.99% | €1.04 – €1.19 | €66.4 B |
| Solana (SOL) | €80.62 | ▼ -0.33% | ▼ -6.40% | €79.81 – €86.83 | €47.6 B |
| Dogecoin (DOGE) | €0.0645 | ▼ -0.55% | ▼ -4.59% | €0.0638 – €0.0696 | €10.1 B |
| Cardano (ADA) | €0.1639 | ▼ -1.86% | ▼ -5.20% | €0.1621 – €0.1793 | €6.2 B |

![7-day performance](charts/2026-11-07.svg)

**Recent reports:** [2026-11-07](reports/2026/11/2026-11-07.md) · [2026-11-06](reports/2026/11/2026-11-06.md) · [2026-11-05](reports/2026/11/2026-11-05.md) · [2026-11-04](reports/2026/11/2026-11-04.md) · [2026-11-03](reports/2026/11/2026-11-03.md) · [2026-11-02](reports/2026/11/2026-11-02.md) · [2026-11-01](reports/2026/11/2026-11-01.md)
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
