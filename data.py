import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# Display basic information about the dataset
# print("Shape: ", df.shape)
# print("\nColumns: ", df.columns.tolist())
# print("\nData Types: ", df.dtypes)
# print("\nSummary Statistics: \n", df.describe())

# Cleaning and preprocessing
# print("Duplicates: ", df.duplicated().sum())
# print("Missing Values: ", df.isnull().sum())

# convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# print("\nData Types after conversion: ", df.dtypes)
# print("\nMissing Values after conversion: ", df.isnull().sum())


# Top metrics
# print("\nTotal Sales: ", df['Sales'].sum())
# print("\nTotal Profit: ", df['Profit'].sum())
# print("\nTotal Orders: ", df['Order ID'].nunique())
# print("\nTotal Customers: ", df['Customer ID'].nunique())

# Sales by Category
sales_by_category = (
    df.groupby('Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)

# print("\nSales by Category: \n", sales_by_category)

# sub category
sales_by_sub_category = (
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)

# print("\nSales by Sub-Category: \n", sales_by_sub_category)

# Profit by Category
profit_by_category = (
    df.groupby('Category')['Profit']
    .sum()
    .sort_values(ascending=False)
)

# print("\nProfit by Category: \n", profit_by_category)

# regional sales
sales_by_region = (
    df.groupby('Region')['Sales']
    .sum()
    .sort_values(ascending=False)
)

# print("\nSales by Region: \n", sales_by_region)

# regional profit
profit_by_region = (
    df.groupby('Region')['Profit']
    .sum()
    .sort_values(ascending=False)
)

# print("\nProfit by Region: \n", profit_by_region)

# top customers
top_customers = (
    df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# print("\nTop Customers: \n", top_customers)

# time series
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

monthly_sales = (
    df.groupby(['Year', 'Month'])['Sales']
    .sum()
    .reset_index()
)

print("\nMonthly Sales: \n", monthly_sales)
