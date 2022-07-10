from pydantic import BaseModel

# The pydanctic model / schema that defines the structure of a request & response
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass
