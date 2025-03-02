from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app import models
from app.schemas import PostBase, PostCreate
from app.database import engine, get_db
from sqlalchemy.orm import Session


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

@app.get("/")
def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {'data': posts}

@app.post("/posts")
def create_posts(post: PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES(%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {'data': new_post}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post:
        return {'data': post}
    else:
        raise HTTPException(status_code=404, detail=f"post with id {id} not found")

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.filter() == None:
        raise HTTPException(status_code=404, detail=f"post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, updated_post: PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=404, detail=f"post with id {id} not found")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {'data': post}

    
    
    

   
   
   