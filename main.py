from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {'data': 'This is a list of posts'}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.published)
    return {'new_post': f"title: {new_post.title}, content: {new_post.content}"}
   