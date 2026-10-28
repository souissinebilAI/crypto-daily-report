import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import report  # noqa: E402


def coin(cid, symbol, price, d24, d7, week):
    return {"id": cid, "name": cid.title(), "symbol": symbol, "current_price": price,
            "market_cap": price * 1e7, "price_change_percentage_24h_in_currency": d24,
            "price_change_percentage_7d_in_currency": d7, "sparkline_in_7d": {"price": week}}


COINS = [coin("bitcoin", "btc", 60000, 1.5, -2.0, [61000, 59000, None, 60000]),
         coin("ethereum", "eth", 2500, -3.25, 4.0, [2400, 2450, 2500])]
MARKET = {"data": {"total_market_cap": {"eur": 2.1e12}, "market_cap_change_percentage_24h_usd": 0.8,
                   "market_cap_percentage": {"btc": 56.42}}}


class FormatTest(unittest.TestCase):
    def test_eur(self):
        self.assertEqual(report.fmt_eur(2.1e12), "€2.10 T")
        self.assertEqual(report.fmt_eur(1.25e9), "€1.2 B")
        self.assertEqual(report.fmt_eur(60000), "€60,000.00")
        self.assertEqual(report.fmt_eur(0.12345), "€0.1235")

    def test_pct(self):
        self.assertEqual(report.fmt_pct(1.5), "▲ +1.50%")
        self.assertEqual(report.fmt_pct(-3.25), "▼ -3.25%")
        self.assertEqual(report.fmt_pct(None), "n/a")


class ContentTest(unittest.TestCase):
    def test_table_skips_missing_points(self):
        table = report.coin_table(COINS)
        self.assertIn("| Bitcoin (BTC) | €60,000.00 | ▲ +1.50% | ▼ -2.00% | €59,000.00 – €61,000.00 |", table)

    def test_summary_names_best_and_worst(self):
        text = report.summary(COINS, MARKET)
        self.assertIn("Best of the tracked coins (24h):** Bitcoin", text)
        self.assertIn("Weakest of the tracked coins (24h):** Ethereum", text)
        self.assertIn("1 of 2 tracked coins are up", text)

    def test_chart_is_svg_with_a_line_per_coin(self):
        svg = report.chart_svg(COINS)
        self.assertTrue(svg.startswith("<svg"))
        self.assertEqual(svg.count("<polyline"), 2)
        self.assertIn("ETH +4.2%", svg)


if __name__ == "__main__":
    unittest.main()
