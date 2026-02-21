from sqlalchemy import create_engine, text
from config import DB_CONFIG, TABLE_NAME


def get_engine():
    return create_engine(
        f"postgresql://{DB_CONFIG['user']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )


def load_data(df):
    engine = get_engine()

    with engine.begin() as conn:
        for _, row in df.iterrows():
            conn.execute(text(f"""
            INSERT into {TABLE_NAME} (order_id,customer_id,order_date,total_amount,is_delivered,delivery_date)
            VALUES (:order_id,
                    :customer_id,
                    :order_date,
                    :total_amount,
                    :is_delivered,
                    :delivery_date)
            ON CONFLICT(order_id)
            DO UPDATE SET
                    customer_id  = EXCLUDED.customer_id,
                    order_date   = EXCLUDED.order_date,
                    total_amount = EXCLUDED.total_amount,
                    is_delivered = EXCLUDED.is_delivered,
                    delivery_date = EXCLUDED.delivery_date;
            """), row.to_dict())  # row.to_dict() converts a pandas Series into a dictionary so it can be used for parameterized SQL execution.
