CRUD Operations on Book Model

1\. Create

from bookshelf.models import Book



\# Create a new Book

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book

\# Expected output:

\# <Book: 1984 by George Orwell (1949)>



2\. Retrieve

\# Retrieve all books

Book.objects.all()

\# Expected output:

\# <QuerySet \[<Book: 1984 by George Orwell (1949)>]>



3\. Update

\# Update the title

book.title = "Nineteen Eighty-Four"

book.save()



\# Verify update

Book.objects.all()

\# Expected output:

\# <QuerySet \[<Book: Nineteen Eighty-Four by George Orwell (1949)>]>



4\. Delete

\# Delete the book

book.delete()

\# Output:

\# (1, {'bookshelf.Book': 1})



\# Verify deletion

Book.objects.all()

\# Expected output:

\# <QuerySet \[]>

