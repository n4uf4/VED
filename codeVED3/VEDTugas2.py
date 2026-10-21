import pandas as pd, numpy as np
import matplotlib.pyplot as plt, seaborn as sns
data=pd.read_excel(r'C:\VED\codeVED3\(2026)7. Data Studi Kasus.xlsx')
data.head(9)

bruto=data['bruto']
print(bruto.describe())
print('Skewness:',bruto.skew()); print('Kurtosis:',bruto.kurt())
Q1,Q3=bruto.quantile(.25),bruto.quantile(.75); IQR=Q3-Q1
bb,ba=Q1-1.5*IQR,Q3+1.5*IQR
print('IQR:',IQR,'| batas pencilan:',bb,'-',ba)
print(data[(bruto<bb)|(bruto>ba)][['Txn_ID','Kota','Channel','Qty','bruto']])
fig,ax=plt.subplots(1,2,figsize=(11,4))
sns.boxplot(y=bruto,ax=ax[0]); ax[0].set_title('Boxplot Bruto')
sns.histplot(bruto,bins=6,ax=ax[1]); ax[1].set_title('Histogram Bruto')
plt.tight_layout(); plt.show()

ring=data.groupby('Kota')['bruto'].agg(Frekuensi='count',Total='sum',Mean='mean',Median='median',Std='std',Min='min',Max='max')
ring['Kontribusi (%)']=(ring['Total']/ring['Total'].sum()*100).round(2)
print(ring.round(2))
fig,ax=plt.subplots(1,2,figsize=(11,4))
sns.barplot(data=ring.reset_index(),x='Kota',y='Total',errorbar=None,ax=ax[0]); ax[0].set_title('Total Bruto per Kota')
sns.boxplot(data=data,x='Kota',y='bruto',ax=ax[1]); sns.stripplot(data=data,x='Kota',y='bruto',color='k',ax=ax[1]); ax[1].set_title('Sebaran Bruto per Kota')
plt.tight_layout(); plt.show()
# sensitivitas: tanpa T007
print(data[data.Txn_ID!='T007'].groupby('Kota')['bruto'].agg(['count','sum','mean','median']))

piv=data.pivot_table(values='bruto',index='Kota',columns='Channel',aggfunc='sum',fill_value=0,margins=True,margins_name='Total')
print(piv)
print(data.pivot_table(values='bruto',index='Kota',columns='Channel',aggfunc='count',fill_value=0,margins=True,margins_name='Total'))
print(data.pivot_table(values='bruto',index='Kota',columns='Channel',aggfunc='mean',margins=True,margins_name='Rata-rata').round(0))
piv.drop(index='Total',columns='Total').plot(kind='bar',figsize=(7,4),title='Total Bruto per Kota menurut Channel'); plt.ylabel('Bruto (Rp)'); plt.xticks(rotation=0); plt.show()
import plotly.express as px
px.treemap(data,path=['Kota','Channel'],values='bruto',title='Treemap Bruto: Kota > Channel').show()
# sensitivitas tanpa T007
print(data[data.Txn_ID!='T007'].pivot_table(values='bruto',index='Kota',columns='Channel',aggfunc='sum',fill_value=0,margins=True))
