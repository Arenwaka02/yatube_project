from django.shortcuts import HttpResponse
# Импортируем загрузчик.
from django.shortcuts import render

# Create your views here.
def index(request, template):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(requests, slug):
    return HttpResponse(f'Посты {slug}')


def group_posts_list(requests):
    return HttpResponse('Посты')
