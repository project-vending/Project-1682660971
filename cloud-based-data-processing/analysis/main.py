python
import pandas as pd
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("DataAnalysis").getOrCreate()

# Load data from S3
s3_input_path = "s3://your-bucket-name/your-data-folder/data.csv"
df = spark.read.csv(s3_input_path, header=True)

# Perform some data analysis
df_count = df.count()
df_mean = df.selectExpr("avg(some_numeric_field)").head()[0]

# Print results
print("Total number of rows: {}".format(df_count))
print("Mean of some_numeric_field: {}".format(df_mean))

# Save results to S3
s3_output_path = "s3://your-bucket-name/your-analysis-folder/output.csv"
df.write.csv(s3_output_path, mode="overwrite", header=True)
