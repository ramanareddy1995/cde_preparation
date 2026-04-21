from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import avg
# Create SparkSession
spark = SparkSession.builder \
    .appName("Employee DataFrame") \
    .getOrCreate()

# Define schema for employee data
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("department", StringType(), True),
    StructField("salary", DoubleType(), True)
])

# Sample employee data
employee_data = [
    (1, "John Doe", 30, "Engineering", 75000.0),
    (2, "Jane Smith", 28, "Marketing", 65000.0),
    (3, "Bob Johnson", 35, "Sales", 80000.0),
    (4, "Alice Brown", 32, "Engineering", 85000.0),
    (5, "Charlie Wilson", 29, "HR", 60000.0),
    (6, "Diana Davis", 31, "Finance", 78000.0),
    (7, "Edward Miller", 33, "Engineering", 90000.0),
    (8, "Fiona Garcia", 27, "Marketing", 62000.0),
    (9, "George Taylor", 36, "Sales", 82000.0),
    (10, "Helen Anderson", 30, "HR", 58000.0)
]

# Create DataFrame
emp_df = spark.createDataFrame(employee_data, schema)

avg_sal_df=emp_df.groupBy("department").agg(avg("salary").alias("avg_sal"))
avg_sal_df.show()