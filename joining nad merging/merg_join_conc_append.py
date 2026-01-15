import pandas as pd

# -------------------------------
# Create Sample DataFrames
# -------------------------------

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Neha", "Rahul"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 4],
    "Score": [85, 90, 88]
})

df3 = pd.DataFrame({
    "ID": [5],
    "Name": ["Priya"],
    "Score": [92]
})

print("\nDataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)
print("\nDataFrame 3:\n", df3)

# -------------------------------
# 1. CONCAT (Row-wise)
# -------------------------------
concat_rows = pd.concat([df1, df3], ignore_index=True)
print("\nConcat Row-wise:\n", concat_rows)

# -------------------------------
# 2. CONCAT (Column-wise)
# -------------------------------
concat_cols = pd.concat([df1, df2], axis=1)
print("\nConcat Column-wise:\n", concat_cols)

# -------------------------------
# 3. MERGE (Inner Join)
# -------------------------------
inner_merge = pd.merge(df1, df2, on="ID")
print("\nInner Merge:\n", inner_merge)

# -------------------------------
# 4. MERGE (Left Join)
# -------------------------------
left_merge = pd.merge(df1, df2, on="ID", how="left")
print("\nLeft Merge:\n", left_merge)

# -------------------------------
# 5. MERGE (Right Join)
# -------------------------------
right_merge = pd.merge(df1, df2, on="ID", how="right")
print("\nRight Merge:\n", right_merge)

# -------------------------------
# 6. MERGE (Outer Join)
# -------------------------------
outer_merge = pd.merge(df1, df2, on="ID", how="outer")
print("\nOuter Merge:\n", outer_merge)

# -------------------------------
# 7. JOIN (Using Index)
# -------------------------------
df1_indexed = df1.set_index("ID")
df2_indexed = df2.set_index("ID")

join_df = df1_indexed.join(df2_indexed, how="inner")
print("\nJoin Using Index:\n", join_df)

# -------------------------------
# 8. APPEND (Deprecated)
# -------------------------------
append_df = df1.append(df3, ignore_index=True)
print("\nAppend DataFrame:\n", append_df)

print("\nAll operations completed successfully.")
print("Code execution finished.")

