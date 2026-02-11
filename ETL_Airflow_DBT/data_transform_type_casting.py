import pandas as pd
df = pd.read_csv("sales_data_cleaned.csv")
df.columns = [
    "order_id",
    "customer_id",
    "customer_name",
    "order_date",
    "amount",
    "city",

]
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print(df.dtypes)
