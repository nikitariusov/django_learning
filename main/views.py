from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME"
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cupiditate obcaecati accusamus explicabo. Nesciunt, architecto.'
    }
    
    return render(request, 'main/about.html', context)