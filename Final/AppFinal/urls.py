from django.urls import path

from AppFinal import views


urlpatterns = [
    path('', views.inicio, name="Inicio" ),
    path('personal/', views.personal, name= "Personal" ),
    path('especialidad/', views.especialidad, name = "Especialidad" ),
    path('equipoTrabajo/', views.equipo_trabajo, name = "EquipoTrabajo" ),
    path('busquedaPersonal/', views.busquedaPersonal, name= "BusquedaPersonal" ),
    path('busquedaEspecialidad/', views.busquedaEspecialidad, name= "BusquedaEspecialidad" ),
    path('busquedaEquipo/', views.busquedaEquipo, name= "BusquedaEquipo" ),
    path('buscar/', views.buscar, name= "Buscar" ),
    path('buscar_especialidad/', views.buscar_especialidad, name= "BuscarEspecialidad" ),
    path('buscar_equipo/', views.buscar_equipo, name= "BuscarEquipo" ),

    ]