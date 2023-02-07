from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список групп
    path('group/', views.group_posts_list),
    # Подробная ифно о группе
    path('group/<slug:slug>/', views.group_posts),
]