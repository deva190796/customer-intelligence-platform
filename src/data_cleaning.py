import pandas as pd

from config import DATA_PATH

df = pd.read_csv(DATA_PATH, sep="\t")

print("Before Cleaning")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

# Fill Income with Median

median_income = df["Income"].median()

df["Income"] = df["Income"].fillna(median_income)

print("\nAfter Cleaning")
print(df.isnull().sum())

# Save cleaned data

df.to_csv(
    "../data/processed/cleaned_data.csv",
    index=False
)

print("\nCleaned Data Saved Successfully")