import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Interactive Business Dashboard",
    layout="wide"
)

st.title("📊 Interactive Dashboard Development")

# Load data
import os
import pandas as pd

csv_path = os.path.join("data", "sales_data.csv")
df = pd.read_csv(csv_path)

# KPI Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{df['Sales'].sum():,}")
col2.metric("Total Profit", f"₹{df['Profit'].sum():,}")
col3.metric("Total Customers", f"{df['Customers'].sum():,}")

st.markdown("---")

# Sales Trend
fig_sales = px.line(
    df,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(fig_sales, use_container_width=True)

# Profit Analysis
fig_profit = px.bar(
    df,
    x="Month",
    y="Profit",
    title="Monthly Profit Analysis"
)

st.plotly_chart(fig_profit, use_container_width=True)

# Customer Growth
fig_customers = px.area(
    df,
    x="Month",
    y="Customers",
    title="Customer Growth"
)

st.plotly_chart(fig_customers, use_container_width=True)

# Data Table
st.subheader("Dataset")
st.dataframe(df)
