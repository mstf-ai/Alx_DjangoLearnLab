# Create Book

```python
from bookshelf.models import Book

# Create a new Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected output:
# <Book: 1984 by George Orwell (1949)>

---

### **2️⃣ Create `retrieve.md`**
**Path:** `LibraryProject/bookshelf/retrieve.md`  
**Content:**
```markdown
# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# Expected output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

---

### **3️⃣ Create `update.md`**
**Path:** `LibraryProject/bookshelf/update.md`  
**Content:**
```markdown
# Update Book

```python
from bookshelf.models import Book

# Update the title of the book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
Book.objects.all()
# Expected output:
# <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>

---

### **4️⃣ Create `delete.md`**
**Path:** `LibraryProject/bookshelf/delete.md`  
**Content:**
```markdown
# Delete Book

```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Output:
# (1, {'bookshelf.Book': 1})

# Verify deletion
Book.objects.all()
# Expected output:
# <QuerySet []>

---

Once you create these 4 files in `LibraryProject/bookshelf/`, the automated checks should pass.  

If you want, I can **write a single command sequence to quickly create all 4 files with the correct content** so you don’t have to do it manually. Do you want me to do that?
