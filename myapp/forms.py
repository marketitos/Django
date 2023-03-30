from cProfile import label
from django import forms

class crearnuevatarea(forms.Form):
    titulo = forms.CharField(label="Titulo de tarea", max_length=200)
    descripcion =forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea)


class crearproyecto(forms.Form):
    name = forms.CharField(label="Titulo del proyecto", max_length=200)