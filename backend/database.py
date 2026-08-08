from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

password = quote_plus("@Crazy@67#") #password encoding

sqlalchemy_database_url=f"postgresql://postgres:{password}@localhost/appdatabase"
engine=create_engine(sqlalchemy_database_url)

SessionLocal =sessionmaker(autocommit=False,autoflush=False,bind=engine) # default values

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db   #dependency
    finally:
         db.close()