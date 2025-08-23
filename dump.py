import random
import datetime
import os 
import click
import time
import subprocess
import exceptions as ex

from vault_s3 import send_dump, download_dump_s3

@click.group()
def cli():
    pass

def gzip_file(path: str) -> int:
    '''Gzip tar file'''
    code = os.system(f"gzip {path}")
    return code

def create_name() -> str:
    '''Creating name for file'''

    r_int = random.randrange(0, 1000000000)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d_%H:%M:%S')
    name = f'{formatted_time}_{r_int}.tar'
    return name

def make_dump(full_path: str, database_name: str, name: str) -> None:
    '''Common logic'''
    
    exit_code = os.system(f"pg_dump -F tar -f '{full_path}' -U postgres {database_name}")
    ex.exception_pg_dump(exit_code)
    ex.exception_gzip_file(gzip_file(full_path))
    full_path = full_path + '.gz' 
    name = name + '.gz'
    send_dump(full_path, database_name, name)

@cli.command()
@click.argument('database_name')
@click.argument('path', default='/var/lib/postgresql/16/dumps/')
def create_dump(database_name: str, path: str) -> None:
    '''Dump backup'''

    path = path if path[-1] == '/' else f"{path}/"
    name = create_name()
    full_path = f'{path}{name}' 
    make_dump(full_path, database_name, name)

@cli.command()
@click.argument('path', default='/var/lib/postgresql/16/dumps/')
def create_dump_all(path: str) -> None:
    '''Dump backup all'''

    path = path if path[-1] == '/' else f"{path}/"
    databases = subprocess.run(['./script.sh'], capture_output=True, text=True)
    parsed_databases=[str(database) for database in databases.stdout[0:-1].strip(':').split(':')]

    for database_name in parsed_databases:
        if not os.path.isdir(f'{path}{database_name}/'): 
            os.system(f'mkdir {path}{database_name}/')
        name = create_name()
        full_path = f'{path}{database_name}/{name}' 
        make_dump(full_path, database_name, name)

@cli.command()
@click.argument('database_name')
@click.argument('path', default='/var/lib/postgresql/16/saves/')
def download_dump(database_name: str, path: str) -> None:
    '''Dump restore'''

    path = path if path[-1] == '/' else f"{path}/"
    download_dump_s3(path, database_name)
    
if __name__ == '__main__':
    cli()
