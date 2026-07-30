import streamlit as st
import requests
import pandas as pd

st.title("📜 Prediction History")

API_URL = "https://customer-intelligence-api-j066.onrender.com/history"

try:
    response = requests.get(API_URL, timeout=30)

    if response.status_code == 200:

        try:
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
                st.warning("No prediction history available.")

        except requests.exceptions.JSONDecodeError:
            st.error("The backend did not return valid JSON.")
            st.write("Response received:")
            st.code(response.text)

    else:
        st.error(f"Backend returned status code: {response.status_code}")
        st.code(response.text)

except requests.exceptions.RequestException as e:
    st.error("Unable to connect to the backend.")
    st.exception(e)