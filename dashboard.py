from pathlib import Path
import streamlit as st
from data import df as store_df
from graphs import (
    calculateMonthlySales,
    getProfitByCategory,
    getProfitByRegion,
    getSalesByCategory,
    getSalesByRegion,
    getTopCustomers,
)

st.set_page_config(layout="wide")
st.markdown(
    '<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

st.title("Superstore Sales Dashboard")
st.caption("Interactive insights built from the Superstore sample dataset.")

logo_path = Path(__file__).resolve().parent / "data" / "logo.png"
if logo_path.exists():
    st.sidebar.image(str(logo_path), use_column_width=True)
else:
    st.sidebar.header("Superstore Analytics")

regions = ["All", *sorted(store_df["Region"].dropna().unique())]
categories = ["All", *sorted(store_df["Category"].dropna().unique())]

selected_region = st.sidebar.selectbox("Region", regions)
selected_category = st.sidebar.selectbox("Category", categories)

filtered_df = store_df.copy()
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

sales_value = float(filtered_df["Sales"].sum())
profit_value = float(filtered_df["Profit"].sum())
profit_margin_value = (profit_value / sales_value *
                       100) if sales_value else 0.0
avg_order_value = float(filtered_df["Sales"].mean())
customer_count_value = int(filtered_df["Customer ID"].nunique())

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${sales_value:,.0f}")
col2.metric("Total Profit", f"${profit_value:,.0f}")
col3.metric("Profit Margin", f"{profit_margin_value:.1f}%")
col4.metric("Customers", f"{customer_count_value}")

st.subheader("Sales and Profit Trends")
left_col, right_col = st.columns(2)
with left_col:
    st.pyplot(getSalesByCategory(filtered_df))
with right_col:
    st.pyplot(getProfitByCategory(filtered_df))

st.subheader("Regional Performance")
left_col, right_col = st.columns(2)
with left_col:
    st.pyplot(getSalesByRegion(filtered_df))
with right_col:
    st.pyplot(getProfitByRegion(filtered_df))

st.subheader("Customer and Monthly Analysis")
left_col, right_col = st.columns(2)
with left_col:
    st.pyplot(getTopCustomers(filtered_df))
with right_col:
    st.pyplot(calculateMonthlySales(filtered_df))
