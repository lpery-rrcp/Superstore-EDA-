import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)
# convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Sales

# Sales by Category


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


def getSalesByRegion():
    sales_by_region = (
        df.groupby('Region')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    sales_by_region.plot(
        kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    plt.title('Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

# Profits


def getProfitByRegion():
    profit_by_region = (
        df.groupby('Region')['Profit']
        .sum()
        .sort_values(ascending=False)
    )

    profit_by_region.plot(
        kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    plt.title('Profit by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Profit')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


def getProfitByCategory():
    profit_by_category = (
        df.groupby('Category')['Profit']
        .sum()
        .sort_values(ascending=False)
    )

    profit_by_category.plot(
        kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    plt.title('Profit by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Profit')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# Test the function
# getSalesByCategory()
# getSalesBySubCategory()
# getSalesByRegion()
# getProfitByRegion()
getProfitByCategory()
