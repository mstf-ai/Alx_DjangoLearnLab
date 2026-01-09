from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# ListAPIView فقط لعرض قائمة الكتب
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# ViewSet كامل للـ CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
