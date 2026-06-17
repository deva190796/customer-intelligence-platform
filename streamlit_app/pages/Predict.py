import streamlit as st
import requests

st.title("🎯 Campaign Response Prediction")

income = st.number_input(
    "Income",
    min_value=0.0,
    value=50000.0
)

age = st.number_input(
    "Age",
    min_value=18,
    value=35
)

children = st.number_input(
    "Total Children",
    min_value=0,
    value=1
)

spending = st.number_input(
    "Total Spending",
    min_value=0.0,
    value=800.0
)

campaigns = st.number_input(
    "Accepted Campaigns",
    min_value=0,
    value=1
)

recency = st.number_input(
    "Recency",
    min_value=0,
    value=15
)

if st.button("Predict"):

    payload = {
        "Income": income,
        "Age": age,
        "Total_Children": children,
        "Total_Spending": spending,
        "Accepted_Campaigns": campaigns,
        "Recency": recency
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    result = response.json()

    if result["prediction"] == 1:

        st.success(
            f"✅ {result['result']}"
        )

    else:

        st.error(
            f"❌ {result['result']}"
        )

    st.json(result)