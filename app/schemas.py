from pydantic import BaseModel, EmailStr
from datetime import datetime

# The pydanctic model / schema that defines the structure of a request & response
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# Overall base class
# Specifies what data the server expects from client
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


# Specifies what data the client will receive
class Post(PostBase):
    id: int
    created_at: datetime

    # We need this because pydantic expects dict but we pass a sqlalchemy model
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
