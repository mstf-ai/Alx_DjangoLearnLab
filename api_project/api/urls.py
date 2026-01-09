from django.urls import path
from .views import BookList  # استيراد View الصحيح

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # رابط GET لقائمة الكتب
]
