from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# The schema for a post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title 1", "content": "content of post 1", "id": 1},
    {"title": "title 2", "content": "content of post 2", "id": 2},
]


def find_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_index_of_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": my_posts}


@app.get("/posts")
def get_posts():
    return {"data": "A single post"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(1, 10000000)  # Adding an ID to make posts distinctive
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[-1]
    return {"detail": post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} was not found",
        )
    return {"post_detail": post}


@app.delete("/posts/{id}")
def delete_post():
    index = find_index_of_post(id)
    my_posts.pop(index)

    return {"message": "The post was successfully deleted."}
