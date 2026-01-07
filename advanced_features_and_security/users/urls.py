from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # الصفحة الرئيسية
    path('register/', views.register, name='register'),  # تسجيل مستخدم جديد
    path('login/', views.user_login, name='login'),      # تسجيل الدخول
    path('logout/', views.user_logout, name='logout'),   # تسجيل الخروج
]
