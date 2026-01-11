import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Suresh"],
    "Age": [21, 22, 23, None, 24],
    "Marks": [85, 90, 78, 88, None],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df) 

print(df.isnull())
print("\nMemory Usage of DataFrame:")
print(df.memory_usage(deep=True))