from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")  #for hashing password
def hash(password:str):
    return pwd_context.hash(password)

def verify(plain_password,hash_password): # type: ignore
    return pwd_context.verify(plain_password,hash_password)