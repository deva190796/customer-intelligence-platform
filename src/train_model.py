import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

df = pd.read_csv(
    "../data/processed/featured_data.csv"
)

features = [
    "Income",
    "Age",
    "Total_Children",
    "Total_Spending",
    "Accepted_Campaigns",
    "Recency"
]

X = df[features]

y = df["Response"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:\n")
print(round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")
print(
    classification_report(
        y_test,
        predictions
    )
)

joblib.dump(
    model,
    "../models/campaign_model.pkl"
)

print(
    "\nModel Saved Successfully"
)