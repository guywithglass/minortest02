from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    current_user = request.user
    user_name = current_user.username
    print(user_name)
    return render(request, 'index.html')


def sample(request):
    return render(request, 'sample.html')


def sam(request):
    return render(request, 'sam.html')


def base(request):
    return render(request, 'base.html')


# def contact(request):
#     return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == "POST":
        username = request.POST['uname']
        email = request.POST['email']
        first_name = request.POST['fname']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            return redirect('register')
        else:
            user = User.objects.create_user(
                first_name=first_name, email=email, username=username, password=password)
            user.save()
            print("User Created")
            return redirect('index')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            print("User")
            # return redirect('login')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('index')
