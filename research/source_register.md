# Sources, alternatives, and evidence rules

**Cut-off:** October 22, 2026 for case facts. Filing periods and release dates are listed separately. A quoted stock price is a time-sensitive input; recheck before presenting. `F` means directly reported, `D` derived arithmetic, and `A` a team assumption.

## Primary evidence

| ID | Source and date | Figures used | Limitation |
|---|---|---|---|
| UA-10K | [Under Armour FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1336917/000133691726000073/ua-20260331.htm), filed 2026 | Revenue $4,966.4m, operating loss $163.1m, DTC $2,054.1m; regional sales; history and governance | March 31 balance is superseded by later June quarter |
| UA-Q1 | [UA June 30, 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1336917/000133691726000111/ua-20260630.htm), Aug 2026 | Cash $396.0m, debt $591.2m; 2026 notes paid with previously restricted investments; operating cash $109.1m for quarter | Seasonal working capital and lease liabilities matter |
| FTLF-10K | [FitLife 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1374328/000143774926010680/ftlf20251231_10k.htm), Mar 2026 | Revenue $81.458m, operating income $10.062m; 95% US sales, business and risk disclosures | Irwin Naturals contributed only from Aug 2025 |
| FTLF-Q2 | [FitLife June 30, 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1374328/000143774926027478/ftlf20260630_10q.htm), Aug 13, 2026 | H1 revenue $51.874m and operating income $6.416m vs $32.063m and $5.476m; cash $1.089m; debt $38.1m; 9.391m common shares outstanding | Intangibles $51.0m and goodwill $19.3m complicate purchase accounting |
| FTLF-ER | [FitLife Q2 earnings release](https://www.sec.gov/Archives/edgar/data/1374328/000143774926027493/ex_1004382.htm), Aug 13, 2026 | Q2 revenue $26.549m, gross margin 37.0%, Legacy FitLife down 23%, Irwin $14.135m, adjusted EBITDA $3.7m | Consolidated growth primarily from acquired Irwin; adjusted EBITDA is non-GAAP |
| XPOF-Q2 | [Xponential Q2 release](https://investor.xponential.com/news/detail/174/xponential-fitness-inc-announces-second-quarter-2026), Aug 6, 2026 | Revenue $66m, down 13%; net debt burden: $522.4m debt vs $25m cash; 2026 revenue guidance $250–260m | Franchisee control and debt make acquisition risky |
| LSF-Q2 | [Laird Superfood Q2 release](https://investors.lairdsuperfood.com/news/news-details/2026/Laird-Superfood-Reports-Second-Quarter-2026-Financial-Results/default.aspx), Aug 13, 2026 | Revenue $41.3m, up 244%, net loss $1.8m, gross margin 30.3% | Growth heavily acquisition-driven; stock capitalization misses preferred |
| LSF-Q | [Laird June 30 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1650696/000143774926027697/lsf20260630_10q.htm), Aug 2026 | Series A preferred mezzanine equity about $110.2m | Common market cap alone is a misleading purchase-price proxy |
| GPRO-DEAL | [GoPro definitive merger announcement](https://investor.gopro.com/press-releases/press-release-details/2026/GOPRO-ENTERS-INTO-DEFINITIVE-AGREEMENT-TO-MERGE-WITH-STARMAN-OPTICAL-INC-/default.aspx), Sep 2026 | Existing Starman transaction | Another buyer has a definitive agreement; not a clean available target |
| FDA/FTC | [FDA supplement overview](https://www.fda.gov/consumers/consumer-updates/fda-101-dietary-supplements); [FTC health products guidance](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance); [USADA supplement advice](https://www.usada.org/substances/supplement-connect/) | Product safety, evidence for health claims, anti-doping controls | Legal review needed before using UA athlete endorsements or marketing to minors |

The October 22 price anchors in `inputs.json` are **indicative secondary quotes**: [FTLF quote/history](https://robinhood.com/us/en/stocks/FTLF/) shows about $8.25 and $77.62m equity capitalization; [UAA history](https://finance.yahoo.com/quote/UAA/history/) supports a roughly $4.88 quote. Verify exact closing prices and classes of UA stock before the final deck. The deal price, mix, fees, and all cross-sell conversions are assumptions, not filed company guidance.

## Candidate screen

| Candidate | Different industry and smaller? | Customer access | Financial/transaction concern | Decision |
|---|---|---|---|---|
| **FitLife Brands** (nutritional supplements) | Yes: roughly $78m common equity vs UA about $2b | Repeat purchases, US nutrition retail and online brands; potential sportswear customer overlap | Legacy brands down 23% in Q2, cash only $1.1m, $38.1m debt, health-claim risk | **Work up, conditional** |
| Xponential Fitness (boutique studio franchising) | Yes by equity capitalization | Physical community and frequent studio visits | $522.4m debt, falling revenue and same-store sales; franchisees are independent | Reject whole-company acquisition on leverage/consent grounds; commercial pilot might still make sense |
| Laird Superfood (functional food and beverage) | Yes by common equity, but that omits securities | Stronger grocery channel, food repeat purchases | About $110m preferred mezzanine claim; low 30.3% gross margin; recently acquired brands drive growth | Reject simplistic low-price thesis; complex capitalization and integration |
| GoPro (consumer electronics) | Yes by equity size | Large action-sport audience and content | Already signed a definitive deal with Starman in Sep 2026; sales declining | Exclude as unavailable on ordinary deal terms |

**Selection logic:** FitLife is a hypothesis worth testing because it offers repeat purchases and a purchase price proportionate to UA's liquidity, with public financials to audit. It is not an established turnaround. The strongest rival strategy is *no acquisition*: fund footwear and North American brand renewal internally. Apply the same hurdle rate and customer-acquisition evidence to both.

## Calculations and gaps

- FitLife LTM revenue to June 2026: `81.458 + 51.874 - 32.063 = $101.269m` [D]. LTM operating income: `10.062 + 6.416 - 5.476 = $11.002m` [D].
- FitLife Q2 consolidated 65% growth is **not organic**. Legacy group declined 23% and the acquired Irwin group generated $14.135m Q2 [F]. Diligence must isolate organic cohorts by SKU and channel.
- UA FY2026 and FitLife June LTM are different ending dates. The simple $5,067.669m combined revenue is a screening bridge, **not** a SEC Article 11 pro forma or a claim that acquisition restored UA organic growth.
- Exact store conversion, basket size, order frequency, overlap, athlete-safe product certification, retention, target's change-of-control provisions, and purchase price are **not public facts in this project**. Do not turn assumptions into market research.
- Avoid adding sportswear and supplement market-size estimates: there is customer overlap, and a large TAM does not demonstrate feasible sales for this buyer. The model uses reachable UA store and DTC touchpoints instead.
