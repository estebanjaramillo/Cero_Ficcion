from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('login/', views.login, name='login'),
]