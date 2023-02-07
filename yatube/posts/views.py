
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


def group_posts(requests, slug):
    return HttpResponse(f'Посты {slug}')


def group_posts_list(requests):
    return HttpResponse('Посты')
