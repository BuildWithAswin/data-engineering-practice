from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("Day5_spark").getOrCreate()
df = spark.read.csv("day_4_practice.csv", header=True, inferSchema=True)
# filter
df.filter(col("Price") < 30000).show()
# where
df.where(col("Quantity") > 2).show()
# order by
df.orderBy("Product").show()
# desc
df.orderBy(col("Product").desc()).show()
