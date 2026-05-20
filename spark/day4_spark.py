from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("Day4_Spark").getOrCreate()
df = spark.read.csv("day_4_practice.csv", header=True, inferSchema=True)

# Using Alias
df.select("Product", "Quantity", (col("Price").alias("Price per piece"))).show()

# Adding another column without modifiying dataframe
df.select("Product", (col("Price") * col("Quantity")).alias("total_price")).show()

# Adding another column which persist in dataframe
df = df.withColumn("Total_Price", col("Price") * col("Quantity")).show()
