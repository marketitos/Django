from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, tareas
from django.shortcuts import render


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

def task(request, ):
    tarea = tareas.objects.get(titulo=titulo)
    return render(request, "tareas.html")

