from django.shortcuts import render
from django.http import HttpResponse

from AppCovid.models import Guantes, Barbijos, Oximetros
from AppCovid.forms import BarbijosFormulario
# Create your views here.

def inicio(request):

    return render(request, "AppCovid/inicio.html")

def guantes(request):

    return render(request, "AppCovid/guantes.html")

def barbijos(request):
    
    return render(request, "AppCovid/barbijos.html")

def oximetros(request):
    
    return render(request, "AppCovid/oximetros.html")

def barbijosFormulario(request):
    if request.method == "POST":

        miFormulario = BarbijosFormulario(request.POST)
        
        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            barbijoInst= Barbijos(marca= informacion["marca"], tamanio= informacion["tamanio"], precio= request.POST ["precio"])

            barbijoInst.save()  

            return render(request,"AppCovid/inicio.html")

    else:

        miFormulario = BarbijosFormulario()

    return render(request, "AppCovid/barbijosFormulario.html", {"miFormulario": miFormulario})

def busquedaDeBarbijos(request):

    return render(request, "AppCovid/busquedaDeBarbijos.html")


def buscar(request):

    #if request.GET["marca"]:
        
        #marca= request.GET["marca"]

        #barbijo= Barbijos.objects.filter(marca_icontains= marca)

    respuesta= f"Estoy buscando a: {request.GET['marca']}"
        #return render(request, "AppCovid/resultadoBusqueda.html")
    #else: 
        #respuesta= "Por favor mandame mas informacion, sino no puedo ayudarte"
    return HttpResponse(respuesta)