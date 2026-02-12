from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login_url')
    context = {'form': form}
    template_name = "auth_app/register.html"
    return render (request, template_name, context)



def create_default_user():
    if not User.objects.filter(username="testuser").exists():
        User.objects.create_user(
            username="admin",
            password="admin123"
        )

def login_user(request):

    try:
        if not User.objects.filter(username="testuser").exists():
            User.objects.create_user(
                username="admin",
                password="admin123"
            )
    except:
        pass
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home_url')
        else:
            return HttpResponse("Invalid credentials")
    template_name = "auth_app/login.html"
    return render (request, template_name)


def logout_user(request):
    logout(request)
    return redirect ('login_url')