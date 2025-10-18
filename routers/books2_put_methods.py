
from fastapi import Body,APIRouter, HTTPException
from models import book
from models.book import Book, BookRequest
from data.data import books

router = APIRouter()

# Simple test endpoint
# Put is the method used to update existing resources on the server
# Data is typically sent in the request body in formats like JSON
# Example: Updating an existing book entry
@router.put("/books/update_book/")
async def update_book(book: BookRequest):
    book_changed = False
    for idx, b in enumerate(books):        
            if b.id == book.id:
                books[idx] = book                
                book_changed = True            
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")
