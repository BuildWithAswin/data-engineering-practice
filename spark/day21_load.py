from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .appName("ReadParquet") \
        .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3") \
        .getOrCreate()
df = spark.read.parquet("output/order_parquet")
df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/sql_practice") \
    .option("dbtable", "orders_temp") \
    .option("user", "postgres") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()