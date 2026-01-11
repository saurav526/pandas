import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, None, 24],
    "Marks": [85, 90, 78, 88, None],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df)

df.describe()
print("Shape of DataFrame:", df.shape)
print("Columns in DataFrame:", df.columns)
print("Data types of each column:\n", df.dtypes)
print("Summary statistics of DataFrame:\n", df.describe())