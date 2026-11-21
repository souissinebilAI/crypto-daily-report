# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-21

- **Total crypto market cap:** €1.90 T (▼ -4.82% in 24h, measured in USD)
- **Bitcoin dominance:** 58.0%
- **Best of the tracked coins (24h):** Solana ▼ -0.30%
- **Weakest of the tracked coins (24h):** BNB ▼ -3.79%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €54,891.00 | ▼ -2.21% | ▼ -9.69% | €50,794.40 – €60,892.25 | €1.10 T |
| Ethereum (ETH) | €1,537.64 | ▼ -2.93% | ▼ -10.48% | €1,421.40 – €1,725.04 | €188.0 B |
| BNB (BNB) | €498.08 | ▼ -3.79% | ▼ -10.88% | €464.38 – €553.53 | €65.5 B |
| XRP (XRP) | €0.8471 | ▼ -1.20% | ▼ -6.29% | €0.7939 – €0.9135 | €53.8 B |
| Solana (SOL) | €64.33 | ▼ -0.30% | ▼ -6.48% | €59.59 – €68.82 | €38.1 B |
| Dogecoin (DOGE) | €0.0504 | ▼ -1.59% | ▼ -11.92% | €0.0469 – €0.0570 | €7.9 B |
| Cardano (ADA) | €0.1318 | ▼ -1.02% | ▼ -11.25% | €0.1228 – €0.1466 | €5.0 B |

![7-day performance](charts/2026-11-21.svg)

**Recent reports:** [2026-11-21](reports/2026/11/2026-11-21.md) · [2026-11-20](reports/2026/11/2026-11-20.md) · [2026-11-19](reports/2026/11/2026-11-19.md) · [2026-11-18](reports/2026/11/2026-11-18.md) · [2026-11-17](reports/2026/11/2026-11-17.md) · [2026-11-16](reports/2026/11/2026-11-16.md) · [2026-11-15](reports/2026/11/2026-11-15.md)
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
