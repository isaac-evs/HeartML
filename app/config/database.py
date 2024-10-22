from sqlalchemy import create_engine # create database connection
from sqlalchemy.ext.declarative import declarative_base # function to define a base class
from sqalchemy.orm import sessionmaker # Generate a new session

# Database URL
SQALCHEMY_DATABASE_URL = "sqlite:///./app.bd"

# Create Database engine
engine = create_engine(
    SQALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # Restrict the conection to only one thread (SQLite specific)

# Create a Session
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Create new Base Class
Base = declarative_base()


# Generator function to yield database session and ensure is properly closed after use
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
