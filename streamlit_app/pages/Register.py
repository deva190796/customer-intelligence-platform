import streamlit as st
import requests

st.title("🔐 User Registration")

username = st.text_input(
    "Username"
)

email = st.text_input(
    "Email"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Register"):

    payload = {
        "username": username,
        "email": email,
        "password": password
    }

    response = requests.post(
        "https://customer-intelligence-api-j066.onrender.com/register",
        json=payload
    )

    st.json(
        response.json()
    )