from django.urls import path
from . import views

urlpatterns= [
    path('', views.index),
    path('about/', views.about),
    path('hola/<str:username>', views.hola),
    path('projecto/', views.projects),
    path('tareas/<str:titulo>', views.tareas),

]