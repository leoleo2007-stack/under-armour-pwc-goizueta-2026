import unittest
from valuation import ESCALADE, FITLIFE, deal_bridge, enterprise_value, forecast


class ValuationTests(unittest.TestCase):
    def test_tariff_adjusted_earnings_and_ltm_revenue(self):
        self.assertAlmostEqual(ESCALADE.ltm_operating_income, 20.348)
        self.assertAlmostEqual(ESCALADE.ltm_revenue, 243.833)
        self.assertAlmostEqual(FITLIFE.ltm_revenue, 101.269)

    def test_value_and_cash_bridges(self):
        for target, mix in [(ESCALADE, .6), (FITLIFE, .5)]:
            b = deal_bridge(target, mix)
            self.assertAlmostEqual(b['offer_ev'], target.offer_equity + target.debt - target.cash)
            self.assertAlmostEqual(b['cash_offer'] + b['stock_offer'], target.offer_equity)
            self.assertAlmostEqual(b['closing_cash'], 395.981 + target.cash - b['cash_offer'] - target.debt - target.fees)
            self.assertAlmostEqual(b['value_gap'], b['target_standalone_ev'] - b['offer_ev'])

    def test_discount_rate_and_reinvestment_sensitivities(self):
        for target in [ESCALADE, FITLIFE]:
            self.assertLess(enterprise_value(target, target.wacc + .01), enterprise_value(target))
            self.assertGreater(enterprise_value(target, terminal_growth=target.terminal_growth + .005), enterprise_value(target))
            self.assertEqual(len(forecast(target)), 5)
            self.assertTrue(all(row['fcf'] > 0 for row in forecast(target)))
            with self.assertRaises(ValueError):
                enterprise_value(target, target.terminal_growth)


if __name__ == '__main__':
    unittest.main()
