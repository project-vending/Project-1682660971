python
from pyspark.sql import SparkSession

# Set up the Spark session
spark = SparkSession.builder.appName("ETL").getOrCreate()

# Load the raw data
raw_data_df = spark.read.csv("../data/raw_data.csv", header=True)

# Perform ETL processing
processed_data_df = raw_data_df.select(
    "col1", "col2", "col3"
).filter(
    raw_data_df["col1"] > 100
)

# Write the processed data to a new file
processed_data_df.write.csv("../data/processed_data.csv", header=True)

# Stop the Spark session
spark.stop()
