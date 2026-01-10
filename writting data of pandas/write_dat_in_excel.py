import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Ravi"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
})

print(df.to_excel("output.xlsx", index=True))
print("Data written to Excel file successfully.")
print(df)
print(df.head())
print(df.tail())