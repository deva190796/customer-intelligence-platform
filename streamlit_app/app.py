import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# -----------------------
# LOAD DATA
# -----------------------

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "featured_data.csv"
)

segmented_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "segmented_customers.csv"
)

# -----------------------
# TITLE
# -----------------------

st.title("📊 Customer Intelligence Platform")

st.markdown("""
### End-to-End Machine Learning Application

This platform provides:

✅ Customer Segmentation

✅ Campaign Response Prediction

✅ Authentication System

✅ Prediction History

✅ FastAPI Backend

✅ MLflow Tracking

---
""")

# -----------------------
# KPI CARDS
# -----------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Customers",
        len(df)
    )

with col2:
    st.metric(
        "Model Accuracy",
        "85.27%"
    )

with col3:
    st.metric(
        "Clusters",
        segmented_df["Cluster"].nunique()
    )

# -----------------------
# SUCCESS MESSAGE
# -----------------------

st.success(
    "Use the sidebar to navigate through the application."
)