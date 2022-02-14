from django.http import HttpResponse
from django.shortcuts import render

from AppFinal.models import Personal
from AppFinal.forms import PersonalFormulario, EspecialidadFormulario, EquipoFormulario
from AppFinal.models import Especialidad, EquipoTrabajo



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

def personalFormulario(request):
    
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
    return render(request, 'Final/personalFormulario.html', {"miFormulario":miFormulario})
    #return render(request, 'Final/personalFormulario.html')

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
    miFormulario = EquipoFormulario()
    if request.method == 'POST':

        miFormulario = EquipoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            equipo = EquipoTrabajo(equipo=informacion['equipo'], responsable=informacion['responsable'])
            
            equipo.save()
            
            return render(request, 'Final/inicio.html')

        else:
            miFormulario=EquipoFormulario()
    return render(request, 'Final/equipo_trabajo.html', {"miFormulario":miFormulario})
    
    
def busquedaPersonal(request):
    return render(request, 'Final/busquedaPersonal.html')

def busquedaEspecialidad(request):
    return render(request, 'Final/busquedaEspecialidad.html')

def busquedaEquipo(request):
    return render(request, 'Final/busquedaEquipo.html')

def buscar(request):
    
    if request.GET['persona']:
        legajo = request.GET['persona']
        persona = Personal.objects.filter(legajo__icontains=legajo)

        return render(request, 'Final/personal.html', {"persona":persona, "legajo":legajo} )
 
    else:
        respuesta = "Ningun dato solicitado"
    
    return render(request, 'Final/personal.html', {"respuesta":respuesta})

def buscar_especialidad(request):
    if request.GET['nombre']:
        especialidad_nombre = request.GET['nombre']
        especialidad = Especialidad.objects.filter(especialidad__icontains=especialidad_nombre)

        return render(request, 'Final/especialidad.html', {"especialidad_nombre":especialidad_nombre, "especialidad":especialidad} )
    
    else:
        respuesta = "Ningun dato solicitado"
    
    return render(request, 'Final/especialidad.html', {"respuesta":respuesta})

def buscar_equipo(request):
    
    if request.GET['nombre']:
        equipo_nombre = request.GET['nombre']
        equipo = EquipoTrabajo.objects.filter(equipo__icontains=equipo_nombre)

        return render(request, 'Final/equipo_trabajo.html', {"equipo_nombre":equipo_nombre, "equipo":equipo} )
    
    else:
        respuesta = "Ningun dato solicitado"
    
    return render(request, 'Final/equipo_trabajo.html', {"respuesta":respuesta})