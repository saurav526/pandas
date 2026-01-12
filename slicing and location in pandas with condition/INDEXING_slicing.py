import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, 21, 24],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nFirst 3 rows:")
print(df[0:3])

print("\nRow with index label 2:")
print(df.loc[2])

print("\nRows 1 to 4 (Name & City):")
print(df.loc[1:4, ["Name", "City"]])

print("\nRows 1 to 3:")
print(df.loc[1:3])

print("\nRows 1 to 3 (Name & Marks):")
print(df.loc[1:3, ["Name", "Marks"]])

print("\nUsing iloc (rows 1 to 3, columns 0 to 1):")
print(df.iloc[1:4, 0:2])
print("\nUsing iloc (all rows, columns 1 to 2):")
print(df.iloc[:, 1:3])