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
print("Duplicates: ", df.duplicated().sum())
print("Missing Values: ", df.isnull().sum())

# convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
