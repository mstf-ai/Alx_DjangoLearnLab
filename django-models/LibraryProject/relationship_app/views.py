from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view (PLAIN TEXT)
def list_books(request):
    books = Book.objects.all()
    output = []

    for book in books:
        output.append(f"{book.title} by {book.author.name}")

    return HttpResponse("\n".join(output))


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
