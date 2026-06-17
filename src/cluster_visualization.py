import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../data/processed/segmented_customers.csv"
)

plt.figure(figsize=(8,6))

plt.scatter(
    df["Income"],
    df["Total_Spending"],
    c=df["Cluster"]
)

plt.xlabel("Income")
plt.ylabel("Total Spending")
plt.title("Customer Segments")

plt.show()