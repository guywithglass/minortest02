from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sample(request):
    return render(request, 'sample.html')


def base(request):
    return render(request, 'base.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
