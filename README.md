# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-08

- **Total crypto market cap:** €2.27 T (▼ -3.59% in 24h, measured in USD)
- **Bitcoin dominance:** 60.0%
- **Best of the tracked coins (24h):** BNB ▲ +0.16%
- **Weakest of the tracked coins (24h):** Cardano ▼ -1.76%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €67,997.00 | ▼ -0.08% | ▼ -2.61% | €67,675.82 – €72,349.19 | €1.37 T |
| Ethereum (ETH) | €2,003.24 | ▼ -0.44% | ▼ -1.39% | €1,993.94 – €2,183.75 | €244.8 B |
| BNB (BNB) | €624.41 | ▲ +0.16% | ▼ -2.13% | €614.63 – €647.02 | €82.1 B |
| XRP (XRP) | €1.04 | ▼ -0.54% | ▼ -7.25% | €1.04 – €1.19 | €66.0 B |
| Solana (SOL) | €79.92 | ▼ -0.90% | ▼ -6.05% | €79.78 – €86.80 | €47.2 B |
| Dogecoin (DOGE) | €0.0638 | ▼ -1.07% | ▼ -5.98% | €0.0635 – €0.0696 | €10.0 B |
| Cardano (ADA) | €0.1610 | ▼ -1.76% | ▼ -6.78% | €0.1611 – €0.1792 | €6.0 B |

![7-day performance](charts/2026-11-08.svg)

**Recent reports:** [2026-11-08](reports/2026/11/2026-11-08.md) · [2026-11-07](reports/2026/11/2026-11-07.md) · [2026-11-06](reports/2026/11/2026-11-06.md) · [2026-11-05](reports/2026/11/2026-11-05.md) · [2026-11-04](reports/2026/11/2026-11-04.md) · [2026-11-03](reports/2026/11/2026-11-03.md) · [2026-11-02](reports/2026/11/2026-11-02.md)
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
