import pandas as pd
df = pd.read_csv("extract_data.csv")
# Clean column names
df.columns = df.columns.str.strip()
df["city"] = df["city"].str.strip()
df["customer_name"] = df["customer_name"].str.strip()

# Handle missing values
df["amount"] = df["amount"].fillna(0)
df = df.dropna(subset=["customer_name"])

# apply name
filtered_df = df[(df["amount"] > 5000) & (df["city"] == "Kochi")]

# print(filtered_df)
print(df)
