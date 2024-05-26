from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница сайта',
        'list': ['nasos', 'smesitel'],
        'dict': {'usd': 40, 'uah': 34},
        'bool': True,
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('<h1>About page</h1>')