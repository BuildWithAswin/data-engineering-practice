import pandas as pd


def clean_data(df):
    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()
    return df


def transform_data(df):
    df["title_length"] = df["title"].apply(len)
    df["is_long_title"] = df["title_length"] > 20


# Rename column to match warehouse schema
    df = df.rename(columns={
        "id": "order_id",
        "userId": "customer_id"
    })

# Add missing columns required by warehouse
    df["order_date"] = pd.Timestamp.today().date()
    df["total_amount"] = 100
    df["is_delivered"] = False
    df["delivery_date"] = df["order_date"] + pd.Timedelta(days=7)

    df = df[[
        "order_id",
        "customer_id",
        "order_date",
        "total_amount",
        "is_delivered",
        "delivery_date"
    ]]

    return df
