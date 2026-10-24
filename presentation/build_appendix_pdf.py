"""Concise presentation-ready PDF companion to the detailed Markdown appendix."""

from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs' / 'diligence_appendix.pdf'
OUT.parent.mkdir(exist_ok=True)
NAVY=colors.HexColor('#142A40'); TEAL=colors.HexColor('#007C83')
LIGHT=colors.HexColor('#E9F2F2'); GRAY=colors.HexColor('#526173')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleUA',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=20,leading=24,textColor=NAVY,spaceAfter=10,alignment=TA_LEFT))
styles.add(ParagraphStyle(name='HUA',parent=styles['Heading2'],fontName='Helvetica-Bold',fontSize=12,leading=16,textColor=TEAL,spaceBefore=12,spaceAfter=6))
styles.add(ParagraphStyle(name='BodyUA',parent=styles['BodyText'],fontName='Helvetica',fontSize=9,leading=13,spaceAfter=7))
styles.add(ParagraphStyle(name='SmallUA',parent=styles['BodyText'],fontName='Helvetica',fontSize=7.3,leading=10,textColor=GRAY,spaceAfter=6))
P=lambda t,style='BodyUA':Paragraph(t,styles[style])

def table(data,widths):
    t=Table([[P(str(c),'SmallUA') for c in row] for row in data],colWidths=widths,hAlign='LEFT',repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),NAVY),('TEXTCOLOR',(0,0),(-1,0),colors.white),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),
        ('BOTTOMPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,-1),(-1,-1),.6,TEAL)
    ]))
    # Paragraph text is colored by its style; use a white style on headers.
    return t

styles.add(ParagraphStyle(name='HeadCell',parent=styles['SmallUA'],textColor=colors.white,fontName='Helvetica-Bold'))
def tbl(data,widths):
    t=Table([[P(str(c),'HeadCell' if i==0 else 'SmallUA') for c in row] for i,row in enumerate(data)],colWidths=widths,hAlign='LEFT',repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,-1),(-1,-1),.6,TEAL)]))
    return t

story=[]
story += [P('Under Armour | target valuation appendix','TitleUA'),P('PwC x Goizueta 2026 case | October 22, 2026 information cut-off | USD millions','SmallUA')]
story += [P('A1. Decision in one view','HUA'),P('FitLife meets the different-industry test more clearly; Escalade offers a more direct sports-participation story but needs an organizer eligibility ruling. Neither modeled 25%-premium offer clears standalone DCF. The gaps are synergy value hurdles, not booked cash losses.')]
story += [tbl([['Measure','Escalade','FitLife'],['LTM June 2026 revenue','243.8','101.3'],['Operating income used','20.3, tariff normalized','11.0 GAAP'],['Standalone DCF EV','214.1','104.3'],['Illustrative offer EV','323.5','134.0'],['DCF EV less offer EV','(109.4)','(29.8)'],['Closing UA cash at modeled mix','261.5','306.5']],[2.55*inch,2.25*inch,2.25*inch]),Spacer(1,10)]
story += [Image(str(ROOT/'presentation/figures/valuation_comparison.png'),width=6.9*inch,height=3.68*inch)]
story += [P('Source: Escalade and FitLife FY2025 10-Ks and June 2026 10-Qs; indicative October 22 secondary quotes. Standalone DCF assumptions in the live workbook. 25% offer premium and cash/stock mix are team scenarios.','SmallUA')]
story += [PageBreak(),P('A2. Five-year unlevered cash flow','TitleUA')]
story += [P('FCF = EBIT - cash tax + D&amp;A - capex - incremental working capital. Each rolling year follows the June 2026 LTM. Terminal value uses Year 5 FCF x (1 + g)/(WACC - g), discounted five years. No operating synergies are included.')]
story += [tbl([['Driver','Escalade','FitLife'],['Revenue growth, Y1-Y5','2%, 3%, 3%, 3%, 2%','3%, 5%, 5%, 4%, 3%'],['EBIT margin, Y1 / Y5','8.35% / 9%','11% / 12%'],['Cash tax / D&amp;A / capex','25% / 2.1% / 1.2%','25% / 1% / 0.5%'],['NWC investment / new sales','15%','12%'],['WACC / terminal g','11% / 2.5%','12% / 2.5%'],['PV explicit / PV terminal','68.2 / 145.9','35.2 / 69.0']],[2.55*inch,2.25*inch,2.25*inch]),Spacer(1,13)]
story += [Image(str(ROOT/'presentation/figures/fcf_forecasts.png'),width=6.9*inch,height=3.68*inch)]
story += [P('Growth, margin, tax, reinvestment, WACC and terminal growth are team assumptions rather than company guidance. Escalade LTM EBIT removes a $9.875m tariff recovery. FitLife reported growth includes the 2025 Irwin acquisition.','SmallUA')]
story += [PageBreak(),P('A3. Sensitivity and capital','TitleUA')]
story += [Image(str(ROOT/'presentation/figures/dcf_sensitivity.png'),width=7.0*inch,height=3.08*inch),Spacer(1,10)]
story += [P('At the base WACC, Escalade EV ranges $197.5m-$235.2m across 1.5%-3.5% terminal growth; FitLife ranges $97.1m-$113.1m. The high WACC/g corners are not confidence intervals. Terminal value is about 68% and 66% of their base EVs.')]
story += [tbl([['Sources and uses','Escalade','FitLife'],['Equity offer / cash to sellers','325.1 / 130.0','97.0 / 48.5'],['UA stock to sellers','195.0','48.5'],['Target debt retired / assumed fees','14.9 / 6.0','38.1 / 4.0'],['Target cash acquired','16.4','1.1'],['UA June cash / closing cash','396.0 / 261.5','396.0 / 306.5']],[2.55*inch,2.25*inch,2.25*inch])]
story += [P('A $250m minimum cash balance is a team placeholder, not UA guidance. The bridge omits seasonal cash, closing adjustments, purchase accounting and financing costs. Escalade 60% stock mix implies ~40m illustrative new UA shares at a $4.88 secondary quote.','SmallUA')]
story += [PageBreak(),P('A4. Diligence and judge questions','TitleUA')]
story += [P('<b>Escalade:</b> Verify whether equipment qualifies under the case rule; distinguish owned brands from STIGA and other licensed rights, review the adidas Fitness arrangement, retailer control of customer data, two-customer concentration, Gold Tip effects and tariff/import risk.')]
story += [P('<b>FitLife:</b> Reconcile the 23% Q2 legacy revenue decline with Irwin-driven consolidated growth. Require SKU/cohort retention, product certification, substantiated claims, athlete-safe testing, debt terms and true new-to-UA customer measurement.')]
story += [P('<b>Commercial experiment:</b> Pilot matched stores and opt-in digital cohorts; track new-to-UA purchasers, repeat purchases, cannibalization and incremental combined gross profit. The prior Year 3 FitLife case of $17.49m new sales and $3.47m operating contribution is an assumption, not observed demand.')]
story += [P('<b>What changes the recommendation?</b> An organizer eligibility ruling, verified market quote and capitalization, organic growth evidence, contract rights, a seasonal cash plan, and risk-adjusted synergy NPV above the value gap plus integration costs. Compare acquisition against internal UA footwear and North America investment.')]
story += [P('Primary filing links','HUA')]
links=[('UA June 2026 10-Q','https://www.sec.gov/Archives/edgar/data/1336917/000133691726000111/ua-20260630.htm'),('Escalade 2025 10-K','https://www.sec.gov/Archives/edgar/data/33488/000143774926006094/esca20251231_10k.htm'),('Escalade June 2026 10-Q','https://www.sec.gov/Archives/edgar/data/33488/000143774926024943/esca20260630_10q.htm'),('FitLife 2025 10-K','https://www.sec.gov/Archives/edgar/data/1374328/000143774926010680/ftlf20251231_10k.htm'),('FitLife June 2026 10-Q','https://www.sec.gov/Archives/edgar/data/1374328/000143774926027478/ftlf20260630_10q.htm')]
for label,url in links:story.append(P(f'<link href="{url}" color="#007C83">{label}</link>','SmallUA'))
story += [Spacer(1,8),P('The full appendix.md and target_valuation.xlsx contain the operating bridge, source URLs beside workbook inputs, formula sensitivities and further Q&amp;A. This PDF is a presentation companion, not a fairness opinion or audited merger pro forma.','SmallUA')]

def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(TEAL);canvas.line(42,42,570,42)
    canvas.setFont('Helvetica',8);canvas.setFillColor(GRAY)
    canvas.drawString(42,29,'Under Armour case | team working analysis');canvas.drawRightString(570,29,str(doc.page))
    canvas.restoreState()

doc=SimpleDocTemplate(str(OUT),pagesize=(612,792),leftMargin=43,rightMargin=43,topMargin=42,bottomMargin=58,
                      title='Under Armour target valuation appendix')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
