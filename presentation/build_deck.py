"""Build the 15-slide anonymous case deck PDF from reviewable slide content."""

from pathlib import Path
import json
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader, simpleSplit

ROOT=Path(__file__).resolve().parents[1]
TEAM='--team' in sys.argv
OUT=ROOT/'outputs'/('team_case_deck.pdf' if TEAM else 'anonymous_case_deck.pdf')
W,H=960,540
NAVY=HexColor('#142A40');TEAL=HexColor('#007C83');ORANGE=HexColor('#C57432')
PALE=HexColor('#E9F2F2');GRAY=HexColor('#536375');SOFT=HexColor('#F3F6F8')
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('Under Armour and FitLife | anonymous case draft')

def txt(x,y,text,size=16,color=NAVY,bold=False):
    c.setFont('Helvetica-Bold' if bold else 'Helvetica',size);c.setFillColor(color);c.drawString(x,y,str(text))

def lines(x,y,text,width,size=16,leading=None,color=NAVY,bold=False):
    leading=leading or size*1.4
    for line in simpleSplit(str(text),'Helvetica-Bold' if bold else 'Helvetica',size,width):
        txt(x,y,line,size,color,bold);y-=leading
    return y

def base(n,title,source='Case packet; filings and team assumptions in appendix'):
    c.setFillColor(white);c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(NAVY);c.rect(0,H-9,W,9,fill=1,stroke=0)
    txt(40,493,title,27,NAVY,True)
    c.setStrokeColor(TEAL);c.setLineWidth(2);c.line(40,477,920,477)
    txt(40,28,source,9,GRAY)
    txt(903,28,f'{n:02d}',10,TEAL,True)

def end():c.showPage()

def card(x,y,w,h,headline,value,detail='',accent=TEAL):
    c.setFillColor(SOFT);c.roundRect(x,y,w,h,12,fill=1,stroke=0)
    c.setFillColor(accent);c.rect(x,y+h-7,w,7,fill=1,stroke=0)
    txt(x+20,y+h-36,headline,14,GRAY,True)
    txt(x+20,y+h-89,value,36,accent,True)
    lines(x+20,y+25,detail,w-40,12,16,GRAY)

def box(x,y,w,h,title,body,accent=TEAL):
    c.setFillColor(SOFT);c.roundRect(x,y,w,h,10,fill=1,stroke=0)
    txt(x+18,y+h-34,title,18,accent,True)
    lines(x+18,y+h-64,body,w-36,14,20)

def table(x,y,widths,headers,rows,row_h=51):
    total=sum(widths);c.setFillColor(NAVY);c.roundRect(x,y-row_h,total,row_h,5,fill=1,stroke=0)
    xx=x
    for w,h in zip(widths,headers):
        lines(xx+10,y-22,h,w-20,13,16,white,True);xx+=w
    y-=row_h
    for i,row in enumerate(rows):
        c.setFillColor(PALE if i%2 else SOFT);c.rect(x,y-row_h,total,row_h,fill=1,stroke=0)
        xx=x
        for w,val in zip(widths,row):
            lines(xx+10,y-22,str(val),w-20,13,16,NAVY);xx+=w
        y-=row_h
    return y

# 1 title
c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0)
c.setFillColor(TEAL);c.rect(0,0,20,H,fill=1,stroke=0)
txt(68,394,'UNDER ARMOUR + FITLIFE',36,white,True)
txt(68,332,'A disciplined acquisition option',27,white)
txt(68,277,'Recurring customers require proof of demand and price',20,HexColor('#CDE8E7'))
txt(68,73,'PwC x Goizueta 2026 | Anonymous case draft | October 2026',13,white)
txt(903,28,'01',10,white,True);end()

# 2 recommendation
base(2,'Investigate FitLife; do not approve the modeled offer today','FitLife June 2026 10-Q; team DCF and illustrative 25% premium')
card(42,239,275,194,'Offer EV','$134m','Illustrative 25% premium',ORANGE)
card(342,239,275,194,'Standalone DCF EV','$104m','Assumption-driven five-year DCF')
card(642,239,275,194,'Value gap','$30m','Net synergies must exceed this plus costs',ORANGE)
lines(52,190,'Board action: authorize diligence and a matched-market pilot. Set a bid ceiling only after verifying organic sales, product safety and risk-adjusted synergies.',855,18,27,NAVY,True);end()

# 3 diagnosis
base(3,'UA needs new full-price demand, especially in North America','UA FY2026 10-K; case Exhibits 1-3; April-June 2026 quarter')
card(42,262,205,160,'FY2026 revenue','$4.97b','Down 3.8%')
card(265,262,205,160,'North America','-7.9%','FY2026 sales')
card(488,262,205,160,'Footwear','-10.8%','FY2026 sales')
card(711,262,205,160,'Latest quarter','-3%','April-June revenue')
box(42,74,875,143,'Why a category adjacency?',"UA's improved adjusted operating outlook includes tariff effects. A smaller repeat-purchase category could broaden customer contact, but it cannot repair a $5b core brand by itself.");end()

# 4 candidate screen
base(4,'FitLife meets the industry rule; Escalade is a serious challenger','Source register; candidate filings and releases; as of October 22, 2026')
table(42,430,[175,290,410],['Target','Strategic link','Decision concern'],[
    ['FitLife','Nutrition repeat purchases','Legacy brands -23% in Q2; compliance and price'],
    ['Escalade','ONIX, Goalrilla: play + train + wear','Equipment eligibility uncertain; $109m DCF gap'],
    ['Xponential','Fitness studios and community','$522m debt; franchisee control'],
    ['Laird / GoPro','Food / action sports audience','Preferred claim / signed other merger']
],row_h=66)
lines(50,86,'FitLife is the primary case target; Escalade deserves diligence if organizers confirm eligibility.',850,17,24,NAVY,True);end()

# 5 target
base(5,'FitLife brings a $101m nutrition business; size alone is not the thesis','FitLife FY2025 10-K and June 2026 10-Q; LTM derived')
card(42,250,275,180,'FY2025 revenue','$81.5m','Filed')
card(342,250,275,180,'June 2026 LTM','$101.3m','2025 + H1 2026 - H1 2025')
card(642,250,275,180,'LTM operating','$11.0m','GAAP; acquisition-affected')
box(42,69,875,147,'Why own it?',"Consumer nutrition has repeat purchase potential beside UA training products. Keep the existing FitLife retail and Amazon channels intact while testing new-to-UA purchases in selected stores and ecommerce.");end()

# 6 diligence problem
base(6,'Headline growth hides an acquired business and weak legacy demand','FitLife Q2 2026 earnings release; June 2026 10-Q')
card(42,239,275,194,'Q2 legacy sales','-23%','Year over year',ORANGE)
card(342,239,275,194,'Irwin Q2 sales','$14.1m','Brand group acquired in 2025')
card(642,239,275,194,'H1 consolidated','$51.9m','Versus $32.1m in H1 2025')
lines(52,190,'Require brand-level organic revenue, SKU retention and customer cohorts. Do not describe consolidated acquisition-driven growth as consumer validation.',850,18,27,NAVY,True);end()

# 7 pilot
base(7,'A controlled pilot tests true new customers and incremental profit','Pilot design is a team proposal, not company guidance')
box(42,265,270,153,'1. Test','20 UA stores plus opt-in digital placements; adult products pass independent testing and claims review.')
box(345,265,270,153,'2. Control','Use matched stores or markets; keep existing FitLife channel revenue visible.')
box(648,265,270,153,'3. Decide','Measure new-to-UA buyers, 90/180-day repeat purchase and combined gross profit after spend.')
lines(52,174,'A customer already buying FitLife on Amazon who switches checkout to UA is not a new combined customer.',850,18,28,NAVY,True);end()

# 8 revenue bridge
base(8,'Year 3 base case: $17.49m net-new sales is an assumption','UA FY2026 10-K DTC/stores; transaction, AOV, attach and overlap assumptions')
card(42,259,270,170,'Store sales','$17.28m','443 x 25 weekly x $30 x 52')
card(345,259,270,170,'Online proxy','$7.70m','DTC / $80 x 1% x $30')
card(648,259,270,170,'After overlap','$17.49m','70% of $24.98m')
box(42,69,875,151,'Reach caveat','UA DTC includes physical stores, so applying its full revenue as an ecommerce order base is generous. Website-only orders, cannibalization and actual conversion need measurement.',ORANGE);end()

# 9 adoption cases
base(9,'The pilot can lose money in the downside adoption case','Team commercial assumptions; model/case_model.py')
table(42,424,[190,160,150,175,200],['Case','Store txns/wk','Online attach','Net-new sales','Operating result'],[
    ['Downside','10','0.5%','$5.38m','($2.39m)'],
    ['Base','25','1.0%','$17.49m','$3.47m'],
    ['Upside','40','1.5%','$33.32m','$9.33m']
],row_h=68)
lines(52,120,'Contribution uses different margin and marketing costs by case. None of these cases is an observed FitLife or UA forecast.',850,17,24,NAVY,True);end()

# 10 funding
base(10,'The 50/50 illustration leaves $306m UA cash at close','UA and FitLife June 2026 10-Qs; price, stock mix and fees are team assumptions')
table(42,424,[248,155,160,155,157],['UA cash','Target cash','Cash to sellers','Debt retired + fees','Closing cash'],[
    ['$395.98m','+$1.09m','-$48.51m','-$42.10m','$306.46m']
],row_h=98)
card(42,88,420,190,'Stock issued','$48.5m','~9.9m illustrative UA Class C shares at $4.88')
card(495,88,422,190,'UA debt after close','$591.2m','Target debt assumed retired; seasonal cash untested');end()

# 11 historical bridge
base(11,'Acquired revenue is only about 2% of UA sales','UA FY2026 10-K; FitLife FY2025 10-K and June 2026 10-Q')
table(42,428,[230,210,210,225],['Metric','UA FY2026','FitLife LTM','Simple sum'],[
    ['Revenue','$4,966.4m','$101.3m','$5,067.7m'],
    ['Operating income','($163.1m)','$11.0m','($152.1m)']
],row_h=75)
box(42,81,875,151,'Interpretation','The periods end at different dates and exclude acquisition accounting, financing and integration. This is screening arithmetic, not a GAAP pro forma or an organic growth claim.');end()

# 12 valuation
base(12,'The 25%-premium offer requires $30m plus costs of net synergy PV','Team DCF; full cash-flow and WACC/g sensitivity in valuation workbook')
c.drawImage(ImageReader(str(ROOT/'presentation/figures/valuation_comparison.png')),48,97,width=624,height=333,mask='auto')
box(690,110,225,307,'Bid discipline','Standalone FitLife DCF EV: $104.3m. Illustrative offer EV: $134.0m. The gap is $29.8m before fees and integration. A lower executable price or proven incremental profit is required.',ORANGE);end()

# 13 risk
base(13,'Product trust and organic sales are hard deal gates','FitLife Q2 release; FDA, FTC and USADA guidance; team proposal')
table(42,428,[245,630],['Risk','Required evidence before an offer'],[
    ['Athlete product safety','Independent certification, contaminant testing and label audit'],
    ['Health claims','Substantiation, compliant adult marketing and counsel review'],
    ['Legacy decline','SKU-level cohort retention and credible stabilization plan'],
    ['Customer cannibalization','Incremental combined profit versus matched controls'],
    ['Liquidity and distraction','Seasonal cash floor, creditor terms and separate P&L']
],row_h=61);end()

# 14 opportunity cost
base(14,"Capital has a competing use in UA's core business",'Cash bridge is modeled; internal program is a counterfactual team assumption')
card(42,242,400,187,'Cash commitment','$90.6m','Cash to sellers + target debt + fees',ORANGE)
card(517,242,400,187,'Internal alternative','UA core','Footwear product and North America customer acquisition')
lines(52,178,'Compare both options on risk-adjusted incremental gross profit and retained new customers. Public data do not establish which has the higher return.',850,18,28,NAVY,True);end()

# 15 board ask
base(15,'Authorize diligence and pilot; require proof before any binding bid','Team recommendation; full sources, scenarios and diligence questions in appendix')
box(42,287,875,142,'Approve now','A 90-day matched-store and opt-in digital experiment; organic SKU diligence; independent product and claims review; debt and seasonal liquidity work.')
box(42,104,875,153,'Offer only if','Risk-adjusted net synergy value exceeds the $29.8m DCF gap plus integration and fees, the target trend can stabilize, safety gates pass, and the deal beats internal UA investment.',ORANGE)
end()

if TEAM:
    path=ROOT/'data'/'team.json'
    if not path.exists():raise SystemExit('Create data/team.json from data/team.example.json before building the team PDF')
    members=json.loads(path.read_text())['members']
    if not members or any(not m.get('name') or not m.get('role') for m in members):
        raise SystemExit('Every team member needs a name and role')
    base(16,'Meet the team','Team-provided names and roles')
    for i,m in enumerate(members[:8]):
        col=i%2;row=i//2;x=42+col*447;y=369-row*90
        box(x,y,410,76,m['name'],m['role'])
    end()

c.save();print(OUT)
