import boto3
from botocore.exceptions import NoCredentialsError
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

AWS_ACCESS_KEY_ID = 'AKIA5FTZABD23BTA2HK3'
AWS_SECRET_ACCESS_KEY = 'EZJeVQ7HbU/o0i19/Apz/9ZcUOZ8tVhYFETzvvi+'
REGION_NAME = 'us-east-1'
BUCKET_NAME = 'your-bucket-name'

# Configure AWS
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=REGION_NAME)

def upload_file_to_s3(file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, BUCKET_NAME, object_name)
        print(f"File {file_name} uploaded to S3 bucket {BUCKET_NAME} as {object_name}.")
    except NoCredentialsError:
        print("Credentials not available")

def download_file_from_s3(object_name, file_name=None):
    if file_name is None:
        file_name = object_name

    try:
        s3.download_file(BUCKET_NAME, object_name, file_name)
        print(f"File {object_name} downloaded from S3 bucket {BUCKET_NAME} as {file_name}.")
    except NoCredentialsError:
        print("Credentials not available")

# Configure SQLAlchemy
DATABASE_URL = "mysql+pymysql://username:password@your-rds-endpoint/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
