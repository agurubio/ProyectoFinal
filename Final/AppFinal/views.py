from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'Final/inicio.html')

def personal(request):
    return render(request, 'Final/personal.html')

def especialidad(request):
    return render(request, 'Final/especialidad.html')

def equipo_trabajo(request):
    return render(request, 'Final/equipo_trabajo.html')
