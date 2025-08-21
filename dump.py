import random
import datetime
import os 
import click
import time

from vault_s3 import send_dump

@click.group()
def cli():
    pass

def gzip_file(path: str) -> int:
    print(path)
    code = os.system(f"gzip {path}")
    return code

def create_name() -> str:
    r_int = random.randrange(0, 1000000000)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d_%H:%M:%S')
    name = f'{formatted_time}_{r_int}.tar'
    return name

@cli.command()
@click.argument('database_name')
@click.argument('path', default='/var/lib/postgresql/16/dumps/')
def create_dump(database_name: str, path: str) -> None:
    name = create_name()
    full_path = f'{path}{name}' if path[-1] == '/' else f'{path}/{name}'
    exit_code = os.system(f"pg_dump -F tar -f '{full_path}' -U postgres {database_name}")

    if exit_code != 0:
       raise ValueError('Not a zero exit code')
    if gzip_file(full_path) != 0:
       raise ValueError('Not a zero exit code')
    full_path = full_path + '.gz' 
    send_dump(full_path, name)

if __name__ == '__main__':
    cli()
