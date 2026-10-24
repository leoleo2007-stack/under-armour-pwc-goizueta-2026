"""Transparent screening model for the Under Armour / FitLife case.

All financial outputs are USD millions unless a label says otherwise.
No external packages or network access are required.
"""

from __future__ import annotations

import json
import copy
import sys
from pathlib import Path

INPUTS = Path(__file__).resolve().parents[1] / "data" / "inputs.json"


def calculate(data: dict) -> dict:
    ua, fit, deal, commercial = (
        data["under_armour"], data["fitlife"], data["deal_assumptions"],
        data["year3_commercial_assumptions"],
    )
    target_ltm_revenue = fit["fy2025_revenue_m"] + fit["h1_2026_revenue_m"] - fit["h1_2025_revenue_m"]
    target_ltm_operating_income = (
        fit["fy2025_operating_income_m"]
        + fit["h1_2026_operating_income_m"]
        - fit["h1_2025_operating_income_m"]
    )
    equity_value = fit["oct22_market_cap_m"] * (1 + deal["equity_premium"])
    stock_value = equity_value * deal["stock_consideration_share"]
    cash_to_sellers = equity_value - stock_value
    debt_repayment = fit["jun2026_debt_m"] if deal["retire_target_debt_at_close"] else 0.0
    combined_debt = ua["jun2026_debt_m"] + fit["jun2026_debt_m"] - debt_repayment
    combined_cash = (
        ua["jun2026_cash_m"] + fit["jun2026_cash_m"]
        - cash_to_sellers - debt_repayment - deal["transaction_fees_m"]
    )
    # The UA quote is an illustration. Actual issued Class C shares need deal terms.
    shares_issued_m = stock_value / ua["share_price_usd"]
    enterprise_value = equity_value + fit["jun2026_debt_m"] - fit["jun2026_cash_m"]
    store_sales_m = (
        ua["stores"] * commercial["store_incremental_transactions_per_week"]
        * commercial["supplement_basket_usd"] * commercial["weeks"] / 1_000_000
    )
    online_sales_m = (
        ua["fy2026_dtc_revenue_m"] * 1_000_000 / commercial["ua_dtc_order_value_usd"]
        * commercial["online_attach_rate"] * commercial["supplement_basket_usd"] / 1_000_000
    )
    net_new_sales_m = (store_sales_m + online_sales_m) * commercial["new_to_combined_group_share"]
    net_new_operating_m = (
        net_new_sales_m * commercial["incremental_gross_margin"]
        - commercial["annual_incremental_marketing_and_operations_m"]
    )
    return {
        "fitlife_ltm_revenue_m": target_ltm_revenue,
        "fitlife_ltm_operating_income_m": target_ltm_operating_income,
        "historical_combined_revenue_m": ua["fy2026_revenue_m"] + target_ltm_revenue,
        "historical_combined_operating_income_m": ua["fy2026_operating_income_m"] + target_ltm_operating_income,
        "illustrative_offer_equity_m": equity_value,
        "illustrative_enterprise_value_m": enterprise_value,
        "stock_consideration_m": stock_value,
        "cash_to_sellers_m": cash_to_sellers,
        "debt_repaid_m": debt_repayment,
        "illustrative_new_class_c_shares_m": shares_issued_m,
        "pro_forma_cash_m": combined_cash,
        "pro_forma_debt_m": combined_debt,
        "store_gross_sales_year3_m": store_sales_m,
        "online_gross_sales_year3_m": online_sales_m,
        "net_new_sales_year3_m": net_new_sales_m,
        "net_new_operating_contribution_year3_m": net_new_operating_m,
    }


def render(results: dict) -> str:
    rows = ["| Metric | USD millions unless noted |", "|---|---:|"]
    labels = {
        "fitlife_ltm_revenue_m": "FitLife LTM revenue (FY25 + H1 26 - H1 25)",
        "fitlife_ltm_operating_income_m": "FitLife LTM operating income",
        "historical_combined_revenue_m": "Historical combined revenue (non-contemporaneous periods)",
        "historical_combined_operating_income_m": "Historical combined operating income (before PPA/synergies)",
        "illustrative_offer_equity_m": "Offer equity value (25% premium assumption)",
        "illustrative_enterprise_value_m": "Implied enterprise value",
        "stock_consideration_m": "Stock issued as consideration",
        "cash_to_sellers_m": "Cash paid to sellers",
        "debt_repaid_m": "FitLife debt repaid at closing",
        "illustrative_new_class_c_shares_m": "Illustrative new UA Class C shares (millions)",
        "pro_forma_cash_m": "Cash immediately after close (illustrative)",
        "pro_forma_debt_m": "Debt immediately after close (illustrative)",
        "store_gross_sales_year3_m": "Year 3 store cross-sell before overlap",
        "online_gross_sales_year3_m": "Year 3 online cross-sell before overlap",
        "net_new_sales_year3_m": "Year 3 net-new cross-sell after overlap",
        "net_new_operating_contribution_year3_m": "Year 3 incremental operating contribution",
    }
    for key, label in labels.items():
        rows.append(f"| {label} | {results[key]:,.2f} |")
    return "\n".join(rows)


def scenario_table(data: dict) -> str:
    """Three explicitly assumed adoption cases, not probability-weighted forecasts."""
    variants = {
        "Downside": (10, 0.005, 0.50, 0.30, 4.0),
        "Base": (25, 0.010, 0.70, 0.37, 3.0),
        "Upside": (40, 0.015, 0.85, 0.40, 4.0),
    }
    rows = [
        "| Scenario | Store transactions/week | Online attach | Net-new share | Incremental sales ($m) | Operating contribution ($m) |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, (store_tx, attach, net_new_share, margin, expense) in variants.items():
        variant = copy.deepcopy(data)
        assumptions = variant["year3_commercial_assumptions"]
        assumptions.update({
            "store_incremental_transactions_per_week": store_tx,
            "online_attach_rate": attach,
            "new_to_combined_group_share": net_new_share,
            "incremental_gross_margin": margin,
            "annual_incremental_marketing_and_operations_m": expense,
        })
        result = calculate(variant)
        rows.append(
            f"| {name} | {store_tx} | {attach:.1%} | {net_new_share:.0%} | "
            f"{result['net_new_sales_year3_m']:.2f} | "
            f"{result['net_new_operating_contribution_year3_m']:.2f} |"
        )
    return "\n".join(rows)


if __name__ == "__main__":
    data = json.loads(INPUTS.read_text())
    print(render(calculate(data)))
    if "--scenarios" in sys.argv:
        print("\nIllustrative Year 3 adoption sensitivity:\n")
        print(scenario_table(data))
