from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

from os import environ

SQLALCHEMY_DATABASE_URL = f"""postgresql://{environ['DB_USER']}:{
    environ['DB_PASSWORD']}@{environ['DB_HOST']}/{environ['DB']}"""

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
