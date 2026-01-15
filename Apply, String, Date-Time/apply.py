import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# Create Sample DataFrame
# --------------------------------
data = {
    "Name": ["Amit Sharma", "Neha Verma", "Rahul Singh", "Priya Gupta"],
    "Marks": [85, 90, 78, 88],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai"],
    "Join_Date": ["2024-01-10", "2024-02-15", "2024-03-20", "2024-04-25"]
}

df = pd.DataFrame(data)
print(df)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")

# Apply on multiple columns
df["Bonus"] = df.apply(lambda row: row["Marks"] + 5, axis=1)

print("\nAfter apply():\n", df)