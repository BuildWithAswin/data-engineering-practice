from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import sum, avg, count
spark = SparkSession.builder.appName("MiniProject").getOrCreate()
df = spark.read.csv("day7_practice.csv", header=True, inferSchema=True)
# cleandata
df = df.dropna(subset=["price", "quantity"])
df = df.filter((col("price") > 0) & (col("quantity") > 0))

# add new column
df = df.withColumn("total_price", col("price") * col("quantity"))

# aggreagate
result = df.groupBy("product").agg(
    sum("total_price").alias("total_sales"),
    avg("total_price").alias("avg_sales"),
    count("*").alias("total_orders")
)

# step6
result = result.orderBy(col("total_sales").desc())
result.show()
