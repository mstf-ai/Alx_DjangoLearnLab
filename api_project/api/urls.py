from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# إعداد Router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Endpoint لقائمة الكتب فقط
    path('books/', BookList.as_view(), name='book-list'),

    # Endpoint للحصول على توكن
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # مسارات CRUD عبر Router
    path('', include(router.urls)),
]
