from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Подробная ифно о группе
    path('group/<slug:slug>/', views.group_posts),
]