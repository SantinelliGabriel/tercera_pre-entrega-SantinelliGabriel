from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tareas/', views.tasks, name="tasks"),
    path('entregar_tareas/', views.create_task, name="create_task"),
    path('registrar/', views.create_project, name="create_project"),
]