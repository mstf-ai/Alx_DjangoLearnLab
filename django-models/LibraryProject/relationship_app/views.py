from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  # << مهم جداً
from django.views.generic.detail import DetailView

from .models import Book, Library


# -----------------------------
# Function-based view
# List all books
# -----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(
        request,
        "relationship_app/list_books.html",
        {"books": books}
    )


# -----------------------------
# Class-based view
# Library details
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# -----------------------------
# Authentication views
# -----------------------------
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # << سجل المستخدم مباشرة بعد التسجيل
            return redirect("list_books")  # أو أي صفحة تريد تحويل المستخدم إليها
    else:
        form = UserCreationForm()

    return render(
        request,
        "relationship_app/register.html",
        {"form": form}
    )
