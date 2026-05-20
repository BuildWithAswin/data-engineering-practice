from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import json
import requests

# Config

DB_CONFIG = {
    "user": "aswin",
    "host": "localhost",
    "port": 5432,
    "database": "sql_practice"
}

API_URL = "https://dummyjson.com/carts"
TABLE_NAME = "orders"

# Extract


def extract_api_data():
    print("Starting API extraction")
    url = API_URL
    response = requests.get(url)
    data = response.json()
    print("Records received:", len(data["carts"]))
    with open("/Downloads/raw_sales.json", "w") as f:
        json.dump(data, f)
    print("API data extracted.")

# Transform


def transform_sales_data():
    with open("/Downloads/raw_sales.json") as f:
        data = json.load(f)
    records = []
    for cart in data["carts"]:
        for product in cart["products"]:
            records.append({
                "sales_id": cart["id"],
                "customer_id": cart["userId"],
                "product_id": product["id"],
                "quantity": product["quantity"],
                "price": product["price"],
                "total": product["total"]
            })
    df = pd.DataFrame(records)
    df.to_csv("/Downloads/raw_sales.json", index=False)
    print("Transform complete")

# Load


def get_engine():
    return create_engine(
        f"postgresql://{DB_CONFIG['user']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )


def load_sales_data():
    df = pd.read_csv("/Downloads/raw_sales.json")
    engine = get_engine()
    df.sql(
        "sales",
        engine,
        schema="public",
        if_exists="append",
        index=False
    )


print("Data loaded into public.sales")


# DAG
with DAG(
    dag_id="api_sales_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract_api_data",
        python_callable=extract_api_data
    )

    transform = PythonOperator(
        task_id="transform_sales_data",
        python_callable=transform_sales_data
    )

    load = PythonOperator(
        task_id="load_sales_data",
        python_callable=load_sales_data
    )

    extract >> transform >> load
