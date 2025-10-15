from typing import Optional
from pydantic import BaseModel, Field

class Book():
    id : int 
    title : str
    author : str 
    description : str
    rating : int
    published_date: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
        

class BookRequest(BaseModel):
    id : Optional[int] = Field(description="ID is not needed on create", default=None) # optional id field
    title : str =Field(min_length=3)
    author : str = Field(min_length=3)
    description : str = Field(min_length=5, max_length=100)
    rating : int = Field(gt=-1, lt=6)
    published_date: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A novel set in the Roaring Twenties, exploring themes of decadence, idealism, and excess.",
                "rating": 5,
                "published_date": 2012
            }
        }
    }