from fastapi import APIRouter, Body
from models.book import Book
from data.data import books
router = APIRouter()


@router.post("/create_book/", response_model=Book)
async def create_book(book_request: Book):
    books.append(book_request)
    return book_request