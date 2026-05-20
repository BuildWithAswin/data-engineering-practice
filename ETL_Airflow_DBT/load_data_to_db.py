import pandas as pd
from sqlalchemy import create_engine

# Load cleaned final dataset
df = pd.read_csv("sales_data_cleaned.csv")

engine = create_engine(
    "postgresql://postgres@localhost:5432/sql_practice"
)

# Load into db
df.to_sql(
    "orders_2026",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")
