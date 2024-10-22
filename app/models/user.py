from sqlalchemy import Column, Integer, String # Import for necessary SQL classes
from ..config.database import Base # import Base class from config

# Define User Class (SQL TABLE)
class User(Base):

    # table name
    __tablename__="users"

    # table columns
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True )
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
