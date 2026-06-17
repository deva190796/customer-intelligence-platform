import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(
    "../data/processed/featured_data.csv"
)

features = [
    "Income",
    "Age",
    "Total_Spending",
    "Accepted_Campaigns"
]

X = df[features]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nCluster Counts\n")

print(
    df["Cluster"].value_counts()
)

df.to_csv(
    "../data/processed/segmented_customers.csv",
    index=False
)

print(
    "\nsegmented_customers.csv saved successfully"
)