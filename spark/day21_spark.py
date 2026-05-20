from db import read_data
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("PostgresToParquet").getOrCreate()
orders_df = read_data("orders")
orders_df.write \
    .mode("overwrite") \
    .parquet("output\order_parquet")