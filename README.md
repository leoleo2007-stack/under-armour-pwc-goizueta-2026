# Under Armour M&A case | PwC x Goizueta 2026

A source-traceable research project for the October 2026 case competition. **Working recommendation:** investigate FitLife Brands (NASDAQ: FTLF) as a smaller, different-industry target, while screening Escalade (NASDAQ: ESCA) as the stronger sports-product challenger. Do not bid at the illustrative 25% premium without verified net synergies that cover the standalone DCF gap and integration costs. This is a team working draft, not a claim that either company has agreed to a transaction.

## Start here

1. Read [the case brief](case/brief.md) and the [recommendation](research/recommendation.md).
2. Check the [source register and alternatives](research/source_register.md), including the [Escalade challenger screen](research/escalade_screen.md). Every sourced number has a filing or release link; every invented scenario input is labeled **assumption**.
3. Open the [editable five-year valuation workbook](outputs/target_valuation.xlsx), [four-page presentation appendix](outputs/diligence_appendix.pdf), [full diligence appendix](presentation/appendix.md), and [visual figures](presentation/figures/). The workbook has source citations, DCF forecasts and WACC/terminal-growth sensitivities for both targets. Run `python3 model/valuation.py` for an independent calculation check; the source builder is `model/build_valuation.mjs`.
4. Run `python3 model/case_model.py --scenarios` for the original FitLife commercial pilot, deal bridge and adoption sensitivity; edit `data/inputs.json` to change those assumptions.
5. Use the [15-slide copy](presentation/slide_copy.md), [storyboard](presentation/slide_story.md), and [presenter notes](presentation/talk_track.md) for the two PDF submissions. The [downloaded project skills](skills/README.md) cover DCF, comps, competitive diligence and deck checking. The team still needs to validate the thesis and design the final deck.

## Central conclusion

The acquisition could add a recurring purchase category, but FitLife's legacy business fell 23% year over year in Q2 2026. The standalone DCF estimates $104.3m enterprise value against a $134.0m illustrative offer, a $29.8m gap before fees and integration. Escalade has a clearer sports participation story, but its $214.1m standalone DCF is $109.4m below its illustrative offer and its case eligibility is uncertain. Prove genuinely incremental customers, risk-adjusted synergies and a financeable price before recommending a binding offer.

## Important timing and sharing

- Case cut-off: facts as of October 22, 2026. The equity-value input uses an indicative October 22 quote; verify the exact official closing price and share count before submitting.
- Deck due Wednesday, October 28 at 5:00 p.m. Eastern. The packet calls for two PDFs, one anonymous and one with a meet-the-team slide. The 15-slide main limit includes title but excludes appendix and meet-the-team.
- The organizer's training PDF and case document are linked in the brief, not committed here. The repository contains the team's working analysis and assumptions.
- The competition allows AI but discourages it for ideation. Treat the target selection as a research hypothesis for your team to challenge and own.

## What the model does and does not do

It computes two editable, standalone five-year DCFs, WACC/g sensitivities, a sources-and-uses sketch, a historical income-statement combination and an illustrative Year 3 FitLife cross-sell bridge. It is **not** a purchase-price allocation, audited pro forma, fairness opinion or five-year balance-sheet forecast. WACC, forecasts, premiums and commercial conversions are team assumptions, not management guidance. An acquisition would require creditor and change-of-control review, tax and regulatory diligence, and an executable price based on negotiations.
