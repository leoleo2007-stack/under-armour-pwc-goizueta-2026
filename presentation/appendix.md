# Under Armour target diligence and valuation appendix

**Information cut-off:** October 22, 2026. **Units:** USD millions unless stated. This is a case exercise and an illustrative screen, not a fairness opinion. The accompanying [live workbook](../outputs/target_valuation.xlsx) is the calculation source; [valuation chart](figures/valuation_comparison.png), [cash-flow chart](figures/fcf_forecasts.png), and [sensitivity chart](figures/dcf_sensitivity.png) are reproducible with the scripts in `model/`.

## A1. Decision and case compliance

The prompt calls for a smaller company in a different industry than UA apparel and footwear. FitLife (nutritional supplements) is clearly separate; Escalade (sporting equipment) is distinct in products and industrial classification but may be judged too close to sportswear. Ask the organizers for a ruling **before using Escalade as the final target**. Neither full-company acquisition should be recommended at the indicative 25% premium without additional, evidenced synergies or a materially better price. A commercial pilot and a disciplined bid ceiling are more defensible interim actions.

| Item | Escalade | FitLife |
|---|---:|---:|
| LTM June 2026 revenue | 243.833 | 101.269 |
| LTM June 2026 operating income used | 20.348, excluding 9.875 tariff recovery | 11.002 GAAP |
| Illustrative equity offer at 25% premium | 325.051 | 97.025 |
| Offer EV, equity + debt - cash | 323.540 | 134.036 |
| Standalone enterprise DCF, base case | 214.101 | 104.259 |
| Standalone EV less offer EV | **(109.440)** | **(29.777)** |
| DCF equity value, EV - debt + cash | 215.612 | 67.248 |
| UA closing cash under modeled mix and fees | 261.471 | 306.458 |

The **DCF gap is not a cash loss booked at closing**. It is the incremental present value that risk-adjusted synergies would need to cover before deal fees and integration costs. At the assumed price, Escalade requires $109.4m of net synergy value and FitLife $29.8m. A $250m minimum cash balance is a team placeholder; UA's seasonal liquidity requirements have not been independently established.

## A2. Historical operating and reinvestment bridge

| Metric | Escalade | FitLife | Calculation |
|---|---:|---:|---|
| FY2025 revenue | 240.158 | 81.458 | Filed 10-K |
| H1 2026 revenue | 113.487 | 51.874 | Filed June 10-Q |
| H1 2025 revenue | 109.812 | 32.063 | Filed June 10-Q |
| LTM revenue | 243.833 | 101.269 | FY2025 + H1 2026 - H1 2025 |
| FY2025 operating income | 18.727 | 10.062 | Filed 10-K |
| H1 2026 operating income | 17.769 | 6.416 | Filed June 10-Q |
| H1 2025 operating income | 6.273 | 5.476 | Filed June 10-Q |
| LTM GAAP operating income | 30.223 | 11.002 | FY2025 + H1 2026 - H1 2025 |
| One-off tariff recovery removed | (9.875) | - | Escalade H1 2026 filing |
| LTM income used in DCF calibration | **20.348** | **11.002** | FitLife GAAP remains acquisition affected |
| FY2025 D&A | 5.063 | 0.420 | Filed cash flows |
| H1 2026 / H1 2025 D&A | 2.503 / 2.501 | 0.500 / 0.033 | Filed cash flows |
| Implied LTM D&A | 5.065 | 0.887 | Context, not the future D&A assumption |
| FY2025 capex | 2.512 | 0.042 | Filed cash flows |
| H1 2026 / H1 2025 capex | 1.290 / 0.976 | 0 / 0.029 | Filed cash flows |
| Implied LTM capex | 2.826 | 0.013 | FitLife future assumption is deliberately higher |

Escalade's H1 reported profit includes tariff refunds and some H1 revenue growth reflects the Gold Tip acquisition. FitLife's H1 revenue growth includes Irwin Naturals acquired in August 2025; its legacy brands declined 23% in Q2. Neither reported growth rate should be extrapolated as organic. [Escalade 10-K](https://www.sec.gov/Archives/edgar/data/33488/000143774926006094/esca20251231_10k.htm), [Escalade 10-Q](https://www.sec.gov/Archives/edgar/data/33488/000143774926024943/esca20260630_10q.htm), [Escalade Q2 release](https://escaladeinc.com/escalade-reports-second-quarter-2026-results-2026-07-30/), [FitLife 10-K](https://www.sec.gov/Archives/edgar/data/1374328/000143774926010680/ftlf20251231_10k.htm), [FitLife 10-Q](https://www.sec.gov/Archives/edgar/data/1374328/000143774926027478/ftlf20260630_10q.htm), [FitLife Q2 release](https://www.sec.gov/Archives/edgar/data/1374328/000143774926027493/ex_1004382.htm).

## A3. DCF method and editable assumptions

Forecast revenue = prior revenue x (1 + growth). EBIT = revenue x margin. Unlevered FCF = EBIT - max(EBIT, 0) x cash tax rate + D&A - capex - change in operating NWC. D&A and capex are modeled as revenue percentages; NWC investment is a percentage of **incremental** revenue. FCF is discounted at the end of each rolling year following the June 2026 LTM. Terminal value = Year 5 FCF x (1 + g) / (WACC - g), discounted five years. Equity value = operating EV - June target debt + June target cash. No leverage tax shield or acquisition synergy is embedded in standalone EV.

| Driver | Escalade Y1-Y5 | FitLife Y1-Y5 | Status |
|---|---|---|---|
| Revenue growth | 2%, 3%, 3%, 3%, 2% | 3%, 5%, 5%, 4%, 3% | Team assumptions; organic/acquired mix unverified |
| Operating margin | 8.35%, 8.5%, 8.75%, 9%, 9% | 11%, 11.2%, 11.5%, 11.8%, 12% | Team assumptions, calibrated to normalized/GAAP LTM |
| Cash tax rate | 25% | 25% | Team assumption; tax attributes not diligenced |
| D&A / sales | 2.1% | 1.0% | Team assumption informed by historical LTM |
| Capex / sales | 1.2% | 0.5% | Team assumption; FitLife above recent unusually low capex |
| NWC investment / new sales | 15% | 12% | Team assumption; no full working capital forecast |
| WACC / terminal growth | 11% / 2.5% | 12% / 2.5% | Illustrative discount assumptions, not a claimed CAPM estimate |
| PV explicit FCF / PV terminal | 68.2 / 145.9 | 35.2 / 69.0 | Terminal contributes ~68% / ~66% of EV |

The 25% premium, mix, fees, WACC, margins and cross-sell estimates are **not company guidance**. Escalade's indicative $18.89 share quote and FitLife's $77.62m common cap are secondary data and should be checked against a licensed closing-price feed before submission. [Escalade quote](https://stockanalysis.com/stocks/esca/history/), [FitLife quote](https://robinhood.com/us/en/stocks/FTLF/).

## A4. Sensitivity and bid discipline

At Escalade's 11% WACC, enterprise value ranges from about $197.5m to $235.2m as terminal growth rises from 1.5% to 3.5%. At 9% WACC and 3.5% terminal growth, the highest corner modeled is $321.3m, still just below the $323.5m offer EV. At FitLife's 12% WACC, EV ranges $97.1m to $113.1m; at 10% and 3.5%, the high corner is $148.6m. These are coupled WACC/g sensitivities **holding FCF unchanged**; they are not probability-weighted confidence intervals.

An illustrative standalone equity ceiling is EV - target debt + target cash: **$215.6m ($15.66 per Escalade share)** and **$67.2m for FitLife common equity**. Both are below the indicative market equity capitalization. This signals that a control deal needs substantiated, risk-adjusted net synergies. It does not mean either public company would sell at the DCF ceiling.

## A5. Deal sources and uses, liquidity and dilution

| USD millions | Escalade, 60% stock | FitLife, 50% stock |
|---|---:|---:|
| Equity offer to target holders | 325.051 | 97.025 |
| UA shares issued as consideration | 195.031 | 48.513 |
| Cash to holders | 130.021 | 48.513 |
| Target debt retired | 14.881 | 38.100 |
| Assumed fees | 6.000 | 4.000 |
| Target cash acquired | 16.392 | 1.089 |
| UA starting June cash | 395.981 | 395.981 |
| Closing cash | **261.471** | **306.458** |

This bridge ignores post-close operating cash, seasonal working capital, closing adjustments, purchase accounting, financing fees, dilution from option awards, change-of-control covenants and costs to integrate. Escalade's 60% stock consideration is approximately 39.97m UA shares at an illustrative $4.88 price, subject to share-class, governance and market-price verification. A 50/50 Escalade mix would leave only about $229m cash, below the team's $250m placeholder. [UA June 10-Q](https://www.sec.gov/Archives/edgar/data/1336917/000133691726000111/ua-20260630.htm), [Escalade June 10-Q](https://www.sec.gov/Archives/edgar/data/33488/000143774926024943/esca20260630_10q.htm), [FitLife June 10-Q](https://www.sec.gov/Archives/edgar/data/1374328/000143774926027478/ftlf20260630_10q.htm).

## A6. Commercial hypothesis and verification plan

**Escalade:** ONIX pickleball and Goalrilla basketball create a play/training context for UA footwear and apparel. Test co-branded activations at matched retailers and UA digital placements; compare incremental UA gross profit per **new UA customer**, not gross reach. Equipment purchase frequency is low, and major retailers may own the customer relationship. Diligence ONIX rights, Goalrilla installation/fulfillment, STIGA licenses, adidas Fitness arrangements, customer concentration (2025 two customers 19% and 11%), and import/tariff exposure. Consider a license or commercial partnership before acquiring unrelated archery and billiards assets.

**FitLife:** Supplements could add repeat purchases to UA direct-to-consumer touchpoints. The existing team case screen estimates $17.49m Year 3 incremental revenue and $3.47m operating contribution under assumed basket, conversion, incrementality and $3m ongoing marketing/operations costs. This is **not demonstrated demand**, and cannot be added to standalone DCF without timing, capital, compliance, cannibalization and execution risk. Run an opt-in pilot with pre/post matched cohorts; require third-party product testing, substantiated health claims and athlete eligibility review. [FDA](https://www.fda.gov/consumers/consumer-updates/fda-101-dietary-supplements), [FTC](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance), [USADA](https://www.usada.org/substances/supplement-connect/).

The alternative use of cash is internal footwear and North American brand renewal, measured against the same risk-adjusted return hurdle. Acquisition should not be justified with customer overlap alone.

## A7. Likely judge questions

1. **Why FitLife specifically?** Smaller and clearly outside apparel, U.S. consumable repeat purchases, public financial audit trail and manageable cash use. But Irwin makes growth look stronger than legacy performance; price and claim risk remain gates.
2. **Why Escalade instead?** More direct sports participation and broader equipment adjacency. Its whole portfolio and high offer price reduce confidence; case eligibility requires organizer interpretation.
3. **Why not Decathlon?** Decathlon's scale and broad sporting-goods retail overlap make it unsuitable for the smaller, different-industry target rule. Its U.S. footprint alone is not the deciding criterion.
4. **Can UA afford Escalade?** The modeled stock-heavy offer leaves $261m cash, just above a team $250m placeholder, but liquidity has not been stress-tested across seasonal quarters. Affordability is different from value creation.
5. **Does reported 2026 Escalade profit justify the premium?** No. Remove the $9.875m tariff recovery from the LTM operating baseline; do not annualize it.
6. **Where do synergies come from and who owns the customers?** Test incremental purchases by newly acquired UA customers, channel by channel. Retailer-owned relationships and equipment purchase cadence weaken the presumed cross-sell.
7. **What would change the recommendation?** Organizer eligibility ruling, verified transaction price, audited organic cohort sales, signed channel rights, SKU-level margin/cannibalization data, seasonal liquidity test and a risk-adjusted synergy NPV exceeding the DCF gap plus integration costs.

## A8. Limitations and source audit

The workbook provides an auditable unlevered DCF and sensitivity, not a full purchase price allocation, GAAP merger pro forma, debt covenant analysis or three-statement forecast. The target filing calendars differ from UA's March fiscal year; LTM amounts are screening periods. Escalade's ownership/licensing mix and FitLife's product claims need contract and legal diligence. The source URL for every filed workbook input appears alongside that input in the **Sources** tab. See [research source register](../research/source_register.md) for rejected alternatives and rule interpretation.
