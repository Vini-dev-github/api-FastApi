from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/postgres_fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLoacal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
