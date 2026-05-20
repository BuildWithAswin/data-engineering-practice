from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number, rank
from db import read_data
customers_df = read_data("customers").alias("c")
orders_df = read_data("orders").alias("o")
df = orders_df.join(customers_df, col(
    "o.customer_id") == col("c.customer_id"))


window_spec = Window.partitionBy("city").orderBy(col("total_amount").desc())

df = df.withColumn("row_num", row_number().over(window_spec))
df.filter(col("row_num") == 1).show()
