import pandas as pd

data = pd.read_csv("./sales_data.csv")

data.columns = data.columns.str.strip()

data["Discount Band"] = data["Discount Band"].fillna("Unknown")

print(data.head())

print("Number of rows and columns:")
print(data.shape)

print("Column names:")
print(data.columns)

print("Missing values:")
print(data.isnull().sum())

print("Duplicate rows:")
print(data.duplicated().sum())

print("Total Sales:")
print(data["Sales"].sum())

print("Total Profit:")
print(data["Profit"].sum())

print("Total Units Sold:")
print(data["Units Sold"].sum())

profit_margin = (data["Profit"].sum() / data["Sales"].sum()) * 100

print("Profit Margin:")
print(profit_margin)

product_sales = data.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("Sales by Product:")
print(product_sales)

segment_sales = data.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

print("Sales by Segment:")
print(segment_sales)

segment_profit = data.groupby("Segment")["Profit"].sum().sort_values(ascending=False)

print("Profit by Segment:")
print(segment_profit)

country_sales = data.groupby("Country")["Sales"].sum().sort_values(ascending=False)

print("Sales by Country:")
print(country_sales)

year_sales = data.groupby("Year")["Sales"].sum()

print("Sales by Year:")
print(year_sales)

monthly_sales = data.groupby("Month Name")["Sales"].sum().sort_values(ascending=False)

print("Sales by Month:")
print(monthly_sales)

top_products = data.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)

print("Top 5 Products:")
print(top_products)

product_profit = data.groupby("Product")["Profit"].sum().sort_values(ascending=False)

print("Profit by Product:")
print(product_profit)

discount_profit = data.groupby("Discount Band")["Profit"].sum().sort_values(ascending=False)

print("Profit by Discount Band:")
print(discount_profit)
print("\n========== FINAL BUSINESS SUMMARY ==========")

print("Total Sales: $", round(data["Sales"].sum(), 2))
print("Total Profit: $", round(data["Profit"].sum(), 2))
print("Total Units Sold:", data["Units Sold"].sum())

profit_margin = (data["Profit"].sum() / data["Sales"].sum()) * 100
print("Profit Margin:", round(profit_margin, 2), "%")

print("Number of Records:", len(data))
print("Number of Products:", data["Product"].nunique())
print("Number of Countries:", data["Country"].nunique())