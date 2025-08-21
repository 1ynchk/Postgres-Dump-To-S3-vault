# Getting started

## Requirements
You have to make sure that you have all the necessary requirements before the start:
```
python3
postgresql16
```

Setting environment variables:
```
ACCESS_KEY="your key"
SECRET_ACCESS_KEY="your key"
S3_URL="your url"
BUCKET_NAME="your bucket"
```

And install requirements (python libs):
```
git clone https://github.com/1ynchk/Postgres-Dump-To-S3-vault
cd Postgres-Dump-To-S3-vault
pip install -r requirements.txt
```

## Dump data 

Usage:
```
python3 dump.py create-dump <database-name> <path-to-save>
```

`database-name` - is required parameter
`path-to-save` - optional parameter that represents path to save dump.

After saving this file locally, the file is being saved to S3-vault.
