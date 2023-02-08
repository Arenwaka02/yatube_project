from django.shortcuts import HttpResponse
# Импортируем загрузчик.
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group': group,
    }
    return render(request, template, context)
