import fs from 'node:fs/promises';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const outputDir = new URL('../outputs/', import.meta.url).pathname;
const wb = Workbook.create();
for (const name of ['Decision', 'Escalade DCF', 'FitLife DCF', 'Sources']) wb.worksheets.add(name);
const dec = wb.worksheets.getItem('Decision');
const src = wb.worksheets.getItem('Sources');
const esc = wb.worksheets.getItem('Escalade DCF');
const fit = wb.worksheets.getItem('FitLife DCF');
const navy = '#142A40', teal = '#007C83', pale = '#E9F2F2';
const num = '#,##0.0;(#,##0.0);–', pct = '0.0%;(0.0%);–';
const put = (s,c,v) => s.getRange(c).values = [[v]];
const formula = (s,c,v) => s.getRange(c).formulas = [[v]];
const bar = (s,r,label,last='H') => {
  put(s,`A${r}`,label);
  s.getRange(`A${r}:${last}${r}`).format = {fill:navy,font:{name:'Aptos',bold:true,color:'#FFFFFF',size:11}};
  s.getRange(`A${r}:${last}${r}`).format.rowHeight=25;
};
for (const s of [dec,esc,fit,src]) {
  s.showGridLines=false;
  s.getRange('A1:L45').format.font={name:'Aptos',size:10,color:'#26394D'};
  s.getRange('A:A').format.columnWidth=38;
  s.getRange('B:B').format.columnWidth=17;
  s.getRange('C:C').format.columnWidth=4;
  s.getRange('D:H').format.columnWidth=15;
  s.freezePanes.freezeRows(3);
}
src.getRange('C:C').format.columnWidth=18;
src.getRange('D:D').format.columnWidth=28;
src.getRange('E:E').format.columnWidth=66;
bar(src,1,'Primary source inputs (USD millions except shares and prices)','E');
src.getRange('A3:E3').values=[['Company / metric','Value','Type','Period','Source URL']];
src.getRange('A3:E3').format={fill:teal,font:{bold:true,color:'#FFFFFF'}};
const ua='https://www.sec.gov/Archives/edgar/data/1336917/000133691726000111/ua-20260630.htm';
const eK='https://www.sec.gov/Archives/edgar/data/33488/000143774926006094/esca20251231_10k.htm';
const eQ='https://www.sec.gov/Archives/edgar/data/33488/000143774926024943/esca20260630_10q.htm';
const fK='https://www.sec.gov/Archives/edgar/data/1374328/000143774926010680/ftlf20251231_10k.htm';
const fQ='https://www.sec.gov/Archives/edgar/data/1374328/000143774926027478/ftlf20260630_10q.htm';
const rows={
  4:['UA cash',395.981,'Filed','Jun 2026',ua],5:['UA debt',591.158,'Filed','Jun 2026',ua],
  7:['Escalade FY25 revenue',240.158,'Filed','FY2025',eK],8:['Escalade H1 2026 revenue',113.487,'Filed','H1 2026',eQ],9:['Escalade H1 2025 revenue',109.812,'Filed','H1 2025',eQ],
  10:['Escalade FY25 operating income',18.727,'Filed','FY2025',eK],11:['Escalade H1 2026 operating income',17.769,'Filed','H1 2026',eQ],12:['Escalade H1 2025 operating income',6.273,'Filed','H1 2025',eQ],13:['Escalade tariff recovery in H1 2026',9.875,'Filed','H1 2026',eQ],
  14:['Escalade cash',16.392,'Filed','Jun 2026',eQ],15:['Escalade debt',14.881,'Filed','Jun 2026',eQ],16:['Escalade shares (millions)',13.766074,'Filed','Jun 2026',eQ],17:['Escalade close per share',18.89,'Secondary quote','Oct 22 2026','https://stockanalysis.com/stocks/esca/history/'],
  18:['Escalade D&A FY25',5.063,'Filed','FY2025',eK],19:['Escalade D&A H1 2026',2.503,'Filed','H1 2026',eQ],20:['Escalade D&A H1 2025',2.501,'Filed','H1 2025',eQ],
  21:['Escalade capex FY25',2.512,'Filed','FY2025',eK],22:['Escalade capex H1 2026',1.290,'Filed','H1 2026',eQ],23:['Escalade capex H1 2025',.976,'Filed','H1 2025',eQ],
  25:['FitLife FY25 revenue',81.458,'Filed','FY2025',fK],26:['FitLife H1 2026 revenue',51.874,'Filed','H1 2026',fQ],27:['FitLife H1 2025 revenue',32.063,'Filed','H1 2025',fQ],
  28:['FitLife FY25 operating income',10.062,'Filed','FY2025',fK],29:['FitLife H1 2026 operating income',6.416,'Filed','H1 2026',fQ],30:['FitLife H1 2025 operating income',5.476,'Filed','H1 2025',fQ],
  31:['FitLife cash',1.089,'Filed','Jun 2026',fQ],32:['FitLife debt',38.1,'Filed','Jun 2026',fQ],33:['FitLife equity cap',77.62,'Secondary quote','Oct 22 2026','https://robinhood.com/us/en/stocks/FTLF/'],
  34:['FitLife D&A FY25',.420,'Filed','FY2025',fK],35:['FitLife D&A H1 2026',.500,'Filed','H1 2026',fQ],36:['FitLife D&A H1 2025',.033,'Filed','H1 2025',fQ],
  37:['FitLife capex FY25',.042,'Filed','FY2025',fK],38:['FitLife capex H1 2026',0,'Filed','H1 2026',fQ],39:['FitLife capex H1 2025',.029,'Filed','H1 2025',fQ]
};
for (const [row,data] of Object.entries(rows)) src.getRange(`A${row}:E${row}`).values=[data];
src.getRange('B4:B39').setNumberFormat(num);
src.getRange('B4:B39').format.font.color='#0000FF';
put(src,'A41','Secondary quotes are indicative; verify before submission. Assumptions are on each DCF tab.');

function build(s, kind) {
  const E=kind==='Escalade', name=E?'Escalade':'FitLife', S="'Sources'!";
  bar(s,1,`${name} | standalone DCF and illustrative offer`);
  put(s,'A2','USD millions; Oct 22, 2026 information cut-off; rolling years after June 2026 LTM');
  bar(s,4,'Historical base and deal assumptions','B');
  const labels={5:'LTM revenue to June 2026',6:'LTM operating income (normalized)',7:'LTM operating margin',8:'Target cash',9:'Target debt',10:E?'October 22 share price':'October 22 common equity cap',11:'Shares outstanding (millions)',12:'Indicative control premium',13:'Equity offer',14:'Assumed fees',15:'Stock share of equity offer',16:'Enterprise offer',17:'Cash paid to sellers',18:'Stock issued to sellers',19:'UA closing cash after deal',20:'Assumed WACC',21:'Assumed terminal growth',22:'Cash tax assumption',23:'D&A / revenue assumption',24:'Capex / revenue assumption',25:'NWC investment / new revenue',27:'PV explicit cash flows',28:'Terminal value at end of Year 5',29:'PV terminal value',30:'Standalone operating EV',31:'Standalone equity value',32:'Standalone EV less offer EV'};
  for (const [r,label] of Object.entries(labels)) put(s,`A${r}`,label);
  formula(s,'B5',E?`=${S}B7+${S}B8-${S}B9`:`=${S}B25+${S}B26-${S}B27`);
  formula(s,'B6',E?`=${S}B10+${S}B11-${S}B12-${S}B13`:`=${S}B28+${S}B29-${S}B30`);
  formula(s,'B7','=B6/B5');
  formula(s,'B8',`=${S}B${E?14:31}`); formula(s,'B9',`=${S}B${E?15:32}`);
  formula(s,'B10',`=${S}B${E?17:33}`);
  if(E) formula(s,'B11',`=${S}B16`); else put(s,'A11','Shares (not used: quote is equity cap)');
  put(s,'B12',.25); formula(s,'B13',E?'=B10*B11*(1+B12)':'=B10*(1+B12)');
  put(s,'B14',E?6:4); put(s,'B15',E?.6:.5);
  formula(s,'B16','=B13+B9-B8');formula(s,'B17','=B13*(1-B15)');formula(s,'B18','=B13*B15');
  formula(s,'B19',`=${S}B4+B8-B17-B9-B14`);
  put(s,'B20',E?.11:.12);put(s,'B21',.025);put(s,'B22',.25);
  put(s,'B23',E?.021:.01);put(s,'B24',E?.012:.005);put(s,'B25',E?.15:.12);
  s.getRange('B5:B32').setNumberFormat(num);
  for (const r of [7,12,15,20,21,22,23,24,25]) s.getRange(`B${r}`).setNumberFormat(pct);
  for (const r of [12,14,15,20,21,22,23,24,25]) s.getRange(`B${r}`).format.font.color='#0000FF';
  for (const r of [5,6,8,9,10,11]) s.getRange(`B${r}`).format.font.color='#008000';
  s.getRange('D4:H4').values=[['Year 1','Year 2','Year 3','Year 4','Year 5']];
  s.getRange('D4:H4').format={fill:teal,font:{bold:true,color:'#FFFFFF'}};
  const growth=E?[.02,.03,.03,.03,.02]:[.03,.05,.05,.04,.03];
  const margin=E?[.0835,.085,.0875,.09,.09]:[.11,.112,.115,.118,.12];
  s.getRange('D5:H5').values=[growth]; s.getRange('D6:H6').values=[margin];
  s.getRange('D5:H6').format.font.color='#0000FF';
  s.getRange('D5:H6').setNumberFormat(pct);
  for (const [r,label] of [[8,'Revenue'],[9,'EBIT'],[10,'Cash taxes'],[11,'D&A added back'],[12,'Capex deducted'],[13,'Incremental NWC investment'],[14,'Unlevered FCF'],[15,'Discount factor'],[16,'Present value of FCF']]) put(s,`C${r}`,`  ${label}`);
  s.getRange('C:C').format.columnWidth=27;
  for (let i=0;i<5;i++) {
    const c='DEFGH'[i],p='CDEFG'[i];
    formula(s,`${c}8`,i?`=${p}8*(1+${c}5)`:`=$B$5*(1+${c}5)`);
    formula(s,`${c}9`,`=${c}8*${c}6`);
    formula(s,`${c}10`,`=MAX(${c}9,0)*$B$22`);
    formula(s,`${c}11`,`=${c}8*$B$23`);
    formula(s,`${c}12`,`=${c}8*$B$24`);
    formula(s,`${c}13`,i?`=(${c}8-${p}8)*$B$25`:`=(${c}8-$B$5)*$B$25`);
    formula(s,`${c}14`,`=${c}9-${c}10+${c}11-${c}12-${c}13`);
    formula(s,`${c}15`,`=1/(1+$B$20)^${i+1}`);
    formula(s,`${c}16`,`=${c}14*${c}15`);
  }
  s.getRange('D8:H16').setNumberFormat(num);
  s.getRange('D15:H15').setNumberFormat('0.000');
  s.getRange('C14:H14').format={fill:pale,font:{bold:true,color:navy}};
  formula(s,'B27','=SUM(D16:H16)');
  formula(s,'B28','=H14*(1+B21)/(B20-B21)');
  formula(s,'B29','=B28*H15');
  formula(s,'B30','=B27+B29');
  formula(s,'B31','=B30-B9+B8');
  formula(s,'B32','=B30-B16');
  s.getRange('A30:B32').format={fill:pale,font:{bold:true,color:navy}};
  put(s,'D19','Sensitivity: standalone EV by WACC and terminal growth');
  s.getRange('D19:H19').format={fill:navy,font:{bold:true,color:'#FFFFFF'}};
  put(s,'C20','WACC / g');
  const gs=[.015,.02,.025,.03,.035], ws=E?[.09,.10,.11,.12,.13]:[.10,.11,.12,.13,.14];
  s.getRange('D20:H20').values=[gs];
  for (let i=0;i<5;i++) {
    const row=21+i;
    put(s,`C${row}`,ws[i]);
    for(let j=0;j<5;j++) {
      const c='DEFGH'[j];
      const pv=[1,2,3,4,5].map((n,k)=>`${'DEFGH'[k]}14/(1+$C${row})^${n}`).join('+');
      formula(s,`${c}${row}`,`=${pv}+($H$14*(1+${c}$20)/($C${row}-${c}$20))/(1+$C${row})^5`);
    }
  }
  s.getRange('C21:C25').setNumberFormat(pct);s.getRange('D20:H20').setNumberFormat(pct);
  s.getRange('D21:H25').setNumberFormat(num);
  s.getRange('F23').format={fill:'#D4EBE8',font:{bold:true,color:navy}};
  put(s,'A35',E?'Tariff recovery of $9.875m removed from LTM operating income.':'LTM GAAP EBIT retains acquisition effects; growth is not organic.');
  put(s,'A36','Assumptions are team illustrations; no management forecast, purchase accounting or synergies.');
  put(s,'A37','FCF is discounted at year end; terminal FCF grows at g; WACC and g are assumptions.');
  put(s,'A38','NWC is modeled only on incremental revenue; decline releases working capital.');
  put(s,'A39','Offer EV excludes transaction fees; closing cash includes target cash and debt repayment.');
}
build(esc,'Escalade');build(fit,'FitLife');
bar(dec,1,'Under Armour acquisition decision | two target screens','F');
put(dec,'A2','Standalone DCF is a screening hurdle. All values USD millions; illustrative as of October 22, 2026.');
dec.getRange('A4:C4').values=[['Measure','Escalade','FitLife']];
dec.getRange('A4:C4').format={fill:teal,font:{bold:true,color:'#FFFFFF'}};
const measures={5:'LTM revenue',6:'Normalized / GAAP operating income',7:'Standalone enterprise DCF',8:'Indicative offer enterprise value',9:'DCF value less offer EV',10:'Closing UA cash',11:'Stock issued to sellers',12:'Fees',13:'No-synergy result'};
for (const [r,label] of Object.entries(measures)) put(dec,`A${r}`,label);
for (const [col,tab] of [['B','Escalade DCF'],['C','FitLife DCF']]) {
  const q=`'${tab}'!`;
  for (const [r,ref] of [[5,'B5'],[6,'B6'],[7,'B30'],[8,'B16'],[9,'B32'],[10,'B19'],[11,'B18'],[12,'B14']]) formula(dec,`${col}${r}`,`=${q}${ref}`);
  formula(dec,`${col}13`,`=IF(${col}9>=0,"Meets standalone DCF","Below offer price")`);
}
dec.getRange('B5:C12').setNumberFormat(num);
dec.getRange('A7:C10').format.rowHeight=24;
dec.getRange('A9:C9').format={fill:pale,font:{bold:true,color:navy}};
put(dec,'A16','Decision gate');put(dec,'A17','Escalade: stronger strategic fit, but confirm case eligibility and brand licenses.');
put(dec,'A18','FitLife: lower cost, but legacy sales decline and supplement risk require proof.');
put(dec,'A19','Neither indicative offer clears standalone DCF on these assumptions.');
put(dec,'A20','Require verified, risk-adjusted synergy PV plus integration costs before an offer.');
put(dec,'A22','Limitations');
put(dec,'A23','Historical periods end June 2026; no current company guidance is used as a DCF forecast.');
put(dec,'A24','Share quotes are secondary and need licensed price verification.');
put(dec,'A25','No purchase accounting, tax shields, financing cost, market reaction or merger probability.');
dec.getRange('A:A').format.columnWidth=67;
dec.getRange('B:C').format.columnWidth=21;
for (const s of [dec,esc,fit,src]) s.getRange('A1').format.rowHeight=32;
wb.recalculate();
const inspection=await wb.inspect({kind:'region',sheetId:'Decision',range:'A4:C13',maxChars:3000});
console.log(JSON.stringify(inspection));
await fs.mkdir(outputDir,{recursive:true});
for(const [sheetName,file] of [['Decision','decision.png'],['Escalade DCF','escalade.png'],['FitLife DCF','fitlife.png'],['Sources','sources.png']]) {
  try {
    const p=await wb.render({sheetName,range:sheetName==='Sources'?'A1:E23':'A1:H39',scale:1.25,format:'png'});
    await fs.writeFile(outputDir+file,new Uint8Array(await p.arrayBuffer()));
  } catch(e) { console.error('Render failure:',sheetName,e.message); throw e; }
}
const xlsx=await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outputDir+'target_valuation.xlsx');
console.log('Saved '+outputDir+'target_valuation.xlsx');
