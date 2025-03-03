from typing import Optional, List
from fastapi import FastAPI, HTTPException, Response, status, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app import models, utils
from app.schemas import PostBase, PostCreate, Post, UserCreate, UserOut
from app.database import engine, get_db
from sqlalchemy.orm import Session
from app.routers import post, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True: 
    try: 
        conn = psycopg2.connect(host='localhost', database='fastapi', user= 'postgres', password="3311", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Connected to the database')
        break
    except Exception as e:
        print('Connection failed')
        print(e)
        time.sleep(2)
    

my_posts = [
    {'title': 'title of post 1', 'content': 'content of post 1', 'id': 1},
    {'title': 'favourite foods', 'content': 'I like pizza', 'id': 2},
    {'title': 'title of post 3', 'content': 'content of post 3', 'id': 3},
]

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post
    return None

def find_index_post(id):
    for i, post in enumerate(my_posts):
        if post['id'] == id:
            return i
    return None

app.include_router(post.router)
app.include_router(user.router)


    

    
    
    

   
   
   