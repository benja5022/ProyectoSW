from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def gerente_general(request):

    return render(request, "appGerente/gerente_general.html")


def gerente_revisar_informe_personal(request):
    return render(request, "appGerente/gerente_revisar_informe_personal.html")

def gerente_revisar_informe_productos(request):
    return render(request, "appGerente/gerente_revisar_informe_productos.html")

def gerente_informe_mensual_productos(request):
    return render(request, "appGerente/gerente_informe_mensual_productos.html")

def gerente_registrar_turno(request):
    return render(request, "appGerente/gerente_registrar_turno.html")