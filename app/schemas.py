from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase): 
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config: 
      orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    class Config: 
      orm_mode = True
    owner_id: int
    owner: UserOut

class PostOut(BaseModel):
   Post: Post
   votes: int
   class Config: 
    orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel): 
   email: EmailStr
   password: str

class Token(BaseModel): 
   access_token: str
   token_type: str

class TokenData(BaseModel):
   id: Optional[str] = None

from typing import Annotated

class Vote(BaseModel): 
   post_id: int
   dir: Annotated[int, conint(le=1)]
