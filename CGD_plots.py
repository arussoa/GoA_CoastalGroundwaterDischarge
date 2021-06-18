#!/usr/bin/env python
# coding: utf-8        

#Code to recreate plots within manuscript after completion of GIS analysis
#All required input can be found in python_input_data folder

q_cgd = pd.read_csv('Q_CGD_lon.csv') #exported from GIS 


step = 0.1
to_bin = lambda x: np.floor(x / step) * step
q_cgd['lonbin'] = q_cgd.lon.map(to_bin)
cgd_grp = (q_cgd.groupby('lonbin').sum().loc[:, 'qmean7913'])/1000000000
cgd_area_grp = q_cgd.groupby('lonbin').sum().loc[:, 'CC_Area_km2']



df_grp = pd.merge(cgd_grp, cgd_area_grp, right_index=True, left_index=True)
df = df_grp.reset_index()


import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, LinearLocator)
import seaborn as sns


sns.set(font_scale=0.5)
sns.set_style('dark')

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

fig, ax = plt.subplots(1,1, figsize=(6.5, 1.0))
plt.subplots_adjust(wspace=0, hspace=0)

ax2 = ax.twinx()

ax.tick_params(length=3.5, width=0.5)
ax2.tick_params(length=3.5, width=0.5)

sns.lineplot(data=df.rolling(10).mean(), x='lonbin', y='CC_Area_km2', color='grey', ax=ax2, linewidth=0.5)

sns.lineplot(data=df.rolling(10).mean(), x='lonbin', y='qmean7913', ax=ax, color='r', linewidth=0.5)
ax2.lines[0].set_linestyle("--")

ax.set(xlabel='', xlim=(-155.6, -131.6), ylim=(0,.24))
ax.set_ylabel('CGD ($km^3/yr$)',fontsize=7)

ax.set_title('           Longitude', fontsize=8, pad=0.03)

ax2.set(xlabel='', xlim=(-155.6, -131.6), ylim=(0,115))
ax2.set_ylabel('CC area ($km^2$)', fontsize=7)
    
plt.tight_layout()
fig.savefig('Fig2.pdf', bbox_inches='tight')


sns.reset_defaults()


mei = pd.read_csv("meiv2.data", header=None, delim_whitespace=True, skiprows=1)
df = pd.melt(mei, id_vars=[0])


df['date'] = pd.to_datetime((df[0] * 10000 + df.variable * 100 + 1).apply(str), format='%Y%m%d')


mei = df.sort_values(by='date')
mei_drop = mei.loc[mei[0] < 2015,:].replace(-999, np.nan).dropna()
mei = mei_drop.set_index('date')


pdo = pd.read_csv("pdo.timeseries.ersstv5.csv")
pdo_slice = pdo.iloc[1500:1931, :]
pdo_slice['Clean Date'] = pdo_slice.Date.apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d'))
pdo = pdo_slice.set_index('Clean Date')
pdo['x'] = dates.date2num(pdo.index)


y1 = mei.value
sns.lineplot(data=pdo, x='x', y='PDO', label='PDO', linewidth=0.5)
plt.fill_between(x=mei.index, y1=mei.value, where=(y1>=0), color='red', label='El Nino')
plt.fill_between(x=mei.index, y1=mei.value, where=(y1<=0), color='blue', label='La Nina')
plt.legend()


q = pd.read_csv("Q_CGD.csv")
q['Month'] = 1
q['month shift'] = 12
q['date'] = pd.to_datetime(((q.Water_year * 10000 + 1) + q.Month * 100 + 1).apply(str), format='%Y%m%d')
df2 = q.apply(lambda x: x['date'] + pd.DateOffset(months = x['month shift']), axis=1)
q['Water Year'] = df2
q = q.set_index('Water Year')
q = q.drop(["Month", "month shift", 'date', 'Water_year'], axis=1)


import seaborn as sns
import pymannkendall as mk
from scipy import stats


x = dates.date2num(q.index)
res = stats.theilslopes(q.FWD, x)
res2 = stats.theilslopes(q.CGD, x)


fig, axes = plt.subplots(4, 1, figsize=(7.1, 6), sharex=True)
sns.color_palette('pastel')
plt.subplots_adjust(wspace=0, hspace=0.1)

sns.lineplot(ax=axes[0], data=pdo, x='x', y='PDO', label='PDO', linewidth=0.5)

y1 = mei.value
axes[0].fill_between(x=mei.index, y1=mei.value, where=(y1>=0), color='red', label='El Nino')
axes[0].fill_between(x=mei.index, y1=mei.value, where=(y1<=0), color='blue', label='La Nina')
axes[0].set(ylabel= 'Multivariate\nIndex')
axes[0].yaxis.set_minor_locator(AutoMinorLocator(2))
axes[0].legend(fontsize=8)

sns.lineplot(ax=axes[1], data=q, x=q.index, y="FWD", linestyle="-", marker='o', color='blue')
axes[1].plot(x, res[1] + res[0] * x, 'k-')
axes[1].set_ylabel('FWD ($km^3/yr$)')

sns.lineplot(ax=axes[2], data=q, x=q.index, y="CGD", linestyle="-", marker='o', color='green')
axes[2].plot(x, res2[1] + res2[0] * x, 'k-')
axes[2].set_ylabel('CGD ($km^3/yr$)')
axes[2].yaxis.set_minor_locator(AutoMinorLocator(5))

sns.lineplot(ax=axes[3], data=q, x=q.index, y="Kodiak Island/Shekilof", linestyle="-", color='orange',
             linewidth=0.5, label='KIS')
sns.lineplot(ax=axes[3], data=q, x=q.index, y="Cook Inlet", linestyle="-", color='grey',
             linewidth=0.5, label='CI')
sns.lineplot(ax=axes[3], data=q, x=q.index, y="Prince William Sound", linestyle="-", color='purple',
             linewidth=0.5, label='PWS')
sns.lineplot(ax=axes[3], data=q, x=q.index, y="Central Coast", linestyle="-", color='blue',
             linewidth=0.5, label='CC')
sns.lineplot(ax=axes[3], data=q, x=q.index, y="Southeast", linestyle="-", color='green',
             linewidth=0.5, label='SE')
axes[3].legend(loc='lower right', ncol=5, fontsize=8, framealpha=0.4)
axes[3].set(ylabel='CGD ($km^3/yr$)', xlabel='Water year', ylim=(0, 7.7), xlim=(3470.5, 16254.5))
axes[3].yaxis.set_minor_locator(AutoMinorLocator(5))
axes[3].xaxis.set_minor_locator(AutoMinorLocator(4))

fig.align_ylabels()

fig.savefig('Fig3.png', bbox_inches='tight', dpi=300)


data = q['CGD'].squeeze()
mk.original_test(data)

#slope/mean:
#increasing by 0.5%/yr
#total increase over 35 year model run: 17.5%


data2 = q['FWD'].squeeze()
mk.original_test(data2)

#increasing by 0.2%/yr
#total increase: 7%


area = pd.read_csv("CGD_Area.csv")
area['q_cumsum']= area['qmean7913'].cumsum() / area['qmean7913'].sum()
area['A_cumsum']= area['CC_Area_km2'].cumsum() / area['CC_Area_km2'].sum()


df1 = area[area['CC_Area_km2'].between(1,5)]
df2 = area[area['CC_Area_km2'].between(6,10)]
df3 = area[area['CC_Area_km2'].between(11,15)]
df4 = area[area['CC_Area_km2'].between(16,20)]


fig, ax = plt.subplots(1, 1, figsize=(3.1, 2.9), sharex=True, sharey=True)
sns.set_style('white')

sns.lineplot(data=df1, x='A_cumsum', y='q_cumsum', label='1-5 km$^2$', color='red')
sns.lineplot(data=df2, x='A_cumsum', y='q_cumsum', label='6-10 km$^2$', color='orange')
sns.lineplot(data=df3, x='A_cumsum', y='q_cumsum', label='11-15 km$^2$', color='green')
sns.lineplot(data=df4, x='A_cumsum', y='q_cumsum', label='16-20 km$^2$', color='blue')

ax.yaxis.set_minor_locator(AutoMinorLocator(2))
ax.set_ylabel('Normalized Cumulative Discharge')
ax.set_xlabel('Normalized Cumulative Area')
ax.set(xlim=(0,1), ylim=(0,1))
ax.grid(color='grey', linestyle='--', linewidth=0.5)

ax.legend(fontsize=9, loc="lower right")
fig.tight_layout()
ax.axhline(0.492, color='grey',ls='-', linewidth=0.69)
ax.axhline(0.705, color='grey',ls='-', linewidth=0.69)
ax.axhline(0.865, color='grey',ls='-', linewidth=0.69)

fig.savefig('Fig4.png', bbox_inches='tight', dpi=300)

