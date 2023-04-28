python
import boto3
from credentials import ACCESS_KEY, SECRET_KEY

def main():
    # Connect to AWS using credentials
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    # List all buckets in S3
    response = s3.list_buckets()

    # Print bucket names
    for bucket in response['Buckets']:
        print(f'Bucket name: {bucket["Name"]}')

if __name__ == '__main__':
    main()
