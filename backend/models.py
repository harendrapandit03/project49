from .database import Base
from sqlalchemy import Column,Integer ,String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import Mapped ,mapped_column;

class User(Base):
    __tablename__="users"
    id:Mapped[str]=mapped_column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=('now()'))
