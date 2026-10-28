# Crypto Daily Report

An automated daily review of the crypto market. Every morning at about 09:00 (Berlin time) a
GitHub Actions workflow fetches prices from the public [CoinGecko API](https://www.coingecko.com/en/api),
writes a Markdown report with a 7-day chart, appends the numbers to a CSV history and updates this page.

The commits labelled `chore(bot): daily market report` are made by that workflow, not by hand.

## Latest report

<!-- LATEST:START -->
### 2026-10-28

- **Total crypto market cap:** €2.46 T (▼ -0.92% in 24h, measured in USD)
- **Bitcoin dominance:** 59.5%
- **Best of the tracked coins (24h):** Dogecoin ▲ +3.70%
- **Weakest of the tracked coins (24h):** XRP ▲ +1.44%
- **Week:** 1 of 7 tracked coins are up over 7 days.

| Coin | Price | 24h | 7d | 7d range | Market cap |
|---|---:|---:|---:|---:|---:|
| Bitcoin (BTC) | €72,818.00 | ▲ +1.79% | ▼ -2.49% | €71,397.34 – €76,146.93 | €1.46 T |
| Ethereum (ETH) | €2,111.10 | ▲ +1.85% | ▼ -3.90% | €2,066.39 – €2,257.62 | €257.9 B |
| BNB (BNB) | €681.10 | ▲ +2.79% | ▲ +1.87% | €647.56 – €681.97 | €89.6 B |
| XRP (XRP) | €1.18 | ▲ +1.44% | ▼ -2.42% | €1.14 – €1.25 | €75.0 B |
| Solana (SOL) | €91.84 | ▲ +2.52% | ▼ -3.66% | €89.30 – €97.51 | €54.2 B |
| Dogecoin (DOGE) | €0.0717 | ▲ +3.70% | ▼ -2.21% | €0.0679 – €0.0749 | €11.2 B |
| Cardano (ADA) | €0.1846 | ▲ +1.45% | ▼ -8.23% | €0.1808 – €0.2056 | €6.9 B |

![7-day performance](charts/2026-10-28.svg)

**Recent reports:** [2026-10-28](reports/2026/10/2026-10-28.md)
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
