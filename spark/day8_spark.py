from pyspark.sql.functions import col
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Day 8 Spark SQL").getOrCreate()
df = spark.read.csv("day7_practice.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("sales")
result = spark.sql(""" 
SELECT product, price * quantity AS total
FROM sales
where quantity > 2
""")
result.show()
