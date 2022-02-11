from django.shortcuts import render

from AppFinal.models import Personal
from AppFinal.forms import PersonalFormulario, EspecialidadFormulario
from AppFinal.models import Especialidad


# Create your views here.

def inicio(request):
    return render(request, 'Final/inicio.html')

def personal(request):
    
    miFormulario = PersonalFormulario()
    if request.method == 'POST':

        miFormulario = PersonalFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            personal = Personal(nombre=informacion['nombre'], apellido=informacion['apellido'], legajo=informacion['legajo'])
            
            personal.save()
            
            return render(request, 'Final/inicio.html')

        else:
            miFormulario=PersonalFormulario()
    return render(request, 'Final/personal.html', {"miFormulario":miFormulario})

def especialidad(request):
    miFormulario = EspecialidadFormulario()
    if request.method == 'POST':

        miFormulario = EspecialidadFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            especialidad = Especialidad(nombre=informacion['especialidad'], activo=informacion['esp_activa'])
            
            especialidad.save()
            
            return render(request, 'Final/inicio.html')

        else:
            miFormulario=EspecialidadFormulario()       
    return render(request, 'Final/especialidad.html', {"miFormulario":miFormulario})


def equipo_trabajo(request):
    return render(request, 'Final/equipo_trabajo.html')

def busquedaPersonal(request):
    return render(request, 'Final/busquedaPersonal.html')

def buscar(request):
    
    if request.GET['persona']:
        legajo = request.GET['persona']
        persona = Personal.objects.filter(legajo__icontains=legajo)

        return render(request, 'Final/personal.html', {"persona":persona, "legajo":legajo} )
    
    else:
        respuesta = "Ningun dato solicitado"
    
    return render(request, 'Final/personal.html', {"respuesta":respuesta})
