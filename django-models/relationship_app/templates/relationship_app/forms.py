from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # اختر الحقول التي تريد أن يظهرها في النموذج
        fields = ["title", "author", "publication_year", "library"]
