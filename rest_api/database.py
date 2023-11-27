from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

username = 'root'
password = config('password')
host='localhost'
port=3306
db_name='fastapi_test'

SQLALCHEMY_DATABASE_URL = f'mysql://{username}:{password}@{host}:{port}/{db_name}'

if not database_exists(SQLALCHEMY_DATABASE_URL):
    create_database(SQLALCHEMY_DATABASE_URL)
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
