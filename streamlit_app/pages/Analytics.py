import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide"
)

st.title("📊 Customer Analytics Dashboard")

# -----------------------
# LOAD DATA
# -----------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "featured_data.csv"
)

segmented_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "segmented_customers.csv"
)

importance_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "feature_importance.csv"
)

# -----------------------
# KPI CARDS
# -----------------------

total_customers = len(df)

avg_income = round(
    df["Income"].mean(),
    2
)

avg_spending = round(
    df["Total_Spending"].mean(),
    2
)

response_rate = round(
    df["Response"].mean() * 100,
    2
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        total_customers
    )

with col2:
    st.metric(
        "Average Income",
        f"${avg_income:,.0f}"
    )

with col3:
    st.metric(
        "Average Spending",
        f"${avg_spending:,.0f}"
    )

with col4:
    st.metric(
        "Campaign Success Rate",
        f"{response_rate}%"
    )

st.divider()

# -----------------------
# INCOME DISTRIBUTION
# -----------------------

st.subheader("📈 Income Distribution")

fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(
    df["Income"],
    bins=30
)

ax.set_title(
    "Income Distribution"
)

ax.set_xlabel(
    "Income"
)

ax.set_ylabel(
    "Customers"
)

st.pyplot(fig)

# -----------------------
# CUSTOMER SEGMENTS
# -----------------------

st.subheader("👥 Customer Segments")

cluster_counts = (
    segmented_df["Cluster"]
    .value_counts()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(8, 5))

cluster_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Customer Segments"
)

ax.set_xlabel(
    "Cluster"
)

ax.set_ylabel(
    "Number of Customers"
)

st.pyplot(fig)

# -----------------------
# CAMPAIGN RESPONSE
# -----------------------

st.subheader("📢 Campaign Response")

response_counts = (
    df["Response"]
    .value_counts()
)

fig, ax = plt.subplots(figsize=(8, 5))

response_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)

# -----------------------
# FEATURE IMPORTANCE
# -----------------------

st.subheader("🎯 Feature Importance")

fig, ax = plt.subplots(figsize=(8, 5))

ax.barh(
    importance_df["Feature"],
    importance_df["Importance"]
)

ax.set_title(
    "Feature Importance"
)

ax.set_xlabel(
    "Importance Score"
)

st.pyplot(fig)

# -----------------------
# DATA PREVIEW
# -----------------------

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

# -----------------------
# SUCCESS MESSAGE
# -----------------------

st.success(
    "Analytics Dashboard Loaded Successfully"
)