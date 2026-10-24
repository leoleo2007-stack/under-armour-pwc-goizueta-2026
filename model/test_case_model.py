"""Check deal conservation and the difference between acquisition and organic growth."""

import json
import unittest
from pathlib import Path

from case_model import calculate, scenario_table


DATA = json.loads((Path(__file__).resolve().parents[1] / "data" / "inputs.json").read_text())


class ModelTests(unittest.TestCase):
    def test_ltm_bridge_and_historical_combination(self):
        result = calculate(DATA)
        self.assertAlmostEqual(result["fitlife_ltm_revenue_m"], 101.269)
        self.assertAlmostEqual(result["fitlife_ltm_operating_income_m"], 11.002)
        self.assertAlmostEqual(result["historical_combined_revenue_m"], 5067.669)

    def test_cash_and_debt_conservation(self):
        result = calculate(DATA)
        self.assertAlmostEqual(
            result["cash_to_sellers_m"] + result["stock_consideration_m"],
            result["illustrative_offer_equity_m"],
        )
        expected = (
            DATA["under_armour"]["jun2026_cash_m"]
            + DATA["fitlife"]["jun2026_cash_m"]
            - result["cash_to_sellers_m"] - result["debt_repaid_m"]
            - DATA["deal_assumptions"]["transaction_fees_m"]
        )
        self.assertAlmostEqual(result["pro_forma_cash_m"], expected)
        self.assertAlmostEqual(result["pro_forma_debt_m"], DATA["under_armour"]["jun2026_debt_m"])

    def test_cross_sell_does_not_count_all_sales_as_new(self):
        result = calculate(DATA)
        self.assertLess(result["net_new_sales_year3_m"],
                        result["store_gross_sales_year3_m"] + result["online_gross_sales_year3_m"])
        self.assertLess(result["net_new_operating_contribution_year3_m"],
                        result["net_new_sales_year3_m"])

    def test_downside_is_loss_making_and_upside_exceeds_base(self):
        output = scenario_table(DATA)
        self.assertIn("| Downside | 10 | 0.5% | 50% | 5.38 | -2.39 |", output)
        self.assertIn("| Base | 25 | 1.0% | 70% | 17.49 | 3.47 |", output)


if __name__ == "__main__":
    unittest.main()
