from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def reponedor_general(request):
    return render(request, "appReponedor/reponedor_general.html")


def reponedor_tareas(request):
    return render(request, "appReponedor/reponedor_tareas.html")


def reponedor_registrar_turno(request):
    return render(request, "appReponedor/reponedor_registrar_turno.html")
