from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

# Create your views here.

def curso(req,nombre,camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse (f"""
       <p>Curso: {curso.nombre} - Camada: {curso.camada} creado con éxito!</p>
        
        """)

#  Crear funcionalidad para recuperar el listado de cursos que tenemos en nuestra BD
    
def listar_cursos(req):

    lista = Curso.objects.all()
        
    return render(req,"lista_cursos.html", {"lista_cursos":lista})

def inicio(req):
    return render(req, "inicio.html")

def cursos(req):
    return render(req, "cursos.html")

def profesores(req):
    return render(req, "profesores.html")

def estudiantes(req):
    return render(req, "estudiantes.html")

def entregables(req):
    return render(req, "entregables.html")

# FORMULARIO

def cursoFormulario(req):
    print('method', req.method)
    print ('POST',req.POST)
    
    if req.method == 'POST':
        miFormulario=CursoFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data   
            curso = Curso(nombre=data['curso'], camada=data['camada'])
            curso.save()

        return render(req, "inicio.html")
    else:
        miFormulario=CursoFormulario()
        return render(req, "cursoFormulario.html",{"miFormulario":miFormulario})
    
# BUSQUEDA
def busquedaCamada(req):
    return render(req, "busquedaCamada.html") 

def buscar(req:HttpRequest):

    if req.GET["camada"]:
        camada=req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(req,"resultadosBusqueda.html",{"cursos":cursos})
    else:
         return HttpResponse(f"Debe agregar una camada")

# PROFESORES

def listaProfesores(req):

    profesores=Profesor.objects.all() 
    return render(req,"listaProfesores.html",{"profesores":profesores})

# Función de Registro/Creación

def crea_profesor(req):

    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save() 

            return render(req, "inicio.html")
    else:
        miFormulario = ProfesorFormulario()
        return render(req, "profesorFormulario.html", {"miFormulario": miFormulario})
    
# Función Eliminar

def eliminar_profesor(req, id):

    if req.method == 'POST':

        profesor = Profesor.objects.get(id=id)
        profesor.delete()

        profesores = Profesor.objects.all()

        return render(req, "listaProfesores.html", {"profesores": profesores})
    
# Función Editar
    
def editar_profesor(req, id):

    profesor = Profesor.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]
            profesor.save()

            return render(req, "inicio.html")
    else:

        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion,
        })
        return render(req, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})
    
# VISTAS basadas en clases

class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"
    context_object_name = "cursos"


class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail.html"
    context_object_name = "curso"

class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields = ['nombre', 'camada']
    success_url = '/app-coder/'

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    fields = ('nombre', 'camada')
    success_url = '/app-coder/listaCursos'
    context_object_name = "curso"

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = '/app-coder/listaCursos'
    context_object_name = "curso"