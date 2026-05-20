#from db import read_data
#from pyspark.sql import SparkSession
#spark = SparkSession.builder.appName("ReadCSV").getOrCreate()
#orders_df = read_data("orders")
#orders_df.write \
#    .option("header", True) \
#    .mode("overwrite") \
#    .csv("output/orders_csv/")


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Day22").getOrCreate()
#read csv
df = spark.read.csv("output/orders_csv/orders.csv",
    header = True,
    inferSchema = True
)

#Transform
df = df.filter("total_amount > 50000")

#write parquet
df.write \
    .partitionBy("order_date") \
    .mode("overwrite") \
    .parquet("output/order_parquet/")
