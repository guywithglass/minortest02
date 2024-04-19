from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sample(request):
    return render(request, 'sample.html')
