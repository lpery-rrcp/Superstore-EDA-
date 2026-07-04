from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent / \
    "data" / "Sample - Superstore.csv"
df = pd.read_csv(DATA_PATH, encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")


def _style_axes(ax, title, xlabel, ylabel):
    ax.set_title(title, fontsize=12, pad=8)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    return ax


def getSalesByCategory(dataframe=None):
    data = dataframe if dataframe is not None else df
    sales_by_category = data.groupby(
        "Category")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    sales_by_category.plot(
        kind="bar", color=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
    _style_axes(ax, "Sales by Category", "Category", "Total Sales")
    return fig


def getSalesBySubCategory(dataframe=None):
    data = dataframe if dataframe is not None else df
    sales_by_sub_category = data.groupby(
        "Sub-Category")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    sales_by_sub_category.plot(
        kind="bar", color=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
    _style_axes(ax, "Sales by Sub-Category", "Sub-Category", "Total Sales")
    return fig


def getSalesByRegion(dataframe=None):
    data = dataframe if dataframe is not None else df
    sales_by_region = data.groupby(
        "Region")["Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    sales_by_region.plot(kind="bar", color=[
                         "#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
    _style_axes(ax, "Sales by Region", "Region", "Total Sales")
    return fig


def getProfitByRegion(dataframe=None):
    data = dataframe if dataframe is not None else df
    profit_by_region = data.groupby(
        "Region")["Profit"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    profit_by_region.plot(
        kind="bar", color=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
    _style_axes(ax, "Profit by Region", "Region", "Total Profit")
    return fig


def getProfitByCategory(dataframe=None):
    data = dataframe if dataframe is not None else df
    profit_by_category = data.groupby(
        "Category")["Profit"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    profit_by_category.plot(
        kind="bar", color=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
    _style_axes(ax, "Profit by Category", "Category", "Total Profit")
    return fig


def getProfitBySubCategory(dataframe=None):
    data = dataframe if dataframe is not None else df
    profit_by_sub_category = data.groupby(
        "Sub-Category")["Profit"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    profit_by_sub_category.plot(
        kind="bar", color=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
    _style_axes(ax, "Profit by Sub-Category", "Sub-Category", "Total Profit")
    return fig


def getTopCustomers(dataframe=None):
    data = dataframe if dataframe is not None else df
    top_customers = data.groupby("Customer Name")[
        "Sales"].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(7, 4))
    top_customers.plot(kind="bar", color=[
                       "#1f77b4", "#ff7f0e", "#2ca02c"], ax=ax)
    _style_axes(ax, "Top Customers by Sales", "Customer Name", "Total Sales")
    return fig


def calculateMonthlySales(dataframe=None):
    data = dataframe if dataframe is not None else df
    monthly_sales = data.groupby(data["Order Date"].dt.to_period("M"))[
        "Sales"].sum()
    fig, ax = plt.subplots(figsize=(8, 4))
    monthly_sales.plot(kind="line", marker="o", color="#1f77b4", ax=ax)
    _style_axes(ax, "Monthly Sales", "Month", "Total Sales")
    return fig
