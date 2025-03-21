from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Curso

# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    #cursosListados = Curso.objects.all()[:5]
    #cursosListados = Curso.objects.all()[4:9]
    #cursosListados = Curso.objects.all().order_by('nombre')
    #cursosListados = Curso.objects.all().order_by('-nombre')
    #cursosListados = Curso.objects.all().order_by('nombre','creditos')
    #cursosListados = Curso.objects.filter(nombre='Historia',creditos=4)
    #cursosListados = Curso.objects.filter(creditos__lte=4)
    #cursosListados = Curso.objects.filter(nombre__startswith='Q')
    #cursosListados = Curso.objects.filter(nombre__contains='g')

    data = {
        'titulo': 'Gestion de Cursos',
        'cursos': cursosListados
    }
    return render(request, 'gestionCursos.html', data)

class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        return Curso.objects.filter(creditos__lte=4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Cursos'
        return context
    
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/')

def registrar_curso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    curso = Curso.objects.create(nombre=nombre, creditos=creditos)
    return redirect('/')

def edicion_curso(request, id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo': 'Edicion de Curso',
        'curso': curso
    }

    return render(request, 'edicionCursos.html', data)

def editar_curso(request):
    id = int(request.POST['txtId'])
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    
    curso.save()

    return redirect('/')