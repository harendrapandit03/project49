from typing import Optional
from pydantic import BaseModel ,EmailStr
from datetime import datetime

class create_user(BaseModel):
    name:str
    age:int
    email:EmailStr
    password:str
    
    
class user_out(BaseModel):
    id:int
    name:str
    age:int
    email:EmailStr
    created_at:datetime
    class config:
        from_attributes=True

class Token(BaseModel):
    access_token:str
    token_type:str
    class config:
        from_attributes=True