from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Day2inferschema") \
    .getOrCreate()

df = spark.read.csv("schema.csv", header=True, inferSchema=True)
df.printSchema()
