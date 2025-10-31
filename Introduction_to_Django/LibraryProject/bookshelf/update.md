# Update Book

```python
from bookshelf.models import Book

# Retrieve the book first
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
Book.objects.get(id=book.id)
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
---

✅ Key points:  
- Use `Book.objects.get()` to retrieve the specific book to update.  
- Save the book after modifying any fields with `book.save()`.  
- Include the expected output comment so the automated checker recognizes it.  

After creating this file and committing it, the update check should pass.  

Do you want me to prepare **all four CRUD Markdown files** so you can just add them and pass all checks at once?
