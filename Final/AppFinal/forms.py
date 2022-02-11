from django import forms

class PersonalFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    legajo = forms.IntegerField()

class EspecialidadFormulario(forms.Form):
    especialidad = forms.CharField(max_length=30)
    esp_activa = forms.BooleanField()