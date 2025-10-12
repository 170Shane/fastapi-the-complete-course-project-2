from typing import Optional
from pydantic import BaseModel, Field

class Book():
    id : int 
    title : str
    author : str 
    description : str
    rating : int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id : Optional[int] = None # optional id field
    title : str =Field(min_length=3)
    author : str = Field(min_length=3)
    description : str = Field(min_length=5, max_length=100)
    rating : int = Field(gt=-1, lt=6)