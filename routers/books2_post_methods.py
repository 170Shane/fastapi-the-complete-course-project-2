from fastapi import APIRouter, Body
from models.book import Book, BookRequest
from data.data import books
from starlette import status
router = APIRouter()


@router.post("/create_book/", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append(find_book_index(new_book)) 
    return {"message": "Book created successfully", "book": new_book}

def find_book_index(book: Book):
    # if len(books) == 0:
    #     book.id = 1
    # else:
    #     book.id = max(int(book.id) for book in books) + 1 if books else 0     # select maximum id from books and increment by 1

    book.id = 1 if len(books) == 0 else max(int(book.id) for book in books) + 1

    return book
