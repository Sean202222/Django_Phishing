from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def recc(request):
    return render(request, 'recc.html', {})

def phish1(request):
    return render(request, 'phish1.html', {})

def phish1a(request):
    return render(request, 'phish1a.html', {})

def phish1b(request):
    return render(request, 'phish1b.html', {})

def phish1c(request):
    return render(request, 'phish1c.html', {})

def phish2(request):
    return render(request, 'phish2.html', {})

def phish3(request):
    return render(request, 'phish3.html', {})
# Create your views here.
