from django.urls import path

from AppFinal import views


urlpatterns = [
    path('', views.inicio, name="Inicio" ),
    path('personal/', views.personal, name= "Personal" ),
    path('especialidad/', views.especialidad, name = "Especialidad" ),
    path('equipoTrabajo/', views.equipo_trabajo, name = "EquipoTrabajo" ),
    path('personalFormulario/', views.personalFormulario, name= "PersonalFormulario" ),
    path('busquedaPersonal/', views.busquedaPersonal, name= "BusquedaPersonal" ),
    path('buscar/', views.buscar, name= "Buscar" ),
    ]