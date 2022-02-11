from django import forms

class PersonalFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    legajo = forms.IntegerField()