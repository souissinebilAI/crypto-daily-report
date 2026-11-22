# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-22

- **Total crypto market cap:** €1.92 T (▼ -2.18% in 24h, measured in USD)
- **Bitcoin dominance:** 58.0%
- **Best of the tracked coins (24h):** BNB ▲ +2.05%
- **Weakest of the tracked coins (24h):** XRP ▼ -0.56%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €55,492.00 | ▲ +1.08% | ▼ -7.35% | €50,794.12 – €59,650.51 | €1.12 T |
| Ethereum (ETH) | €1,559.49 | ▲ +1.51% | ▼ -7.25% | €1,421.40 – €1,683.14 | €190.6 B |
| BNB (BNB) | €508.23 | ▲ +2.05% | ▼ -7.23% | €464.38 – €544.17 | €66.8 B |
| XRP (XRP) | €0.8422 | ▼ -0.56% | ▼ -5.00% | €0.7939 – €0.9135 | €53.5 B |
| Solana (SOL) | €64.04 | ▼ -0.44% | ▼ -3.84% | €59.59 – €68.50 | €37.9 B |
| Dogecoin (DOGE) | €0.0502 | ▼ -0.36% | ▼ -7.49% | €0.0469 – €0.0548 | €7.9 B |
| Cardano (ADA) | €0.1317 | ▼ -0.09% | ▼ -7.47% | €0.1228 – €0.1419 | €4.9 B |

![7-day performance](charts/2026-11-22.svg)

**Recent reports:** [2026-11-22](reports/2026/11/2026-11-22.md) · [2026-11-21](reports/2026/11/2026-11-21.md) · [2026-11-20](reports/2026/11/2026-11-20.md) · [2026-11-19](reports/2026/11/2026-11-19.md) · [2026-11-18](reports/2026/11/2026-11-18.md) · [2026-11-17](reports/2026/11/2026-11-17.md) · [2026-11-16](reports/2026/11/2026-11-16.md)
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
