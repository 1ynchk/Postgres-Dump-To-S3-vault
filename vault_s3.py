from dotenv import load_dotenv
import boto3
import os 
import exceptions as ex
import datetime

load_dotenv()

# s3 instance
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
    endpoint_url=os.getenv('S3_URL')
)

@ex.exception_path_to_dump
def send_dump(path_to_dump: str, database_name: str, name: str) -> None:
    '''Sending dump to S3 vault'''

    try:
        s3.upload_file(
            path_to_dump,
            os.getenv('BUCKET_NAME'),
            f'{database_name}/{name}'
        )
    except Exception as e:
        raise f'An exception occured: {e}'
    print('Dumped successfuly')

@ex.exception_path_to_dump
def download_dump_s3(path_to_save: str, database_name: str) -> None:
    '''Downloading file from S3'''

    try:
        response = s3.list_objects_v2(
            Bucket=os.getenv('BUCKET_NAME'),
            Prefix=f'{database_name}/'
        )
    except Exception as e: 
        raise ValueError(f'An exception occured: {e}')
    
    ex.exception_no_contents(response)
    sorted_objects = sorted(response['Contents'], key=lambda obj: obj['LastModified'])
    downloading_obj = sorted_objects[-1]['Key']
    filename = downloading_obj.split('/')[-1]
    try:
        response = s3.download_file(
                os.getenv('BUCKET_NAME'),
                downloading_obj, 
                f'/var/lib/postgresql/16/saves/{filename}')
    except Exception as e: 
        raise ValueError(f'An exception occured: {e}')
     
    print('Downloaded successfully')

