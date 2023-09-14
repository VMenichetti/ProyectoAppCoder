from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/',listar_cursos, name='ListaCursos'),
    path('',inicio,name="inicio"),
    path('cursos/',cursos, name="cursos"),
    path('profesores/',profesores, name="profesores"),
    path('estudiantes/',estudiantes, name="estudiantes"),
    path('entregables/',entregables, name="entregables"),
    path('curso-formulario/',cursoFormulario, name="CursoFormulario"),
    path('busqueda-camada/',busquedaCamada, name="BusquedaCamada"),
    path('buscar/',buscar, name="Buscar"),   
] 