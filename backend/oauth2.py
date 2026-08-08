from jose import jwt, JWTError
from datetime import datetime, timedelta
from . import schemas ,models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import  get_db
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "frSDFkuh765%&^^&GFSjiyewufFGTD%^$&t5t674FYT^%$65r574RFt"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt