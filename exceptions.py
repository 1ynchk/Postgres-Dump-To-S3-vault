
def exception_pg_dump(exit_code: int):
    if exit_code != 0:
        raise ValueError('Not a zero exit code: pg_dump exited with non zero code')
    pass

def exception_gzip_file(exit_code: int):
    if exit_code != 0:
        raise ValueError('Not a zero exit code: gzip_file() exception')
    pass
