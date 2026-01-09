# LibraryProject/relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian

def sample_queries():
    # -------------------------------
    # Query all books by a specific author
    # -------------------------------
    author_name = "Author 1"  # ضع اسم مؤلف موجود في قاعدة البيانات
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

    # -------------------------------
    # List all books in a library
    # -------------------------------
    library_name = "Central Library"  # ضع اسم مكتبة موجودة
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in library {library.name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

    # -------------------------------
    # Retrieve the librarian for a library
    # -------------------------------
    try:
        librarian = Librarian.objects.get(library=library)  # استخدم كائن Library مباشرة
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to {library.name}")
