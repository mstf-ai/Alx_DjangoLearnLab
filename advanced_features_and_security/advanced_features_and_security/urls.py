from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', user_views.home, name='home'),  # هذا المسار للجذر
]
