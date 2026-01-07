from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# صفحة تسجيل المستخدم
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

# صفحة تسجيل الخروج
@login_required
def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")

# الصفحة الرئيسية للمشروع
@login_required
def home(request):
    return render(request, "users/home.html")
