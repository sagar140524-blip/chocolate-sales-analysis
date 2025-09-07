# Chocolate Sales Analysis Project
# Dataset contains: Sales Person, Country, Product, Date, Amount, Boxes Shipped
# Used Pandas for cleaning & grouping, Matplotlib + Squarify for visualization

import pandas as pd
import matplotlib.pyplot as plt
import squarify as sq
# LOAD DATASET 
a=pd.read_excel("C:/Users/HP/OneDrive/Documents/Chocolate Sales.xlsx")
df=pd.DataFrame(a)
# DATA CHECK
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
# DATA CLEANING 
df.drop_duplicates(inplace=True)
# STANDARIZED COLUMNS NAME 
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
# CONVERT DATE COLUMN TO DATETIME
df["date"]=pd.to_datetime(df["date"], format="%d-%m-%Y")
# GROUPPING AND AGGREGATION
x=df.groupby("product")["amount"].sum().sort_values(ascending=False)
y=df.groupby(["country","product"])["amount"].sum().sort_values(ascending=False).head(10)
z=df.groupby("sales_person")["amount"].sum().sort_values(ascending=False).head(10)
l=df.groupby("country")["amount"].sum().sort_values(ascending=False).head()
print(x,y,z,l)

#         TREEMAP
plt.figure(figsize=(10,6))
sq.plot(sizes=x.values, label=x.index, alpha=0.8)
plt.title("Total Sales by Product")
plt.axis("off")
plt.show()

#        BAR CHART
y.plot(kind="bar",stacked=True, figsize=(10,5), title="Top 10 Sales by Country and Product", ylabel="Total Amount", xlabel="Country and Product")
plt.show()
#        horizontal bar chart
z.plot(kind="barh", color ="green", title="Top 10 Sales by Sales Person", ylabel=" Sale Amount ", xlabel="Sales Person")
plt.show()
#       pie chart 
l.plot.pie (title="Top 5 Sales by Country", ylabel="", autopct="%1.1f%%", startangle=140, cmap="tab20")
plt.show()


