from django.urls import path
from . import views
from .views import  asistencia_estudiante



urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
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
    path('estudiante/asistencia/<int:estudiante_id>/', asistencia_estudiante, name='asistencia-estudiante'),
    path('aulas/delete/<int:pk>/', views.aula_delete, name='aula_delete'),
    path('aulas/update/<int:pk>/', views.aula_update, name='aula_update'),
    path('aulas/<int:aula_id>/estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:estudiante_id>/tomar_asistencia/', views.tomar_asistencia, name='tomar_asistencia'),
    path('estudiantes/<int:estudiante_id>/registrar_calificacion/', views.registrar_calificacion, name='registrar_calificacion'),
    path('estudiantes/create/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/delete/<int:pk>/', views.estudiante_delete, name='estudiante_delete'),
    path('estudiantes/update/<int:pk>/', views.estudiante_update, name='estudiante_update'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('crear-equipo/', views.equipo_create, name='crear_equipo'),
    path('actualizar-equipo/<int:pk>/', views.actualizar_equipo, name='actualizar_equipo'),
    path('eliminar-equipo/<int:pk>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('proyectos/<int:equipo_id>/', views.lista_proyectos, name='lista_proyectos'),
    path('crear-proyecto/<int:equipo_id>/', views.proyecto_create, name='proyecto_create'),
    path('actualizar-proyecto/<int:pk>/', views.proyecto_update, name='proyecto_update'),
    path('eliminar-proyecto/<int:pk>/', views.proyecto_delete, name='proyecto_delete'),
    path('archivos/<int:proyecto_id>/', views.lista_archivos, name='lista_archivos'),
    path('actualizar-archivo/<int:pk>/', views.archivo_update, name='archivo_update'),
    path('eliminar-archivo/<int:pk>/', views.archivo_delete, name='archivo_delete'),
    path('cargar_archivo/<int:proyecto_id>/', views.cargar_archivo, name='cargar_archivo'),
    path('descargar_archivo/<int:archivo_id>/', views.descargar_archivo, name='descargar_archivo'),
    path('descargar_confirmado/<int:archivo_id>/', views.descargar_confirmado, name='confirmar_descarga'),

    ]


