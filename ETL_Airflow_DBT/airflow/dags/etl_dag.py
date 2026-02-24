from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

# ------------------------
# Default arguments
# ------------------------

default_args = {
    "owner": "aswin",
    "retries": 1,
}

# ------------------------
# Define DAG
# ------------------------

with DAG(
    dag_id="etl_pipeline_dag",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    description="Simple ETL pipeline DAG",
    tags=["etl", "learning"],
) as dag:

    # ------------------------
    # Task 1 - Extract
    # ------------------------

    def extract():
        logging.info("Extracting data...")
        print("Extract step complete")

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract,
    )

    # ------------------------
    # Task 2 - Transform
    # ------------------------

    def transform():
        logging.info("Transforming data...")
        print("Transform step complete")

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform,
    )

    # ------------------------
    # Task 3 - Load
    # ------------------------

    def load():
        logging.info("Loading data...")
        print("Load step complete")

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load,
    )

    # ------------------------
    # Set Dependencies
    # ------------------------

    extract_task >> transform_task >> load_task

