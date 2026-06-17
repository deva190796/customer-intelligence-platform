import pandas as pd
from config import DATA_PATH

df = pd.read_csv(DATA_PATH, sep="\t")

print("\nDataset Loaded Successfully\n")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())