"""Reproducible, source-aware charts for case slides and appendix."""

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from valuation import ESCALADE, FITLIFE, deal_bridge, enterprise_value, forecast

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'presentation' / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':11,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'savefig.facecolor':'white'})
NAVY='#142A40'; TEAL='#007C83'; ORANGE='#C57432'

targets=[ESCALADE,FITLIFE]
fig,ax=plt.subplots(figsize=(9,4.8))
fig.subplots_adjust(left=.09,right=.97,top=.83,bottom=.24)
x=[0,1]; width=.35
vals=[enterprise_value(t) for t in targets]
offers=[deal_bridge(t,.6 if t is ESCALADE else .5)['offer_ev'] for t in targets]
ax.bar([i-width/2 for i in x],vals,width,label='Standalone DCF EV',color=TEAL)
ax.bar([i+width/2 for i in x],offers,width,label='Illustrative 25% premium offer EV',color=ORANGE)
for i,(v,o) in enumerate(zip(vals,offers)):
    ax.text(i-width/2,v+3,f'${v:.0f}m',ha='center',fontweight='bold')
    ax.text(i+width/2,o+3,f'${o:.0f}m',ha='center',fontweight='bold')
ax.set_xticks(x,['Escalade','FitLife']);ax.set_ylim(0,375)
ax.set_ylabel('USD millions');ax.set_title('Both indicative offers exceed standalone operating value',loc='left',color=NAVY,fontweight='bold')
ax.legend(frameon=False,loc='upper right')
fig.text(.09,.035,'Illustrative DCF; source filings through Jun 2026 and Oct 22 indicative quotes. No synergies. See workbook assumptions.',fontsize=8,color='#56616B')
fig.savefig(OUT/'valuation_comparison.png',dpi=180);plt.close(fig)

fig,ax=plt.subplots(figsize=(9,4.8))
fig.subplots_adjust(left=.09,right=.97,top=.83,bottom=.24)
for t,c in [(ESCALADE,TEAL),(FITLIFE,ORANGE)]:
    rows=forecast(t)
    ax.plot([r['year'] for r in rows],[r['fcf'] for r in rows],marker='o',linewidth=2.5,color=c,label=t.name)
ax.set_xticks(range(1,6),['Y1','Y2','Y3','Y4','Y5'])
ax.set_ylabel('USD millions');ax.set_ylim(0,24)
ax.set_title('Unlevered free cash flow under base assumptions',loc='left',color=NAVY,fontweight='bold')
ax.legend(frameon=False)
fig.text(.09,.035,'Team growth, margin, tax and reinvestment assumptions; rolling years after Jun 2026 LTM.',fontsize=8,color='#56616B')
fig.savefig(OUT/'fcf_forecasts.png',dpi=180);plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(10,4.4),layout='constrained')
for ax,t,ws in zip(axes,targets,[[.09,.10,.11,.12,.13],[.10,.11,.12,.13,.14]]):
    for g,style in [(.015,':'),(.025,'-'),(.035,'--')]:
        ax.plot([w*100 for w in ws],[enterprise_value(t,w,g) for w in ws],style,label=f'g={g:.1%}',linewidth=2)
    ax.axhline(deal_bridge(t,.6 if t is ESCALADE else .5)['offer_ev'],color=ORANGE,alpha=.8,label='Offer EV')
    ax.set_title(t.name);ax.set_xlabel('WACC (%)');ax.grid(alpha=.2)
    ax.legend(frameon=False,fontsize=8)
axes[0].set_ylabel('Standalone enterprise value (USD m)')
fig.suptitle('Valuation is sensitive to WACC and terminal growth',color=NAVY,fontweight='bold')
fig.savefig(OUT/'dcf_sensitivity.png',dpi=180);plt.close(fig)
