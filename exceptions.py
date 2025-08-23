from typing import Optional
import os 

def exception_pg_dump(exit_code: int) -> Optional[Exception]:
    if exit_code != 0:
        raise ValueError('Not a zero exit code: pg_dump exited with non zero code')
    pass

def exception_gzip_file(exit_code: int) -> Optional[Exception]:
    if exit_code != 0:
        raise ValueError('Not a zero exit code: gzip_file() exception')
    pass

def exception_path_to_dump(func):

    def inner(*args, **kwargs) -> Optional[Exception]:
        if func.__name__ == 'download_dump_s3':
            path_to_dump, others = args
            if os.path.isdir(path_to_dump):
                func(*args, **kwargs)
            else:
                text = f'An exception occured: dir {path_to_dump} doesn\'t exists'
                raise ValueError(text)
        else:
            path_to_dump, others, name = args
            if os.path.isfile(path_to_dump):
                func(*args, **kwargs)
            else:
                text = f'An exception occured: file {path_to_dump} doesn\'t exists'
                raise ValueError(text)

    return inner

def exception_no_contents(response: dict) -> Optional[Exception]:
    if response.get('Contents', None) is None:
        raise ValueError(f'An exception occured: dictionary doesn\'t have \'Contents\' key.\n Possibly, there is not such a directory.')
    pass
