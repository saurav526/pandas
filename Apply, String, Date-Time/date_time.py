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
print(df) 

df["Year"] = df["Join_Date"].dt.year
df["Month"] = df["Join_Date"].dt.month
df["Day"] = df["Join_Date"].dt.day
df["Weekday"] = df["Join_Date"].dt.day_name()

print("\nDate-Time Methods Output:\n", df)