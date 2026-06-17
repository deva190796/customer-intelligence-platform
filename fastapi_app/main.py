from fastapi import FastAPI
from pydantic import BaseModel
from auth_api import register_user
from auth_api import UserRegister
from auth_api import login_user
from auth_api import UserLogin
from history import save_prediction
from history import get_history
import joblib
import pandas as pd

app = FastAPI(
    title="Customer Intelligence API"
)

model = joblib.load(
    "../models/campaign_model.pkl"
)


class CustomerInput(BaseModel):

    Income: float
    Age: int
    Total_Children: int
    Total_Spending: float
    Accepted_Campaigns: int
    Recency: int


@app.get("/")
def home():

    return {
        "message": "Customer Intelligence API Running"
    }


@app.post("/predict")
def predict(data: CustomerInput):

    input_df = pd.DataFrame(
        [data.dict()]
    )

    prediction = model.predict(input_df)[0]

    probability = float(
    model.predict_proba(input_df)[0][1]
)

    if prediction == 1:

        result = "Likely To Respond"

    else:

        result = "Unlikely To Respond"

    save_prediction(
    "guest@gmail.com",
    int(prediction),
    result
)
    return {
    "prediction": int(prediction),
    "result": result,
    "probability": round(probability, 2)
}
   
@app.post("/register")
def register(user: UserRegister):

    return register_user(user)
@app.post("/login")
def login(user: UserLogin):

    return login_user(
        user.email,
        user.password
    )
    
@app.get("/history")
def history():

    return get_history()