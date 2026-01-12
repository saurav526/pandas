import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, None, 24],
    "Marks": [85, 90, 78, 88, None],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data , columns=["Name", "Age", "Marks", "City"])
print(df)

print("Number of dimensions (ndim):", df.ndim)
print("Size (total number of elements):", df.size)
print("Shape (rows, columns):", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Columns in DataFrame:", df.columns)

print("Data count:\n", df.count())
print(df.index)

