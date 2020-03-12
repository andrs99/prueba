from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo


def inicio(request):

    fecha=datetime.datetime.now()

    persona=Persona("Luis Andres Rodriguez Campos","Administrador")

    temas=["Plantillas","Modelos","Formularios","Vistas","Despligue de aplicacion"]



    # doc_externo=open("/home/andres/Documentos/Django/Proyecto2/Proyecto2/plantillas/login.html")
    # plt=Template(doc_externo.read())
    # doc_externo.close()
    #doc_externo=get_template('login.html')
    # ctx=Context({"nombre_persona":persona.nombre,"tipo_persona":persona.tipo,"fecha":fecha,"temas":temas})
    # documento=doc_externo.render(diccionario)
    # return HttpResponse(documento)
    diccionario={"nombre_persona":persona.nombre,"tipo_persona":persona.tipo,"fecha":fecha,"temas":temas}
    return render(request,'inicio.html',diccionario)

def view_python(request):
    return render(request,'python.html')

def view_javascript(request):
    return render(request,'javascript.html')

def view_java(request):
    return render(request,'java.html')

def view_csh(request):
    return render(request,'csh.html')

