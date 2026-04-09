from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engin = create_engine("postgresql://postgres:7777@localhost/fastapi_db")

Base = declarative_base()
Session = sessionmaker(bind=engin)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()