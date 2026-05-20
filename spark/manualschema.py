from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
spark = SparkSession.builder.appName("Day2ManulaSchema").getOrCreate()


# Define schema
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

df = spark.read.csv("schema.csv", header=True, schema=schema)

df.show()
df.printSchema()
