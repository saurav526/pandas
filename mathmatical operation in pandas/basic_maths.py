import pandas as pd

# -------------------------------
# Create Sample DataFrame
# -------------------------------
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, 21, 24],
    "score": [85, 90, 78, 88, 92],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)

# basic maths-------------------------------
print("\nMean Score:", df["score"].mean())
print("Max Score:", df["score"].max())
print("Min Score:", df["score"].min())
print("Total Score:", df["score"].sum())
print("Standard Deviation:", df["score"].std())

# Count values
print("\nCity Count:\n", df["City"].value_counts())

# Group By
grouped = df.groupby("City")["score"].mean()
print("\nAverage Score by City:\n", grouped)

# Describe
print("\nDescribe:\n", df.describe())

# Correlation
print("\nCorrelation:\n", df[["score"]].corr())