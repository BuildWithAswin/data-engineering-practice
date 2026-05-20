from pyspark.sql import SparkSession
from config import DB_CONFIG

spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3") \
    .getOrCreate()


def read_data(source):
    df = spark.read \
        .format("jdbc") \
        .options(**DB_CONFIG) \
        .option("dbtable", source) \
        .load()
    return df
