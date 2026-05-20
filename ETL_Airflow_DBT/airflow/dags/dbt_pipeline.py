from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

DBT_PATH = "/Users/aswin/Documents/data-engineering-practice/ETL_Airflow_DBT/dbt/dbt_env/bin/dbt"
PROJECT_PATH = "/Users/aswin/Documents/data-engineering-practice/ETL_Airflow_DBT/dbt_project"

default_args = {
    "execution_timeout": timedelta(minutes=15)
}

with DAG(
    dag_id='dbt_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args=default_args
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=f'''
        set -e
        cd {PROJECT_PATH}
        exec {DBT_PATH} run --no-use-colors
        ''',
        env={"DBT_PROFILES_DIR": "/Users/aswin/.dbt"}
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f'''
        set -e
        cd {PROJECT_PATH}
        exec {DBT_PATH} test --no-use-colors
        ''',
        env={"DBT_PROFILES_DIR": "/Users/aswin/.dbt"}
    )

    dbt_docs = BashOperator(
        task_id='dbt_docs',
        bash_command=f'''
        set -e
        cd {PROJECT_PATH}
        exec {DBT_PATH} docs generate --no-use-colors
        ''',
        env={"DBT_PROFILES_DIR": "/Users/aswin/.dbt"}
    )

    dbt_run >> dbt_test >> dbt_docs
