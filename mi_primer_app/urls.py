
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('Hola-Mundo/', views.hola_mundo, name='hola_mundo'),
    path('crear-familiar/<str:nombre>/', views.crear_familiar, name='crear-familiar'),
    path("listar-familiares/", views.listar_familiares, name="listar_familiares"),
    path("crear-curso/", 
         views.crear_curso, name="crear_curso"),
    path("listar-cursos/", 
         views.listar_cursos, name="listar_cursos"),
    path('cursos/buscar', 
         views.buscar_cursos, name='buscar_cursos'),
    path('crear-estudiante/', 
         views.crear_estudiante, name='crear_estudiante'),
    path('listar-estudiantes/', 
         views.listar_estudiantes, name='listar_estudiantes'),
]
