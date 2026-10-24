# Investment thesis and recommendation — team working draft

## Answer first

Recommend a **conditional acquisition of FitLife Brands** at an illustrative enterprise value near **$134m** (October 22 indicative equity capitalization of $77.62m, assumed 25% equity premium, plus $38.1m target debt, less $1.1m cash). Fund half of the roughly $97m equity offer with non-voting UA Class C stock and half with cash; retire FitLife debt and budget $4m deal fees. In the screening bridge, cash after closing is about **$306m** and UA debt remains **$591m**. No acquisition is warranted if diligence fails the organic-demand, product-safety, or price tests below.

This is a **small customer-frequency wedge**, not a $200m instant cure. Use FitLife's MusclePharm and other appropriate products in a *train–fuel–recover* assortment, with selected UA stores and ecommerce as a measured acquisition channel. Keep FitLife's own retail and Amazon channels independent initially. If that test works, expand; if it does not, preserve UA capital for footwear and brand renewal.

## Diagnosis and why this target

- UA FY2026 revenue fell to $4.97b and North America sales fell 7.9%. The packet identifies customer desire at full price as the problem. A cost-only program can improve margins without creating customer demand.
- UA earned $47m of operating income in the April–June 2026 quarter and guided to $140–160m FY2027 **adjusted** operating income, partly aided by tariff refunds. This improvement does not establish a recovery in organic customer demand: quarterly sales still declined 3% and management guided to a mid-single-digit full-year sales decline. Keep GAAP FY2026 and non-GAAP FY2027 measures separate.
- FitLife sells a frequently purchased category outside apparel and has $101.3m LTM revenue and $11.0m LTM operating income to June 2026. Its $78m indicative equity value makes a transaction small relative to UA's roughly $2b capitalization and $396m June cash.
- FitLife's own legacy revenue fell 23% in Q2. Irwin's purchase explains most headline growth. The thesis therefore depends on a verified retention/marketing engine and UA incremental conversion, rather than celebrating a consolidated growth rate.
- UA's old fitness-app acquisitions produced poor exits. This proposal uses physical consumables and revenue per channel with a discrete pilot and a kill condition. That lowers, but does not eliminate, integration and distraction risk.

## Historical bridge and funding (USD millions)

| Item | Value | Type |
|---|---:|---|
| UA FY2026 revenue | 4,966.4 | Filed fact |
| FitLife LTM revenue through June 2026 | 101.3 | Derived from filings |
| Simple combined revenue | 5,067.7 | Derived, periods do not match |
| UA FY2026 operating income | (163.1) | Filed fact |
| FitLife LTM operating income | 11.0 | Derived |
| Simple combined operating income | (152.1) | Excludes deal amortization, interest changes, and synergies |
| Indicative offer for FitLife equity | 97.0 | Assumed 25% premium to an indicative Oct 22 quote |
| UA stock issued / cash to target shareholders | 48.5 / 48.5 | Assumed 50/50 split |
| Repay target debt / deal fees | 38.1 / 4.0 | Filed target debt / assumed fees |
| Pro forma cash / debt immediately after close | 306.4 / 591.2 | Simplified balance bridge; no working-capital or PPA changes |

At an assumed UA Class C price of $4.88, stock consideration implies about **9.9m** new non-voting shares, around **2.3%** of roughly 429.5m UA A/B/C shares outstanding at June 30. Verify legal issuance terms, weighted-average EPS, and Plank's voting control. It would be misleading to show EPS accretion from UA's current GAAP loss or to assert GAAP pro forma balance-sheet goodwill without a valuation allocation.

## How customer growth is actually tested

**A launch design, not a forecast:** In a sample of 20 UA stores and UA ecommerce, offer two or three independently tested, adult-oriented products in adjacent training contexts. Keep the acquired brands' labeling intact. Randomize comparable stores or markets between pilot and control, and compare *incremental combined gross profit after acquisition/marketing costs*, not just supplement units sold. Use a 90-day test; repeat at six months to check retention.

The Year 3 base-case mechanism is deliberately auditable:

| Driver | Assumption | Formula / result |
|---|---:|---:|
| Stores | 443 stores × 25 incremental transactions/week × $30 × 52 weeks | $17.28m gross cross-sell |
| Ecommerce | $2,054.1m UA DTC sales ÷ assumed $80 AOV × 1% attach × $30 | $7.70m gross cross-sell |
| Net-new share after existing FitLife customer overlap and displaced channels | 70% | **$17.49m** net-new sales |
| Gross margin less incremental marketing/operations | 37% × net-new sales − $3m | **$3.47m** operating contribution |

Those assumptions are **not observed conversion data**. An $80 AOV is a proxy, and UA DTC revenue includes physical stores, so this uses the entire DTC revenue as a generous ecommerce order base. The model likely overstates online reach; split website and store revenue in diligence. It also assumes FitLife's 37% Q2 gross margin transfers to the new mix; merchandising and retailer margin could lower it. The operating benefit could be negative in a downside scenario.

| Year 3 case | Store transactions/week | Online attach | Truly net-new share | Net-new revenue | Operating contribution |
|---|---:|---:|---:|---:|---:|
| Downside | 10 | 0.5% | 50% | $5.38m | **($2.39m)** |
| Base | 25 | 1.0% | 70% | $17.49m | **$3.47m** |
| Upside | 40 | 1.5% | 85% | $33.32m | **$9.33m** |

The downside also assumes 30% incremental margin and $4m launch expense; base assumes 37% and $3m; upside assumes 40% and $4m. None are company forecasts. Run `python3 model/case_model.py --scenarios` to reproduce.

**Customer metrics:** new-to-UA purchasers, repeat nutrition orders at 90/180 days, incremental UA apparel/footwear units versus controls, blended gross profit per acquired customer, return/refund rate, and adverse product events. A successful launch should not count an existing FitLife buyer switching from Amazon to UA as a new customer.

## Risk, ethics, and disconfirming evidence

| Risk | Evidence or mechanism | Mitigation / deal gate |
|---|---|---|
| FitLife legacy decline | Q2 legacy revenue down 23% year over year, including retailer concentration | Require SKU/cohort analysis and a credible stabilization plan; lower price or walk if decline persists after channel normalization |
| Liquidity and valuation | Cash purchase plus debt retirement consumes roughly $91m before working-capital needs | Preserve >$250m UA cash in base financing, negotiate stock/earnout, review debt covenants and share authorization |
| Reputation and athlete safety | Supplements do not receive premarket FDA approval of safety/effectiveness; claims require substantiation and contamination can affect tested athletes | Independent quality review, substantiated claims, third-party certification appropriate for athletes, no medical claims or youth-targeted performance products |
| Customer cannibalization | Existing FitLife buyers might merely change checkout channels; UA product budget might shift | Measure incremental combined contribution with randomized market test and customer identity controls |
| Integration and management distraction | UA's past app acquisitions and current restructuring | Separate product P&L, retain target operating specialists, quarterly board stage gates |

**Hard no-deal conditions:** (1) credible organic declines remain around 20% annually with no unit-economic recovery; (2) safety/label or anti-doping audit fails; (3) negotiated enterprise value exceeds a price justified by independently modeled cash flows; (4) base financing pushes UA below a board-approved seasonal cash floor. The $250m floor above is a **team placeholder**, not UA guidance.

## Implementation and opportunity cost

1. **Before LOI (0–30 days):** UA CFO and strategy team reconcile share count, target net debt, target SKU/brand organic sales, customer overlaps, debt change-of-control, and capital constraints. Ask independent regulatory advisers to inspect claims and testing.
2. **Post signing/closing (months 1–3):** Maintain separate channel operations; select 20 matched UA stores and control stores; instrument product-level sales and consent-based customer cohorts.
3. **Decision gate (months 4–6):** Expand only if incremental contribution is positive and repeat purchase meets a board-set hurdle. Stop unproductive assortments.
4. **Scale (months 7–24):** Roll out proven products to selected UA locations and ecommerce; evaluate wholesale retailer buy-in separately. Protect athlete trust with product testing and clear disclosure.

**Best alternative:** Spend the same roughly $90m cash commitment on footwear product work, North American athlete/community marketing, and DTC execution. The acquisition wins only if the repeat-category customer relationship and incremental profit clear a higher return than that internal program. The current public data do **not** prove that hurdle; the team should describe the proposed pilot and diligence as the evidence-generating step.

## Tough Q&A

**Does $101m in acquired sales fix a $5b brand?** No. It adds only about 2% to reported top line. The thesis is buying a repeat category and measuring whether new customers and retention can grow over time.

**Is FitLife growing 65% organically?** No. Q2 headline growth came mainly from acquired Irwin. Legacy FitLife revenue declined 23%.

**Why not Xponential?** Its studios offer customer touchpoints, but $522.4m debt and weaker same-store sales raise financing and execution risk; franchises are not wholly controlled UA stores.

**What happened to UA's $600m current debt?** It was discharged with restricted investments and settled June 15, 2026. Do not subtract it again from June unrestricted cash.

**Why does the model still show an operating loss?** Historical combination mechanically adds one profitable target to UA's prior loss. It omits purchase accounting and is not a full forecast; it reveals how small the target is relative to UA's core problem.
