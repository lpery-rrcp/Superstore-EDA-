import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

avg_order_value = df['Sales'].mean()

customer_count = df['Customer ID'].nunique()


# information about the dataset
# print(profit_margin)
# print(avg_order_value)
# print(customer_count)
