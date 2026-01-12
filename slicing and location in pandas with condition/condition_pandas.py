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
print("\nRows where Age > 22:")
print(df[df["Age"] > 22])   
print("\nRows where City is 'Mumbai':")
print(df[df["City"] == "Mumbai"])   
print("\nRows where Marks >= 85 and Age < 23:")
print(df[(df["Marks"] >= 85) & (df["Age"] < 23)])   
print("\nRows where City is 'Delhi' or Marks > 90:")
print(df[(df["City"] == "Delhi") | (df["Marks"] > 90)])
