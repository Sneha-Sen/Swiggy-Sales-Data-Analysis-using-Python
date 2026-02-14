# Swiggy-Sales-Data-Analysis-using-Python
- Project Overview:

This project analyzes Swiggy order data using Python (Pandas & Matplotlib) to extract business insights related to revenue, ratings, and order trends.

- The objective is to understand:

Overall sales performance

Customer rating behavior

Monthly, daily, and quarterly revenue trends

Order distribution patterns

This is a pure Exploratory Data Analysis (EDA) project.

🛠️ Tech Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

📊 Key Metrics Calculated
1️⃣ Total Sales
df['Price (INR)'].sum()

2️⃣ Average Rating
df['Rating'].mean()

3️⃣ Average Order Value (AOV)
df['Price (INR)'].mean()

4️⃣ Total Ratings Count
df['Rating Count'].sum()

5️⃣ Total Orders
len(df)

📈 Analysis Performed
🔹 Monthly Revenue Trend

Converted Order Date to datetime

Created YearMonth column

Grouped revenue by month

Plotted revenue trend line chart

Business Insight:
Helps identify seasonal spikes and slow months.

🔹 Daily Revenue Trend

Extracted day names

Grouped revenue by weekday

Reindexed to maintain weekday order

Visualized using bar chart

Business Insight:
Identifies highest revenue-generating days of the week.

🔹 Quarterly Performance Analysis

Converted Order_Date to datetime

Extracted quarter

Aggregated:

Total Sales

Average Rating

Total Orders

Business Insight:
Provides high-level performance view per quarter.

📌 Data Processing Steps

Checked data structure using:

df.head()

df.info()

df.describe()

df.tail()

Verified data types

Converted date columns to datetime

Created derived columns (Month, Day, Quarter)

📉 Visualizations Created

Monthly Revenue Line Chart

Daily Revenue Bar Chart

All charts were created using Matplotlib.

🎯 Business Questions Answered

What is the total revenue generated?

What is the average order value?

Which day generates the highest revenue?

How does revenue vary month-wise?

What is quarterly performance?


