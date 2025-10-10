from fastapi import APIRouter, Body
from models.book import Book, BookRequest
from data.data import books
router = APIRouter()


@router.post("/create_book/")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}