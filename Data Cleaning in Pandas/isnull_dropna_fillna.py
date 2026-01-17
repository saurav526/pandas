import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Neha", None, "Priya", "Suresh", "Neha"],
    "Age": [21, np.nan, 23, 21, 24, np.nan],
    "Marks": [85, 90, np.nan, 88, 92, 90],
    "City": ["Mumbai", "Delhi", "Pune", None, "Delhi", "Delhi"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nChecking for null values:")
print(df.isnull())
print("\nDropping rows with any null values:")
print(df.dropna())

print("\nFilling null values:")
df_filled = df.fillna({ "Name": "Unknown", "Age": df["Age"].mean(), "Marks": df["Marks"].mean(), "City": "Unknown" })
print(df_filled)

print(df.isnull().sum())
print(df_filled.isnull().sum())

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
print(df)
df["Name"].fillna("Unknown", inplace=True)
df["City"].fillna("Unknown", inplace=True)

df_replace = df.replace("Delhi", "New Delhi")
print(df_replace)
print(df_replace.replace({85: 95, 90: 100}))

print(df_replace.replace({"Name": {"Neha": "Neha Sharma", "Suresh": "Suresh Kumar"}}))



print(df.duplicated())
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)


df["Marks"] = df["Marks"].round(1)
print(df)
print(df.dtypes)
df["Age"] = df["Age"].astype(int)
print(df.dtypes) 


df.drop(columns=['Age' ,'City'], inplace=True)

print(df) 