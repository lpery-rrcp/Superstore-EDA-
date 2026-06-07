import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)


def getSalesByCategory():
    sales_by_category = (
        df.groupby('Category')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    sales_by_category.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    plt.title('Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


def getSalesBySubCategory():
    sales_by_sub_category = (
        df.groupby('Sub-Category')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    sales_by_sub_category.plot(
        kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    plt.title('Sales by Sub-Category')
    plt.xlabel('Sub-Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# Test the function
getSalesByCategory()
getSalesBySubCategory()
