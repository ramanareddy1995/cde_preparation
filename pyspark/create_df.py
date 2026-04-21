from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import max
spark = SparkSession.builder.appName("Create DataFrame").getOrCreate()

schema = StructType([
               StructField("emp_id",IntegerType(),True),
               StructField("emp_name",StringType(),True),
               StructField("age",IntegerType(), True),
               StructField("department",StringType(), True),
               StructField("salary",IntegerType(), True)
               ])

data = [
    (1, "ram", 30, "engineering", 80000),
    (2, "omkar", 28, "marketing", 60000),
    (3, "anji", 35, "sales", 80000),
    (4, "swamy", 23, "finance", 34000),
    (5, "badram", 27, "hr", 40000)
]

emp_df = spark.createDataFrame(data,schema)
emp_df.show()

max_sal_df = emp_df.select(max("salary").alias("max_sal"))
max_sal_df.show()