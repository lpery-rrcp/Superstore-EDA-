import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

print(df.head())
