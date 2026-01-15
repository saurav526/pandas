import pandas as pd
import matplotlib.pyplot as plt

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

# Line Plot
df.plot(x="Name", y="Marks")
plt.title("Marks by Student")
plt.show()

# Bar Plot
df.plot(kind="bar", x="Name", y="Marks")
plt.title("Bar Chart of Marks")
plt.show()

# Histogram
df["Marks"].plot(kind="hist")
plt.title("Marks Distribution")
plt.show()

# Box Plot
df["Marks"].plot(kind="box")
plt.title("Marks Boxplot")
plt.show()