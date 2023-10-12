from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('forums/', views.forum_list, name='forum_list'),
    path('forums/create/', views.forum_create, name='forum_create'),
    path('forums/update/<int:pk>/', views.forum_update, name='forum_update'),
    path('forums/delete/<int:pk>/', views.forum_delete, name='forum_delete'),
    path('forums/<int:forum_id>/', views.chat_detail, name='chat_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('aulas/', views.lista_aulas, name='aulas'),
    path('aulas/<int:aula_id>/estudiantes/<int:estudiante_id>/notas/', views.notas_estudiante_por_aula, name='notas_estudiante_por_aula'),
    path('aulas/create/', views.aula_create, name='aula_create'),
    path('aulas/delete/<int:pk>/', views.aula_delete, name='aula_delete'),
    path('aulas/update/<int:pk>/', views.aula_update, name='aula_update'),
    path('aulas/<int:aula_id>/estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:estudiante_id>/tomar_asistencia/', views.tomar_asistencia, name='tomar_asistencia'),
    path('estudiantes/<int:estudiante_id>/registrar_calificacion/', views.registrar_calificacion, name='registrar_calificacion'),
    path('estudiantes/create/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/delete/<int:pk>/', views.estudiante_delete, name='estudiante_delete'),
    path('estudiantes/update/<int:pk>/', views.estudiante_update, name='estudiante_update')
    ]

