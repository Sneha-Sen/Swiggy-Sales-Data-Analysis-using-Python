import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df= pd.read_excel("swiggy_data.xlsx")
print(df.head())
print(df.info())
print(df.describe())
print(df.tail())
print("No of rows:",df.shape[0])
print("No of columns:",df.shape[1])
print(df.dtypes)

#Total Sales
print("Total Sales",round(df['Price (INR)'].sum(),2))

#Average Rating
print("Average Rating",round(df['Rating'].mean(),2))

#Average Order Value
print("Average Order Value",round(df['Price (INR)'].mean(),2))

#Ratings Count
print("Ratings Count",round(df['Rating Count'].sum(),2))

#Total Orders
print("Total Order:",len(df))

#Monthly Sales Trend
df["Order Date"]= pd.to_datetime(df["Order Date"])
df["YearMonth"]=df["Order Date"].dt.to_period("M").astype(str)
monthly_revenue = df.groupby("YearMonth")["Price (INR)"].sum().reset_index()

plt.figure()
plt.plot(monthly_revenue["YearMonth"],monthly_revenue["Price (INR)"])
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Revenue Trend")
plt.tight_layout()
plt.show()

#Daily Sales Trend
df["DayName"]= pd.to_datetime(df["Order Date"]).dt.day_name()
daily_revenue = df.groupby("DayName")["Price (INR)"].sum().reindex(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

plt.figure(figsize=(10,5))
plt.bar(daily_revenue.index,daily_revenue.values)
plt.xticks(rotation=45)
plt.xlabel("Day")
plt.ylabel("Revenue")
plt.title("Daily Revenue Trend")
plt.tight_layout()
plt.show()

#Quarterly Performance Salary
df["Order_Date"]=pd.to_datetime(df["Order Date"])
df["Quarter"]=df["Order_Date"].dt.to_period("Q").astype(str)
quarterly_summary = (df.groupby("Quarter",as_index=False).agg(Total_Sales=("Price (INR)","sum"),AVG_Rating=("Rating","mean"),Total_Orders= ("Order_Date","count")).sort_values("Quarter")
)
print(quarterly_summary)
