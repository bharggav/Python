from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("Postgres to CSV") \
    .config("spark.jars", "C:\\Users\\bharg\\Documents\\postgresql-42.7.7.jar") \
    .config("spark.hadoop.hadoop.native.lib", "false") \
    .config("spark.sql.debug.maxToStringFields", "1000") \
    .getOrCreate()

# JDBC details
jdbc_url = "jdbc:postgresql://localhost:5432/postgres"
query = "(SELECT * FROM mini_gb.employee WHERE id = 2) AS emp"
properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}

# Read data from PostgreSQL with SQL query
df = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)

# Show result
df.show()

# Save to CSV
output_path = "file:///C:/Users/bharg/Documents/Outputdata/test"
df.write.mode("overwrite").option("header", "true").csv(output_path)

# Stop SparkSession
spark.stop()            
