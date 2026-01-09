from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import ExampleForm


@csrf_protect
def book_list(request):
    books = Book.objects.all()
    response = render(request, 'bookshelf/book_list.html', {'books': books})
    response['Content-Security-Policy'] = "default-src 'self'"
    return response


@csrf_protect
def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()

    response = render(request, 'bookshelf/form_example.html', {'form': form})
    response['Content-Security-Policy'] = "default-src 'self'"
    return response
