import pandas as pd
df = pd.read_csv("sales_data_deduplicate.csv")
df["order_id"] = df["order_id"].astype(int)
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
print("Duplicate order_id count:",
      df.duplicated(subset=["order_id"]).sum())
print(df[df.duplicated(subset=["order_id"], keep=False)].to_string())
df = df.drop_duplicates(subset=["order_id"])
print("Duplicate order_id count:",
      df.duplicated(subset=["order_id"]).sum())
print(df[df.duplicated(subset=["order_id"], keep=False)].to_string())
