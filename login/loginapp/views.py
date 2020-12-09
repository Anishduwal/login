from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print("login succeed")
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('/')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist')
            else:
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password)
                user.save()
                print('User added successfully')
                return redirect('login')
        else:
            messages.error(request, 'Password not matching')
    return render(request, 'register.html')
    
def signout(request):
    return redirect('/')