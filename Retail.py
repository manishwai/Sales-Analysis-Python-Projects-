import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns
import  os
#
# basepath=r"C:\Users\Admin\OneDrive - Bytedance\Desktop\SalesData"
# files=os.listdir(basepath)
# print(files)
# df=pd.DataFrame()
# for file in files:
#     monthly_data=pd.read_csv(fr'C:\Users\Admin\Downloads\Sales\{file}')
#     df=pd.concat((df,monthly_data),ignore_index=True)
# pd.set_option('display.max_columns',None)
# print(df)
# df.to_csv(r'C:\Users\Admin\Downloads\Sales\Sales3.csv', index=False)

df1=pd.read_csv(r"C:\Users\Admin\Downloads\Sales\Sales3.csv")
print(df1.columns)
print(df1)
print(df1.isnull().sum())

df1=df1[df1['Quantity Ordered']!='Quantity Ordered']
print(df1.isnull().sum())
# df1=df1.dropna(how='all')
# df1 = df1.loc[df1['Order Date']!='Order Date']
# # print(df1.head())
# # print(df1.dtypes)
df1['Order Date'] = df1['Order Date'].str.replace('/','-')
df1['Order Date'] = pd.to_datetime(df1['Order Date'],format='%m-%d-%y %H:%M')
df1['Month'] = df1['Order Date'].dt.month_name()
df1['Month_N'] = df1['Order Date'].dt.month

#Conversion To Float
df1['Quantity Ordered'] = df1['Quantity Ordered'].astype('float')
df1['Price Each'] = df1['Price Each'].astype('float')

#Calculated Column
df1['TSV'] = df1['Quantity Ordered'] * df1['Price Each']
# print(df1.head())

edf=df1.groupby(['Month_N','Month'])['TSV'].sum().reset_index()
sns.barplot(data=edf,x='Month',y='TSV')
plt.show()

# What city sold the most product?
# df1['city']=df1['Purchase Address'].str.split(',',expand=True)[1]
# print(df1)
# edf=df1.groupby('city')['Quantity Ordered'].sum().sort_values(ascending=False).reset_index()
# # print(edf)
# sns.catplot(data=edf,x='city',y='Quantity Ordered',kind='bar')
# plt.show()

#What time should we display advertisements to maximize the likelihood of customer’s buying product?
df1['Hour'] = df1['Order Date'].dt.hour
df1['Minute'] = df1['Order Date'].dt.minute
a=df1.groupby('Hour')['TSV'].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=a,x='Hour',y='TSV')
plt.grid()
plt.show()

#What Products are most often sold together ?
# edf=df1[df1['Order ID'].duplicated(keep=False)]
# edf['Grouped']=edf.groupby('Order ID')['Product'].transform(lambda x:','.join(x))
from itertools import combinations
from collections import Counter
count = Counter()
row_list = []
for row in edf['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 3)))
count.most_common(10)

# What product sold the most? Why do you think it sold the most?
df1.groupby('Product')['Quantity Ordered'].sum().sort_values().plot(kind='bar')
plt.show()