from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# API View لقائمة الكتب فقط
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet كامل للـ CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle CRUD operations for Book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
