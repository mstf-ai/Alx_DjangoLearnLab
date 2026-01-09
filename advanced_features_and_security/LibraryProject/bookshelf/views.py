from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookForm


@csrf_protect
def book_list(request):
    books = Book.objects.all()  # Safe ORM usage
    response = render(request, 'bookshelf/book_list.html', {'books': books})

    # Manual CSP Header
    response['Content-Security-Policy'] = "default-src 'self'"
    return response


@csrf_protect
def form_example(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    response = render(request, 'bookshelf/form_example.html', {'form': form})
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
