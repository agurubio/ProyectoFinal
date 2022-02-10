from django.urls import path

from AppFinal import views


urlpatterns = [
    path('', views.inicio, name="Inicio" ),
    path('personal/', views.personal, name= "Personal" ),
    path('especialidad/', views.especialidad, name = "Especialidad" ),
    path('equipoTrabajo/', views.equipo_trabajo, name = "Equipo_Trabajo" ),

]