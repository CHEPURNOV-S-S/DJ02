from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def news(request):
    return render(request, 'pages/news.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')