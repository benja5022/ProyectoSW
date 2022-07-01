from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def supervisor_general(request):
    return render(request, "appSupervisor/supervisor_general.html")


def supervisor_generar_informe(request):
    return render(request, "appSupervisor/supervisor_generar_informe.html")

def supervisor_registrar_turno(request):
    return render(request, "appSupervisor/supervisor_registrar_turno.html")


def supervisor_registrar_supervision(request):
    return render(request, "appSupervisor/supervisor_registrar_supervision.html")


# Create your views here.
