# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-13

- **Total crypto market cap:** €2.12 T (▼ -5.81% in 24h, measured in USD)
- **Bitcoin dominance:** 58.9%
- **Best of the tracked coins (24h):** Cardano ▲ +2.36%
- **Weakest of the tracked coins (24h):** Bitcoin ▼ -3.43%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €62,301.00 | ▼ -3.43% | ▼ -8.49% | €61,557.21 – €68,849.72 | €1.25 T |
| Ethereum (ETH) | €1,762.58 | ▼ -2.46% | ▼ -12.04% | €1,726.78 – €2,033.32 | €215.4 B |
| BNB (BNB) | €577.02 | ▼ -1.98% | ▼ -7.42% | €565.62 – €632.56 | €75.9 B |
| XRP (XRP) | €0.9326 | ▲ +0.78% | ▼ -13.08% | €0.9089 – €1.08 | €59.3 B |
| Solana (SOL) | €73.02 | ▼ -0.19% | ▼ -9.58% | €70.84 – €82.19 | €43.2 B |
| Dogecoin (DOGE) | €0.0595 | ▲ +1.31% | ▼ -8.68% | €0.0572 – €0.0661 | €9.3 B |
| Cardano (ADA) | €0.1565 | ▲ +2.36% | ▼ -6.73% | €0.1513 – €0.1701 | €5.9 B |

![7-day performance](charts/2026-11-13.svg)

**Recent reports:** [2026-11-13](reports/2026/11/2026-11-13.md) · [2026-11-12](reports/2026/11/2026-11-12.md) · [2026-11-11](reports/2026/11/2026-11-11.md) · [2026-11-10](reports/2026/11/2026-11-10.md) · [2026-11-09](reports/2026/11/2026-11-09.md) · [2026-11-08](reports/2026/11/2026-11-08.md) · [2026-11-07](reports/2026/11/2026-11-07.md)
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
