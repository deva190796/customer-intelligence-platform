import streamlit as st
import requests
import pandas as pd

st.title("📜 Prediction History")

response = requests.get(
    "http://127.0.0.1:8000/history"
)

data = response.json()

if data:

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Email",
            "Prediction",
            "Result",
            "Timestamp"
        ]
    )

    st.metric(
        "Total Predictions",
        len(df)
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning(
        "No prediction history available"
    )