import pandas as pd
import matplotlib.pyplot as plt

from config import DATA_PATH

df = pd.read_csv(DATA_PATH, sep="\t")

plt.figure(figsize=(8,5))

plt.hist(df["Income"].dropna())

plt.title("Income Distribution")

plt.xlabel("Income")

plt.ylabel("Count")

plt.show()