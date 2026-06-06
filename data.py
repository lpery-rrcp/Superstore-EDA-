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

print("\nSales by Category: \n", sales_by_category)

# sub category
sales_by_sub_category = (
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Sub-Category: \n", sales_by_sub_category)
