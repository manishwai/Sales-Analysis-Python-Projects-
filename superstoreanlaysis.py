import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns

df=pd.read_csv(r"C:\Users\Admin\Downloads\train.csv")
# pd.set_option('display.max_columns',None)
# print(df)
# print(df.describe())
# print(df.info)
# print(df.isnull().sum())

col=list(df.columns)
print(col)

#Yearly Sales Comparison
# df['Order Date']=pd.to_datetime(df['Order Date'],format='%d/%m/%y')
# this one was not working due to issue in date column in raw file
# so opted other way

# df['Date']=df['Order Date'].str.split('/',expand=True)[0]
# df['Month']=df['Order Date'].str.split('/',expand=True)[1]
# df['Year']=df['Order Date'].str.split('/',expand=True)[2]

df[['Day', 'Month', 'Year']] = df['Order Date'].str.split('/', expand=True).astype(int)
# # Create new 'Date' column
df['Order Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
# print(df)
# print(df.dtypes)

# ndf=df.groupby('Year')['Sales'].sum().__round__(2).reset_index()
# fig=plt.figure(figsize=(12,12))
# plt.plot(ndf['Year'].astype(str),ndf['Sales'],marker='o' , linestyle='--',color='b')
# plt.show()

# Year - Month Comparison
# print(df['Month'])
df['month_name'] = df['Order Date'].dt.month_name()
# edf=df.groupby(['Year','Month','month_name'])['Sales'].sum().__round__(2).reset_index()
# print(edf)
#
# sns.barplot(data=edf,x='Year',y='Sales',hue='month_name')
# plt.show()


# Did Our UserBase Grow
# cust_year={}
# for i in list(df['Year'].unique()):
#     cust_year[i]=len(df.loc[df['Year']==i]['Customer ID'].unique())
# l=list(cust_year.keys())
# l.sort()
# print(l)
# v=list(cust_year.values())
# print(v)
# plt.plot(l,v)
# plt.show()

# sns.countplot(data=df,x='Segment',hue='Category',palette='magma')
# plt.show()


#
# plt.figure(figsize=(15,5))
# for i in [2015,2016,2017,2018]:
#     ndf = df.loc[df['Year']==i]
#
#     sdf = ndf.groupby(['Month','month_name']).agg(totalsale=('Sales','sum')).reset_index()
#     plt.plot(sdf['month_name'],sdf['totalsale'],label=i,marker='o')
#     plt.legend()
#
# plt.show()




