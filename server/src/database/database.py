from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.definitions.credentials import EnvVariables


DATABASE_URL = EnvVariables.database_url()
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()