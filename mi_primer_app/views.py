from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Familiar
from .models import Curso, Estudiante
from .forms import CursoForm, EstudianteForm


# Create your views here.

def home(request):
    return render(request, 'mi_primer_app/home.html')

def hola_mundo(request):
    print("¡Hola, Mundo!")
    return HttpResponse("¡Hola, Mundo!")

def crear_familiar(request, nombre):
    if nombre is not None:
        Familiar.objects.create(
            nombre=nombre, edad=30, parentesco='Hermano', fecha_nacimiento='1993-01-01')
    return render(request, 'mi_primer_app/crear-familiar.html', {"familiar": nombre})

def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'mi_primer_app/listar_familiares.html', {"familiares": familiares})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_fin=form.cleaned_data['fecha_fin'],
                activo=form.cleaned_data['activo']
            )
            curso.save()
            return redirect("listar_cursos")
    
    form = CursoForm()
    return render(request, 'mi_primer_app/crear-curso.html', {"form": form})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos})


def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos, "nombre": nombre})
    

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
            )
            estudiante.save()
            return redirect("listar_estudiantes")
    else:
        form = EstudianteForm()
    return render(request, 'mi_primer_app/crear-estudiante.html', {"form": form})


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_primer_app/listar-estudiantes.html', {"estudiantes": estudiantes})