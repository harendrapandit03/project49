from .database import Base
from sqlalchemy import Integer ,String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import Mapped ,mapped_column;

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,nullable=False)
    name:Mapped[str]=mapped_column(String,nullable=False)
    age:Mapped[int]=mapped_column(Integer,nullable=False)
    email:Mapped[str]=mapped_column(String,nullable=False)
    password:Mapped[str]=mapped_column(String,nullable=False)
    created_at:Mapped[TIMESTAMP]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=('now()'))
