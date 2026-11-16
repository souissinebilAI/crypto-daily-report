# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-11-16

- **Total crypto market cap:** €2.01 T (▼ -1.35% in 24h, measured in USD)
- **Bitcoin dominance:** 58.5%
- **Best of the tracked coins (24h):** Dogecoin ▲ +1.55%
- **Weakest of the tracked coins (24h):** Solana ▼ -0.32%
- **Week:** 0 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €58,732.00 | ▲ +0.26% | ▼ -13.82% | €56,880.81 – €68,557.00 | €1.18 T |
| Ethereum (ETH) | €1,657.70 | ▲ +0.75% | ▼ -14.44% | €1,570.91 – €1,949.44 | €202.6 B |
| BNB (BNB) | €535.57 | ▲ +0.03% | ▼ -14.44% | €518.86 – €627.35 | €70.4 B |
| XRP (XRP) | €0.8685 | ▲ +0.53% | ▼ -13.36% | €0.8158 – €1.01 | €55.2 B |
| Solana (SOL) | €64.57 | ▼ -0.32% | ▼ -18.80% | €61.64 – €79.81 | €38.2 B |
| Dogecoin (DOGE) | €0.0538 | ▲ +1.55% | ▼ -16.19% | €0.0510 – €0.0643 | €8.4 B |
| Cardano (ADA) | €0.1388 | ▼ -0.04% | ▼ -15.91% | €0.1306 – €0.1656 | €5.2 B |

![7-day performance](charts/2026-11-16.svg)

**Recent reports:** [2026-11-16](reports/2026/11/2026-11-16.md) · [2026-11-15](reports/2026/11/2026-11-15.md) · [2026-11-14](reports/2026/11/2026-11-14.md) · [2026-11-13](reports/2026/11/2026-11-13.md) · [2026-11-12](reports/2026/11/2026-11-12.md) · [2026-11-11](reports/2026/11/2026-11-11.md) · [2026-11-10](reports/2026/11/2026-11-10.md)
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
