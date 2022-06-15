from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def cajero_general(request):
    return render(request, "appCajero/cajero_general.html")


def cajero_registrar_venta(request):
    return render(request, "appCajero/cajero_registrar_venta.html")


def cajero_registrar_turno(request):
    return render(request, "appCajero/cajero_registrar_turno.html")

