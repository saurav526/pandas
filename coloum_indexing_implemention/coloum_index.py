import pandas as pd

# -------------------------------
# Create Sample DataFrame
# -------------------------------
data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, 21, 24],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)

# -------------------------------
# COLUMN OPERATIONS
# -------------------------------

# Select column
print("\nSelect single column:\n", df["Name"])

# Select multiple columns
print("\nSelect multiple columns:\n", df[["Name", "Marks"]])

# Add new column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")
print("\nAfter adding new column:\n", df)

# Rename column
df.rename(columns={"Marks": "Score"}, inplace=True)
print("\nAfter renaming column:\n", df)

# Drop column
df.drop("Age", axis=1, inplace=True)
print("\nAfter dropping column:\n", df)

# Column data type
print("\nColumn Data Types:\n", df.dtypes)