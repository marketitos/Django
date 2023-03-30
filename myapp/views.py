from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, tareas
from django.shortcuts import render, redirect
from .forms import crearnuevatarea, crearproyecto


# Create your views here.

def hola(request, username):
    return HttpResponse("<h2>Hola mundo %s</h2>" % username)
    print(username)
    
def about(request):
    return render(request, "about.html")

def index(request):
    titulo= "Bienvenido pedazo de locura!"
    return render(request, "index.html", {
        "titulo":titulo
    })

def projects(request):
    #projects= list(Project.objects.values())
    projects= Project.objects.all()
    return render(request, "projects.html", {
        "projects": projects
    })

def task(request):
    tarea = tareas.objects.all()
    return render(request, "tareas.html", {
        "tareas":tarea
    })


def crear_tarea(request):
    if request.method == 'GET':
            return render(request, 'Crear_tarear.html', {
            "form":crearnuevatarea()
        })
    else:
         tareas.objects.create(titulo = request.POST['titulo'], descripcion = request.POST['descripcion'], project_id=1)
         return redirect('/tareas')


def crear_proyecto(request):
    if request == 'GET':
        return render(request, 'crear_proyectos.html' , {
            "form":crearproyecto()
        })
    else: 
        project = Project.objects.create(name=request.POST["name"])
        print(project)
        return render(request, 'crear_proyectos.html' , {
            "form":crearproyecto()
        })
        






    


