# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-09

- **Total crypto market cap:** €2.25 T (▼ -3.19% in 24h, measured in USD)
- **Bitcoin dominance:** 59.6%
- **Best of the tracked coins (24h):** Cardano ▼ -0.15%
- **Weakest of the tracked coins (24h):** XRP ▼ -5.08%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €66,946.00 | ▼ -1.38% | ▼ -2.96% | €65,896.79 – €72,002.11 | €1.35 T |
| Ethereum (ETH) | €1,903.85 | ▼ -4.67% | ▼ -6.19% | €1,867.16 – €2,173.28 | €232.6 B |
| BNB (BNB) | €614.08 | ▼ -1.55% | ▼ -1.90% | €602.69 – €643.91 | €80.8 B |
| XRP (XRP) | €0.9823 | ▼ -5.08% | ▼ -10.99% | €0.9640 – €1.18 | €62.4 B |
| Solana (SOL) | €77.65 | ▼ -2.60% | ▼ -6.82% | €76.33 – €86.38 | €45.9 B |
| Dogecoin (DOGE) | €0.0625 | ▼ -1.71% | ▼ -5.87% | €0.0607 – €0.0692 | €9.8 B |
| Cardano (ADA) | €0.1604 | ▼ -0.15% | ▼ -4.23% | €0.1537 – €0.1784 | €6.0 B |

![7-day performance](charts/2026-11-09.svg)

**Recent reports:** [2026-11-09](reports/2026/11/2026-11-09.md) · [2026-11-08](reports/2026/11/2026-11-08.md) · [2026-11-07](reports/2026/11/2026-11-07.md) · [2026-11-06](reports/2026/11/2026-11-06.md) · [2026-11-05](reports/2026/11/2026-11-05.md) · [2026-11-04](reports/2026/11/2026-11-04.md) · [2026-11-03](reports/2026/11/2026-11-03.md)
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
