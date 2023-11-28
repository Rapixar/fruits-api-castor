from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
Base = declarative_base()

# Define the Fruit model
class Fruit(Base):
    __tablename__ = "fruits"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    color = Column(String)

# Create a SQLite engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
