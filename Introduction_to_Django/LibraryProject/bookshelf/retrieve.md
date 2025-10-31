# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(title="1984")
book
# Expected output: <Book: 1984 by George Orwell (1949)>
---

✅ Notes:  
- `Book.objects.get()` retrieves a single object that matches the query.  
- Make sure the title matches exactly what you used when creating the book.  

You should update your `retrieve.md` with this content and commit it.  

If you want, I can also generate **all four Markdown files** (`create.md`, `retrieve.md`, `update.md`, `delete.md`) in the exact format required for ALX. This ensures all CRUD checks pass at once. Do you want me to do that?
