import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, 21, 24],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Using apply to increase age by 1
df["Age"] = df["Age"].apply(lambda x: x + 1)
print("\nDataFrame after applying function to 'Age' column:")
print(df)

city_code = {"Mumbai": "MUM", "Delhi": "DEL", "Pune": "PUN"}
df["City_Code"] = df["City"].map(city_code)
print(df)
# Using applymap to format all string entries to uppercase
df_str = df.select_dtypes(include=['object'])
df_str_upper = df_str.applymap(lambda x: x.upper())
print("\nDataFrame with string entries in uppercase:")
print(df_str_upper)

df["Age"] = df["Age"].astype(float)
print(df.dtypes)
df["Marks"] = df["Marks"].astype(float)
print(df.dtypes)