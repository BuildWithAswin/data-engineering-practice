# Fetch data using SparkSQL
# from pyspark.sql.functions import col, sum
# from db import read_data
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("Day13Spark").getOrCreate()
# df = read_data("orders")
# df.createOrReplaceTempView("orders")
# result = spark.sql("""SELECT customer_id,SUM(total_amount) AS total_spent
#                    FROM orders
#                    GROUP BY customer_id
#                    HAVING SUM(total_amount) > 1000
#                    ORDER BY customer_id
#                    """)
#
# result.show()

# using Dataframe API
from pyspark.sql.functions import col, sum
from db import read_data
df = read_data("orders")
result = df.groupBy("customer_id") \
    .agg(sum("total_amount").alias("total_spent")) \
    .filter(col("total_spent") > 1000) \
    .orderBy(col("customer_id"))
result.show()
