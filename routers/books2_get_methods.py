from fastapi import APIRouter
from models.book import Book
from data.data import books

router = APIRouter()

# Simple test endpoint
@router.get("/test")
async def read_root():
    #return {"Hello": "World"}
    return "This is a test endpoint from the books2 router."

# Get all books
@router.get("/books")
async def get_books():
    return books

# Get book titles
@router.get("/books/titles")
async def get_book_titles():
    return [book.title for book in books]