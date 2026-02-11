import pandas as pd
import json
with open("orders.json") as f:
    data = json.load(f)

print(type(data))
print(len(data))

# Convert JSON → DataFrame (Flat Part)
df = pd.json_normalize(data)
print(df.columns)

# Flatten Nested Arrays (items)
items_df = pd.json_normalize(
    data,
    # record_path="items" (MOST IMPORTANT) , meaning ->“Which nested array should become rows?”
    record_path="items",
    meta=[
        "order_id",
        "order_date",
        ["customer", "customer_id"],
        ["customer", "name"],
        ["customer", "city"]
    ]
)

items_df.columns = items_df.columns.str.replace(".", "_")
items_df["customer_city"] = items_df["customer_city"].str.strip()
items_df["customer_name"] = items_df["customer_name"].str.strip()
items_df["total_price"] = items_df["price"] * items_df["qty"]


print(items_df)
