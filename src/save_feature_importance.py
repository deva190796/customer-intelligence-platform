import pandas as pd
import joblib

model = joblib.load(
    "../models/campaign_model.pkl"
)

features = [
    "Income",
    "Age",
    "Total_Children",
    "Total_Spending",
    "Accepted_Campaigns",
    "Recency"
]

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

importance_df.to_csv(
    "../data/processed/feature_importance.csv",
    index=False
)

print(
    "feature_importance.csv created"
)