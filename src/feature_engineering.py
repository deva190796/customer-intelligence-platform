import pandas as pd

df = pd.read_csv(
    "../data/processed/cleaned_data.csv"
)

#age

CURRENT_YEAR = 2026

df["Age"] = CURRENT_YEAR - df["Year_Birth"]

#total children

df["Total_Children"] = (
    df["Kidhome"] +
    df["Teenhome"]
)

# total spend

df["Total_Spending"] = (
    df["MntWines"] +
    df["MntFruits"] +
    df["MntMeatProducts"] +
    df["MntFishProducts"] +
    df["MntSweetProducts"] +
    df["MntGoldProds"]
)

#accepted campaigns

df["Accepted_Campaigns"] = (
    df["AcceptedCmp1"] +
    df["AcceptedCmp2"] +
    df["AcceptedCmp3"] +
    df["AcceptedCmp4"] +
    df["AcceptedCmp5"]
)

print("\nNew Features Created\n")

print(
    df[
        [
            "Age",
            "Total_Children",
            "Total_Spending",
            "Accepted_Campaigns"
        ]
    ].head()
)

df.to_csv(
    "../data/processed/featured_data.csv",
    index=False
)

print("\nfeatured_data.csv saved successfully")