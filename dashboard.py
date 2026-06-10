import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)
# convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')


def getSalesByCategory():
    # Get sales based on category
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
    # get sales based on sub category
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
    # Get sales based on region
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


def getProfitByRegion():
    # Get profit based on region
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
    # Get profit based on category
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


def getTopCustomers():
    # Get top customers based on sales
    top_customers = (
        df.groupby('Customer Name')['Sales']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    top_customers.plot(
        kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    plt.title('Top Customers by Sales')
    plt.xlabel('Customer Name')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


def calculateMonthlySales():
    # Get monthly sales
    monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))[
        'Sales'].sum()

    monthly_sales.plot(kind='line', marker='o', color='#1f77b4')

    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# Test the function
# getSalesByCategory()
# getSalesBySubCategory()
# getSalesByRegion()
# getProfitByRegion()
# getProfitByCategory()
# getTopCustomers()
calculateMonthlySales()
