import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import  seaborn as sns
df=pd.read_csv(r"C:\Users\Admin\Downloads\Sales.csv")
# print(df)
# print(df.info)
# print(df.shape)
# print(df.dtypes)
col=df.columns
print(col)

#drop unrelated/blank columns
# df=df.drop(['Status','unnamed1'],axis=1)

#check for null values
# print(df.isnull().sum())

#DropNull Values
# df=df.dropna()
# df['Amount']=df['Amount'].astype('int')
# print(df.dtypes)

#Statistical Description of data
# print(df.describe())
# print(df[['Age', 'Orders', 'Amount']].describe())

#Exploratory Data Analysis
#Gender
#Gender Count & Distribution
# sns.set_style('darkgrid')
# ax=sns.countplot(data=df ,x='Gender')
# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()

#Pie chart
# a=df['Gender'].value_counts()
# a=a.reset_index()
# a.columns=['Gender','Gender_count']
# print(a)
# plt.pie(data=a,x='Gender_count',labels='Gender',autopct='%1.2f%%')
# plt.legend()
# plt.show()

#Find the Total Amount spend by each Gender
# Total_amount=df.groupby('Gender',as_index=False)['Amount'].sum()
# print(Total_amount)
# sns.barplot(data=Total_amount,x='Gender',y='Amount')
# plt.show()

#From above graphs we can see that most of the buyers are females
# and even the purchasing power of females are greater than men

#AGEGROUP Analysis
# ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
#
# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()

#Find the spending by age Group
# Total_amount=df.groupby('Age Group',as_index=False)['Amount'].sum()
# print(Total_amount)
# sns.barplot(data=Total_amount,x='Age Group',y='Amount')
# plt.show()

#Find the spending  by age group and gender basis
# Total_amount=df.groupby(['Age Group','Gender'],as_index=False)['Amount'].sum()
# print(Total_amount)
# sns.barplot(data=Total_amount,x='Age Group',y='Amount',hue='Gender')
# plt.show()
# From above graphs we can see that most of the buyers are of age group
# between 26-35 yrs female

#State
## total number of orders from top 10 states
# State_Order=(df.groupby('State',as_index=False)['Orders'].sum()
#              .sort_values(by='Orders',ascending=False).head(10))
# print(State_Order)
# plt.figure(figsize=(15,4))
# sns.lineplot(data=State_Order,x='State',y='Orders')
# plt.show()

## total Salesfrom top 10 states
# State_sales=(df.groupby('State',as_index=False)['Amount'].sum()
#              .sort_values(by='Amount',ascending=False).head(10))
# print(State_sales)
# plt.figure(figsize=(15,4))
# sns.barplot(data=State_sales,x='State',y='Amount')
# plt.show()

#Zone Wise


#Marital Status
# ax=sns.countplot(data=df,x='Marital_Status',hue='Gender')
# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()

# Marital_State_Sales=df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# plt.figure(figsize=(15,5))
# sns.barplot(data=Marital_State_Sales , x='Gender', y='Amount',hue='Marital_Status')
# plt.show()

# Occupation
# plt.figure(figsize=(15,5))
# ax = sns.countplot(data = df, x = 'Occupation')
#
# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()

#Which Occupation people spend more

# Occupation_Sales=df.groupby(['Occupation', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# plt.figure(figsize=(15,5))
# ax=sns.barplot(data=Occupation_Sales , x='Occupation', y='Amount',hue='Gender')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
# plt.show()


# Product Category
# ax = sns.countplot(data = df, x = 'Product_Category')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()

#Sales Product_Category Wise
# Product_Category_Sales = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
# sns.set(rc={'figure.figsize':(20,5)})
# sns.barplot(data = Product_Category_Sales, x = 'Product_Category',y= 'Amount')
# plt.show()

#Total 10 most sold product
# df.groupby('Product_ID')['Orders'].sum().sort_values(ascending=False).head(10).plot(kind='bar')
# plt.show()