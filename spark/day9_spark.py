from db import read_data
from pyspark.sql.functions import col
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Day 8 Spark SQL").getOrCreate()

df.createOrReplaceTempView("sales_df")
orders_df = read_data("orders")
customers_df = read_data("customers")

df = orders_df.join(
    customers_df,
    orders_df.order_id == customers_df.customer_id,
    "inner"
)
df.show()
