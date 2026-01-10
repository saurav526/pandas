import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Ravi"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}
pd = pd.DataFrame(data)
print(pd)
print("Writing data to JSON file")
print(pd.to_json("otput.json", index=False))

