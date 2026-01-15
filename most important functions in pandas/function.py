import pandas as pd

# --------------------------------
# 1️⃣ Create & Save CSV (for read_csv)
# --------------------------------
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Marks": [85, 90, None, 88, 92],
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi"]
}

df_original = pd.DataFrame(data)
df_original.to_csv("students.csv", index=False)

# --------------------------------
# 1️⃣ read_csv()
# --------------------------------
df = pd.read_csv("students.csv")
print("\nData Loaded Using read_csv():\n", df)

# --------------------------------
# 2️⃣ head()
# --------------------------------
print("\nFirst 3 Rows using head():\n", df.head(3))

# --------------------------------
# 3️⃣ info()
# --------------------------------
print("\nDataFrame Info:")
df.info()

# --------------------------------
# 4️⃣ describe()
# --------------------------------
print("\nStatistical Description:\n", df.describe())

# --------------------------------
# 8️⃣ dropna()
# --------------------------------
df_clean = df.dropna()
print("\nAfter dropna():\n", df_clean)

# --------------------------------
# 5️⃣ loc[]
# --------------------------------
print("\nUsing loc[] (Name & Marks where City is Mumbai):\n",
      df.loc[df["City"] == "Mumbai", ["Name", "Marks"]])

# --------------------------------
# 6️⃣ groupby()
# --------------------------------
grouped = df.groupby("City")["Marks"].mean()
print("\nAverage Marks by City:\n", grouped)

# --------------------------------
# 7️⃣ merge()
# --------------------------------
extra_data = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Grade": ["B", "A", "C", "B", "A"]
})

merged_df = pd.merge(df, extra_data, on="ID")
print("\nAfter merge():\n", merged_df)

# --------------------------------
# 9️⃣ apply()
# --------------------------------
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 80 else "Fail"
)
print("\nAfter apply():\n", df)

# --------------------------------
# 🔟 value_counts()
# --------------------------------
print("\nCity Value Counts:\n", df["City"].value_counts())
