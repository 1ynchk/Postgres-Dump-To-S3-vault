from dotenv import load_dotenv
import boto3
import os 

load_dotenv()

# s3 instance
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
    endpoint_url=os.getenv('S3_URL')
)

def send_dump(path_to_dump: str, database_name: str, name: str) -> None:
    '''Sending dump to S3 vault'''

    if os.path.isfile(path_to_dump):
        try:
            s3.upload_file(
                path_to_dump,
                os.getenv('BUCKET_NAME'),
                f'{database_name}/{name}'
            )
        except Exception as e:
            raise f'An exception occured: {e}'
        print('Dumped successfuly')
    else:
        raise ValueError(f'An exception occured: file {path_to_dump} doesn\'t exists')
