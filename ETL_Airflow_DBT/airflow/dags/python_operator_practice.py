from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import random


# Task1 - generate random number
def gen_random_numbers(ti):
    number = random.randint(1, 100)
    print(f"Generated number: {number}")
    # Push value to Xcom
    ti.xcom_push(key="random_number", value=number)


# Task2 - multiply
def multiply_numbers(ti):
    # pull values from xcom
    number = ti.xcom_pull(
        task_ids="generate_task",
        key="random_number"
    )
    result = number * 5
    print(f"Multiplied result: {result}")

    ti.xcom_push(key="result", value=result)

# Task3 - Print result


def print_result(ti):
    result = ti.xcom_pull(
        task_ids="multiply_task",
        key="result"
    )
    print(f"Final result is:{result}")


with DAG(
    dag_id="python_operator_practice",
    start_date=datetime(2026, 3, 8),
    schedule=None,
    catchup=False,
    tags=["practice"],
) as dag:

    generate_task = PythonOperator(
        task_id="generate_task",
        python_callable=gen_random_numbers,
    )

    multiply_task = PythonOperator(
        task_id="multiply_task",
        python_callable=multiply_numbers,
    )

    print_task = PythonOperator(
        task_id="print_task",
        python_callable=print_result,
    )

    # chain task
    generate_task >> multiply_task >> print_task
