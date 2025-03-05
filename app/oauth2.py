from jose import JWTError, jwt
from datetime import datetime, timedelta
from app import schemas, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app import database
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# SECRET KEY 
# Algoritm 
# Expiration time 

SECRET_KEY = "ae5c9f57d4f7e7e47741bf070bda197102bef70e02b214351c4bc60a979162cf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

def create_access_token(data: dict): 
  to_encode = data.copy()
  
  expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

  return encoded_jwt

def verify_access_token(token: str, credentials_exception):

  try:
    print(token)
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    id: str = payload.get("user_id")

    if id is None: 
      raise credentials_exception
    token_data = schemas.TokenData(id=str(id))
  except JWTError:
    raise credentials_exception
  return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
  credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

  token = verify_access_token(token, credentials_exception)
  user = db.query(models.User).filter(models.User.id == token.id).first()
  return user
