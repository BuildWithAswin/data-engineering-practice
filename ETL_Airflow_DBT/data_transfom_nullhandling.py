import pandas as pd
df = pd.read_csv("sales_data.csv", header=None)
df.columns = [
    "order_id",
    "customer_id",
    "customer_name",
    "order_date",
    "amount",
    "city",
    "junk"
]
df = df.drop(columns=["junk"])

df = df.dropna(subset=["customer_name"])
df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)
df["city"] = df["city"].fillna("UNKNOWN")
print(df.isna().sum())
print(df.head().to_string())
df.to_csv("sales_data_cleaned.csv", index=False)
print(df.dtypes)
