
import os

# Define project directory 
PROJECT_DIR = "cloud-based-data-processing"

# Define directory names
AWS_DIR = "aws"
AIRFLOW_DIR = "airflow"
DATA_DIR = "data"
ETL_DIR = "etl"
ANALYSIS_DIR = "analysis"

# Define files to create
AWS_FILES = ["main.py", "credentials.py"]
AIRFLOW_FILES = ["main.py", "dag.py"]
DATA_FILES = ["raw_data.csv"]
ETL_FILES = ["main.py"]
ANALYSIS_FILES = ["main.py"]

# Create directory structure
os.mkdir(PROJECT_DIR)
os.mkdir(os.path.join(PROJECT_DIR, AWS_DIR))
os.mkdir(os.path.join(PROJECT_DIR, AIRFLOW_DIR))
os.mkdir(os.path.join(PROJECT_DIR, DATA_DIR))
os.mkdir(os.path.join(PROJECT_DIR, ETL_DIR))
os.mkdir(os.path.join(PROJECT_DIR, ANALYSIS_DIR))

# Create empty files in each directory
for file in AWS_FILES:
    open(os.path.join(PROJECT_DIR, AWS_DIR, file), "a").close()

for file in AIRFLOW_FILES:
    open(os.path.join(PROJECT_DIR, AIRFLOW_DIR, file), "a").close()

for file in DATA_FILES:
    open(os.path.join(PROJECT_DIR, DATA_DIR, file), "a").close()

for file in ETL_FILES:
    open(os.path.join(PROJECT_DIR, ETL_DIR, file), "a").close()

for file in ANALYSIS_FILES:
    open(os.path.join(PROJECT_DIR, ANALYSIS_DIR, file), "a").close()
