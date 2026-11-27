# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-27

- **Total crypto market cap:** €1.91 T (▼ -2.99% in 24h, measured in USD)
- **Bitcoin dominance:** 57.8%
- **Best of the tracked coins (24h):** Solana ▲ +1.80%
- **Weakest of the tracked coins (24h):** Ethereum ▼ -1.05%
- **Week:** 7 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €54,761.00 | ▼ -0.70% | ▲ +1.04% | €50,934.43 – €58,235.51 | €1.10 T |
| Ethereum (ETH) | €1,524.95 | ▼ -1.05% | ▲ +1.21% | €1,425.32 – €1,650.26 | €186.6 B |
| BNB (BNB) | €504.50 | ▲ +0.41% | ▲ +1.29% | €465.66 – €527.28 | €66.4 B |
| XRP (XRP) | €0.8669 | ▲ +0.21% | ▲ +4.47% | €0.7961 – €0.9063 | €55.1 B |
| Solana (SOL) | €65.82 | ▲ +1.80% | ▲ +5.64% | €59.75 – €69.85 | €39.0 B |
| Dogecoin (DOGE) | €0.0526 | ▲ +1.79% | ▲ +7.08% | €0.0470 – €0.0539 | €8.3 B |
| Cardano (ADA) | €0.1360 | ▲ +0.16% | ▲ +6.49% | €0.1232 – €0.1408 | €5.1 B |

![7-day performance](charts/2026-11-27.svg)

**Recent reports:** [2026-11-27](reports/2026/11/2026-11-27.md) · [2026-11-26](reports/2026/11/2026-11-26.md) · [2026-11-25](reports/2026/11/2026-11-25.md) · [2026-11-24](reports/2026/11/2026-11-24.md) · [2026-11-23](reports/2026/11/2026-11-23.md) · [2026-11-22](reports/2026/11/2026-11-22.md) · [2026-11-21](reports/2026/11/2026-11-21.md)
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
