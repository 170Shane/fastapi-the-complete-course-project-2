
from fastapi import Body,APIRouter
from data.data import books

router = APIRouter()

# Simple test endpoint
# Delete is the method used to remove existing resources on the server
# Data is typically sent in the request body in formats like JSON
# Example: Deleting an existing book entry
@router.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int):
    for idx, b in enumerate(books):
        if b.id == book_id:
            books.remove(b)
            print(books)
            break            
    return {"message": "Book not found"}
    
    
        