from pydantic import BaseModel

class Book():
    id : str 
    title : str
    author : str 
    description : str
    rating : int

    def __init__(self, id: str, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id : str 
    title : str
    author : str 
    description : str
    rating : int