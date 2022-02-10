from django.contrib import admin

from AppFinal.models import EquipoTrabajo, Especialidad, Personal

# Register your models here.

admin.site.register(Personal)

admin.site.register(Especialidad)

admin.site.register(EquipoTrabajo)