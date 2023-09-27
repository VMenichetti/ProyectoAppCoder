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
    path('listaProfesores/', listaProfesores, name="ListaProfesores"),
    path('creaProfesores/', crea_profesor, name="CreaProfesores"),  
    path('eliminarProfesor/<int:id>', eliminar_profesor, name="EliminarProfesores"),
    path('editarProfesor/<int:id>', editar_profesor, name="EditarProfesor"),
    path('listaCursos/', CursoList.as_view(), name="ListarCursos"),
    path('detalleCurso/<pk>/', CursoDetail.as_view(), name="DetalleCurso"),
    path('creaCurso/', CursoCreate.as_view(), name="CrearCurso"),
    path('actualizarCurso/<pk>/', CursoUpdate.as_view(), name="ActualizarCurso"),
    path('eliminarCurso/<pk>/', CursoDelete.as_view(), name="EliminarCurso"),
] 