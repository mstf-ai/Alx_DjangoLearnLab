# LibraryProject/relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian

def sample_queries():
    # -------------------------------
    # Query all books by a specific author
    # -------------------------------
    author = Author.objects.first()  # مثال: أخذ أول مؤلف
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")

    # -------------------------------
    # List all books in a library
    # -------------------------------
    library = Library.objects.first()  # مثال: أول مكتبة
    books_in_library = library.books.all()  # ManyToMany relation
    print(f"\nBooks in library {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")

    # -------------------------------
    # Retrieve the librarian for a library
    # -------------------------------
    try:
        librarian = Librarian.objects.get(library=library)  # OneToOne relation
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to {library.name}")
