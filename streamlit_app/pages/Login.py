import streamlit as st
import requests

st.title("🔑 Login")

email = st.text_input(
    "Email"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(
        "http://127.0.0.1:8000/login",
        json=payload
    )

    st.json(
        response.json()
    )