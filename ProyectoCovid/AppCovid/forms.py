from django import forms

class BarbijosFormulario(forms.Form):

    marca= forms.CharField(max_length=40)
    tamanio= forms.CharField(max_length=40)
    precio = forms.IntegerField(required=True)
