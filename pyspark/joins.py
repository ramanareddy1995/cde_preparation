from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Create SparkSession
spark = SparkSession.builder \
    .appName("PySpark Join Operations") \
    .getOrCreate()

# ========== DEPARTMENT DataFrame ==========
dept_schema = StructType([
    StructField("dept_id", IntegerType(), True),
    StructField("dept_name", StringType(), True),
    StructField("location", StringType(), True)
])

dept_data = [
    (1, "Engineering", "New York"),
    (2, "Marketing", "Los Angeles"),
    (3, "Sales", "Chicago"),
    (4, "HR", "Boston"),
    (5, "Finance", "San Francisco")
]

dept_df = spark.createDataFrame(dept_data, dept_schema)
print("\n=== DEPARTMENT DataFrame ===")
dept_df.show()

# ========== EMPLOYEE DataFrame ==========
emp_schema = StructType([
    StructField("emp_id", IntegerType(), True),
    StructField("emp_name", StringType(), True),
    StructField("dept_id", IntegerType(), True),
    StructField("salary", DoubleType(), True)
])

emp_data = [
    (1, "Alice", 1, 75000.0),
    (2, "Bob", 1, 80000.0),
    (3, "Charlie", 2, 65000.0),
    (4, "Diana", 3, 70000.0),
    (5, "Eve", None, 60000.0),  # No department
    (6, "Frank", 1, 85000.0)
]

emp_df = spark.createDataFrame(emp_data, emp_schema)
print("\n=== EMPLOYEE DataFrame ===")
emp_df.show()

# ========== INNER JOIN ==========
print("\n=== INNER JOIN (Only matching records) ===")
inner_join = emp_df.join(dept_df, emp_df.dept_id == dept_df.dept_id, "inner")
inner_join.show()

# ========== LEFT OUTER JOIN ==========
print("\n=== LEFT OUTER JOIN (All from left, matching from right) ===")
left_join = emp_df.join(dept_df, emp_df.dept_id == dept_df.dept_id, "left")
left_join.show()

# ========== RIGHT OUTER JOIN ==========
print("\n=== RIGHT OUTER JOIN (All from right, matching from left) ===")
right_join = emp_df.join(dept_df, emp_df.dept_id == dept_df.dept_id, "right")
right_join.show()

# ========== FULL OUTER JOIN ==========
print("\n=== FULL OUTER JOIN (All records from both) ===")
full_join = emp_df.join(dept_df, emp_df.dept_id == dept_df.dept_id, "full")
full_join.show()

# ========== CROSS JOIN ==========
print("\n=== CROSS JOIN (Cartesian product) ===")
cross_join = emp_df.crossJoin(dept_df)
print(f"Cross join resulted in {cross_join.count()} rows")
cross_join.show(10)

# ========== Using alias for cleaner output ==========
print("\n=== JOIN with alias for cleaner output ===")
result = emp_df.alias("e").join(
    dept_df.alias("d"), 
    emp_df.dept_id == dept_df.dept_id, 
    "inner"
).select("e.emp_id", "e.emp_name", "d.dept_name", "d.location", "e.salary")
result.show()

# Stop SparkSession
spark.stop()