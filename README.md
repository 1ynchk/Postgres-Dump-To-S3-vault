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
# Functionality 
## create_dump()
Description: 
Makes dump of the defined database. The function creates file with `.tar.gz` file extansion locally and then moves it to S3 vault. Creates the same name directory as database name in S3 bucket.

Args:
 - `database_name` - is required parameter, that represents name of database to dump on;
 - `path` - optional parameter that represents path to save dump locally (default path - `/var/lib/postgresql/16/dumps`). 

Usage:
```
python3 dump.py create-dump database-name path-to-save
```

## create_dump_all()
Description: 
Makes dump of all databases which are allowed to connect to. The function creates file with `.tar.gz` file extansion locally and then moves it to S3 vault. Creates the same name directories as database's names in S3 bucket.

Args:
 - `path-to-save` - optional parameter that represents path to save dump locally (default path - `/var/lib/postgresql/16/dumps`). 

Usage:
```
python3 dump.py create-dump-all path
```

## download_dump()
Description:
Downloads the latest dump of the database from S3 vault. Saves dump file locally. 

Args:
 - `database_name` - is required parameter, that represents name of database;
 - `path` - optional parameter that represents path to save dump locally (default path - `/var/lib/postgresql/16/saves`).

Usage:
```
python3 dump.py download-dump database_name path
```
