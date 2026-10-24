"""Illustrative, assumption-driven target DCFs for the Under Armour case.

USD millions. The standalone target value excludes acquisition synergies and
financing effects; it is not an appraisal or an executable offer.
"""

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Target:
    name: str
    ltm_revenue: float
    ltm_operating_income: float
    cash: float
    debt: float
    offer_equity: float
    fees: float
    growth: Sequence[float]
    margins: Sequence[float]
    tax_rate: float
    da_revenue: float
    capex_revenue: float
    nwc_incremental_revenue: float
    wacc: float
    terminal_growth: float


def forecast(target: Target):
    """End-of-year unlevered free cash flow, with incremental NWC investment."""
    revenue = target.ltm_revenue
    rows = []
    for year, (growth, margin) in enumerate(zip(target.growth, target.margins), 1):
        next_revenue = revenue * (1 + growth)
        ebit = next_revenue * margin
        tax = max(ebit, 0) * target.tax_rate
        da = next_revenue * target.da_revenue
        capex = next_revenue * target.capex_revenue
        delta_nwc = (next_revenue - revenue) * target.nwc_incremental_revenue
        fcf = ebit - tax + da - capex - delta_nwc
        rows.append(dict(year=year, revenue=next_revenue, growth=growth, margin=margin,
                         ebit=ebit, cash_tax=tax, da=da, capex=capex,
                         delta_nwc=delta_nwc, fcf=fcf))
        revenue = next_revenue
    return rows


def enterprise_value(target: Target, wacc=None, terminal_growth=None):
    wacc = target.wacc if wacc is None else wacc
    terminal_growth = target.terminal_growth if terminal_growth is None else terminal_growth
    if wacc <= terminal_growth:
        raise ValueError("WACC must exceed terminal growth")
    rows = forecast(target)
    explicit = sum(row['fcf'] / (1 + wacc) ** row['year'] for row in rows)
    terminal = rows[-1]['fcf'] * (1 + terminal_growth) / (wacc - terminal_growth)
    return explicit + terminal / (1 + wacc) ** len(rows)


def deal_bridge(target: Target, stock_share):
    cash_offer = target.offer_equity * (1 - stock_share)
    # Cash acquired, target debt repaid, and transaction fees are distinct.
    closing_cash = 395.981 + target.cash - cash_offer - target.debt - target.fees
    offer_ev = target.offer_equity + target.debt - target.cash
    return dict(offer_ev=offer_ev, cash_offer=cash_offer,
                stock_offer=target.offer_equity * stock_share,
                closing_cash=closing_cash,
                target_standalone_ev=enterprise_value(target),
                value_gap=enterprise_value(target) - offer_ev)


ESCALADE = Target(
    'Escalade', 240.158 + 113.487 - 109.812,
    18.727 + 17.769 - 6.273 - 9.875,
    16.392, 14.881, 18.89 * 13.766074 * 1.25, 6.0,
    (.02, .03, .03, .03, .02), (.0835, .085, .0875, .09, .09),
    .25, .021, .012, .15, .11, .025)

FITLIFE = Target(
    'FitLife', 81.458 + 51.874 - 32.063,
    10.062 + 6.416 - 5.476,
    1.089, 38.1, 77.62 * 1.25, 4.0,
    (.03, .05, .05, .04, .03), (.11, .112, .115, .118, .12),
    .25, .01, .005, .12, .12, .025)


if __name__ == '__main__':
    for target, stock_share in ((ESCALADE, .60), (FITLIFE, .50)):
        print(target.name, deal_bridge(target, stock_share))
