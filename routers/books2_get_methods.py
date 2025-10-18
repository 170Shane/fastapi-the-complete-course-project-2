from fastapi import APIRouter, Path, Query
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

# Get a book by ID using path parameter
@router.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

# Get books by rating using query parameter
@router.get("/books/by_rating/")
async def get_books_by_rating(rating: int):
    filtered_books = [book for book in books if book.rating >= rating]
    if filtered_books:
        return filtered_books
    return {"error": f"No books found with a rating of {rating} or higher"}

# Get books by published year using query parameter
@router.get("/books/by_year/")
async def get_books_by_year(published_date: int):
    filtered_books = [book for book in books if book.published_date == published_date]
    if filtered_books:
        return filtered_books
    return {"error": f"No books found published in the year {published_date}"}

# Data validation using path parameters using Path
# Path is a way to declare additional metadata and validation rules for path parameters
@router.get("/books/validated/{book_id}")
async def get_book_validated(book_id: int = Path(..., description="The ID of the book to get", gt=0, lt=100)):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

# Data validation using query parameters using Query
# Query is a way to declare additional metadata and validation rules for query parameters
@router.get("/books/validated/by_rating/")
async def get_books_by_rating_validated(rating: int = Query(..., description="The minimum rating of the books to get", gt=0, lt=6)):
    filtered_books = [book for book in books if book.rating >= rating]
    if filtered_books:
        return filtered_books
    return {"error": f"No books found with a rating of {rating} or higher"}


