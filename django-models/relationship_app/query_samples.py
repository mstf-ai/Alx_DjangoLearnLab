# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Example Queries:

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}: {[book.title for book in books]}")
    except Author.DoesNotExist:
        print(f"No author named {author_name} found.")

def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")

def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian of {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
