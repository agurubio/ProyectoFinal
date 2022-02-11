from django.http import HttpResponse
from django.shortcuts import render

from AppFinal.models import Personal
from AppFinal.forms import PersonalFormulario


# Create your views here.

def inicio(request):
    return render(request, 'Final/inicio.html')

def personal(request):
    return render(request, 'Final/personal.html')

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
    return render(request, 'Final/especialidad.html')

def equipo_trabajo(request):
    return render(request, 'Final/equipo_trabajo.html')

def busquedaPersonal(request):
    return render(request, 'Final/busquedaPersonal.html')

def buscar(request):
    
    if request.GET['persona']:
        legajo = request.GET['persona']
        persona = Personal.objects.filter(legajo__icontains=legajo)

        return render(request, 'Final/resultadoBusqueda.html', {"persona":persona, "legajo":legajo} )
   
    else:
        respuesta = "Ningun dato solicitado"
    
    return HttpResponse(respuesta)
