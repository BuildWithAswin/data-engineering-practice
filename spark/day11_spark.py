from db import read_data
from pyspark.sql.functions import col
df = read_data("employees")
# df = df.fillna({"age": 0})
# df.filter(col("age").isNull()).show()
df = df.dropna(subset=["age"])
df.show()
