import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Ravi"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}
pd = pd.DataFrame(data)
print(pd)
print("Writing data to CSV file")
print(pd.to_csv("otput.csv", index=False))

