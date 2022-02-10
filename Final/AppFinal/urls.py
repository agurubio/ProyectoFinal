from django.urls import path

from AppFinal import views


urlpatterns = [
    path('', views.inicio ),
    path('personal/', views.personal ),
    path('especialidad/', views.especialidad ),
    path('equipoTrabajo/', views.equipo_trabajo ),

]