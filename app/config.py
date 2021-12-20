import os


from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret 


dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-3]
config = Config(f'{root_dir}.env')

DATABASE_URL = f'sqlite:///{root_dir}' + config('DB_NAME', cast=str)

SECRT_KEY = config('SECRET_KEY', cast=Secret)