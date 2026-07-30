from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import joblib
import pandas as pd

from fastapi_app.auth_api import register_user
from fastapi_app.auth_api import UserRegister
from fastapi_app.auth_api import login_user
from fastapi_app.auth_api import UserLogin
from fastapi_app.history import save_prediction
from fastapi_app.history import get_history


# ==========================
# FASTAPI APP
# ==========================

app = FastAPI(
    title="Customer Intelligence API"
)

# ==========================
# CORS
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Replace "*" with your Streamlit URL after deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# LOAD MODEL
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "campaign_model.pkl"

model = joblib.load(MODEL_PATH)


# ==========================
# INPUT SCHEMA
# ==========================

class CustomerInput(BaseModel):
    Income: float
    Age: int
    Total_Children: int
    Total_Spending: float
    Accepted_Campaigns: int
    Recency: int


# ==========================
# HOME
# ==========================

@app.get("/")
def home():
    return {
        "message": "Customer Intelligence API Running"
    }


# ==========================
# PREDICTION
# ==========================

@app.post("/predict")
def predict(data: CustomerInput):

    input_df = pd.DataFrame([data.dict()])

    prediction = int(model.predict(input_df)[0])

    probability = float(
        model.predict_proba(input_df)[0][1]
    )

    if prediction == 1:
        result = "Likely To Respond"
    else:
        result = "Unlikely To Respond"

    save_prediction(
        "guest@gmail.com",
        prediction,
        result
    )

    return {
        "prediction": prediction,
        "result": result,
        "probability": round(probability, 2)
    }


# ==========================
# REGISTER
# ==========================

@app.post("/register")
def register(user: UserRegister):
    return register_user(user)


# ==========================
# LOGIN
# ==========================

@app.post("/login")
def login(user: UserLogin):
    return login_user(
        user.email,
        user.password
    )


# ==========================
# HISTORY
# ==========================

@app.get("/history")
def history():
    return get_history()