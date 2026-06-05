import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# Display basic information about the dataset
# print("Shape: ", df.shape)
# print("\nColumns: ", df.columns.tolist())
# print("\nData Types: ", df.dtypes)
# print("\nMissing Values: ", df.isnull().sum())
# print("\nSummary Statistics: \n", df.describe())

# Cleaning and preprocessing
print("Duplicates: ", df.duplicated().sum())
print("Missing Values: ", df.isnull().sum())
