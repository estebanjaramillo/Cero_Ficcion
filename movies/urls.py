from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('forums/', views.forum_list, name='forum_list'),
    path('forums/<int:forum_id>/', views.chat_detail, name='chat_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('aulas/', views.lista_aulas, name='lista_aulas'),
    path('aulas/<int:aula_id>/estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:estudiante_id>/tomar_asistencia/', views.tomar_asistencia, name='tomar_asistencia'),
    path('estudiantes/<int:estudiante_id>/registrar_calificacion/', views.registrar_calificacion, name='registrar_calificacion'),
    path('aulas/<int:aula_id>/estudiantes/<int:estudiante_id>/notas/', views.notas_estudiante_por_aula, name='notas_estudiante_por_aula'),
    ]

