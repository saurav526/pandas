import pandas as pd
# --------------------------------
# Create Sample DataFrame
# --------------------------------
data = {
    "Name": ["Amit Sharma", "Neha Verma", "Rahul Singh", "Priya Gupta"],
    "Marks": [85, 90, 78, 88],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai"],
    "Join_Date": ["2024-01-10", "2024-02-15", "2024-03-20", "2024-04-25"]
}

df = pd.DataFrame(data)
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
print(df)
df["Lower_Name"] = df["Name"].str.lower()
df["Upper_City"] = df["City"].str.upper()

df["First_Name"] = df["Name"].str.split().str[0]
df["Name_Length"] = df["Name"].str.len()
df["Contains_A"] = df["Name"].str.contains("A", case=False)

print("\nString Methods Output:\n", df)