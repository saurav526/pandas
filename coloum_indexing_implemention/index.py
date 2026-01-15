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
df.index = df.index + 1
print("\nOriginal DataFrame:\n", df, )

# -------------------------------
# View index
print("\nIndex:\n", df.index)

# Set column as index
df.set_index("Name", inplace=True)
print("\nAfter setting index:\n", df)

# Reset index
df.reset_index(inplace=True , drop=False)
print("\nAfter resetting index:\n", df)

# Sort by index
df_sorted_index = df.sort_index()
print("\nSorted by index:\n", df_sorted_index)

# Sort by column values
df_sorted_values = df.sort_values(by="Marks", ascending=False)
print("\nSorted by Marks:\n", df_sorted_values) 

df.rename(index={0: 'S1', 1: 'S2'}, inplace=True)
print("\nAfter renaming index:\n", df)