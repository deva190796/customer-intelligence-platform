import pandas as pd
import joblib
import matplotlib.pyplot as plt

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

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance\n")
print(importance)

plt.figure(figsize=(8,5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.xticks(rotation=45)

plt.title("Feature Importance")

plt.tight_layout()

plt.show()