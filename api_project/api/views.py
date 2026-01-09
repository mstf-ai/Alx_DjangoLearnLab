from rest_framework import generics  # استيراد generics
from .models import Book
from .serializers import BookSerializer

# تعريف الـ API View بالاسم المطلوب بالضبط
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # كل الكتب
    serializer_class = BookSerializer
