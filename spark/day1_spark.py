from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Day1_Spark") \
    .getOrCreate()

data = [("Aswin", 25), ("John", 30)]
df = spark.createDataFrame(data, ["name", "age"])
df.printSchema()
df.filter(df.age > 25)
df.show()
