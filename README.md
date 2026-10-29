# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-10-29

- **Total crypto market cap:** €2.43 T (▼ -3.23% in 24h, measured in USD)
- **Bitcoin dominance:** 59.4%
- **Best of the tracked coins (24h):** Dogecoin ▲ +0.47%
- **Weakest of the tracked coins (24h):** XRP ▼ -1.82%
- **Week:** 1 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €71,958.00 | ▼ -0.29% | ▼ -2.13% | €71,484.85 – €73,647.28 | €1.45 T |
| Ethereum (ETH) | €2,084.98 | ▼ -0.15% | ▼ -3.28% | €2,068.92 – €2,169.91 | €254.7 B |
| BNB (BNB) | €668.09 | ▼ -0.52% | ▲ +1.08% | €648.35 – €683.48 | €87.9 B |
| XRP (XRP) | €1.16 | ▼ -1.82% | ▼ -2.78% | €1.14 – €1.20 | €73.3 B |
| Solana (SOL) | €90.24 | ▼ -0.37% | ▼ -3.81% | €89.41 – €94.48 | €53.2 B |
| Dogecoin (DOGE) | €0.0710 | ▲ +0.47% | ▼ -0.51% | €0.0680 – €0.0723 | €11.1 B |
| Cardano (ADA) | €0.1810 | ▼ -0.18% | ▼ -7.21% | €0.1774 – €0.1959 | €6.8 B |

![7-day performance](charts/2026-10-29.svg)

**Recent reports:** [2026-10-29](reports/2026/10/2026-10-29.md) · [2026-10-28](reports/2026/10/2026-10-28.md)
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
