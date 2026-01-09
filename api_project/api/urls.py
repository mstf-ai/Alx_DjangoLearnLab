from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# إعداد Router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Endpoint سابق للقائمة فقط
    path('books/', BookList.as_view(), name='book-list'),

    # جميع مسارات CRUD الخاصة بالـ ViewSet
    path('', include(router.urls)),
]
