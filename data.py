import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

print("Shape: ", df.shape)

print("\nColumns: ", df.columns.tolist())
print("\nData Types: ", df.dtypes)
print("\nMissing Values: ", df.isnull().sum())
print("\nSummary Statistics: \n", df.describe())
