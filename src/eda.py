import pandas as pd
from config import DATA_PATH

df = pd.read_csv(DATA_PATH, sep="\t")

print("\nDataset Info\n")
print(df.info())

print("\nMissing Values\n")
print(df.isnull().sum())

print("\nSummary Statistics\n")
print(df.describe())