from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion= models.CharField(max_length=300)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo + " - " + self.project.name
