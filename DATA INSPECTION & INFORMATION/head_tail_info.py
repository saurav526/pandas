import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, None, 24],
    "Marks": [85, 90, 78, 88, None],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df)
print("head info")
print(df.head())
print("tail info")
print(df.tail())
print("Dataframe info")
print(df.info())