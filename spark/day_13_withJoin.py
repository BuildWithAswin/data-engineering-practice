
# Dataframe API
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, sum
# from db import read_data
# from pyspark.sql.functions import col, sum
# from db import read_data
# orders_df = read_data("orders")
# customers_df = read_data("customers")
# df = orders_df.join(customers_df, "customer_id")
# df.select("customer_name", "total_amount").show()

# SparkSQL
from db import read_data
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Day13Spark").getOrCreate()
orders_df = read_data("orders")
customers_df = read_data("customers")
orders_df.createOrReplaceTempView("orders")
customers_df.createOrReplaceTempView("customers")
result = spark.sql("""SELECT c.customer_name, sum(o.total_amount) as total_spent
                   FROM orders o
                   INNER JOIN customers c 
                   ON c.customer_id = o.customer_id
                   group by c.customer_name
                   order by total_spent""")
result.show()
