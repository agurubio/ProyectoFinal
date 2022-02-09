from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
	return HttpResponse('Hola Django - Coder')

def inicio(request):
    return render(request, 'Final/inicio.html')