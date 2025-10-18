
from fastapi import Body,APIRouter, HTTPException
from data.data import books
from starlette import status

router = APIRouter()

# Simple test endpoint
# Delete is the method used to remove existing resources on the server
# Data is typically sent in the request body in formats like JSON
# Example: Deleting an existing book entry
@router.delete("/books/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    book_changed = False
    for idx, b in enumerate(books):
        if b.id == book_id:
            books.remove(b)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully", "book_id": book_id}