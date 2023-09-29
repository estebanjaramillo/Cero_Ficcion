from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('login/', views.login, name='login'),
    path('base/', views.base, name='base'),
    path('login_view/', views.login_view, name='login_view'),
    path('forums/', views.forum_list, name='forum_list'),
    path('forums/<int:forum_id>/', views.chat_detail, name='chat_detail'),
]
