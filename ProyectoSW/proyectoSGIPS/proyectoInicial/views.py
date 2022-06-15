from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def login(request): #primera vista
    # doc_externo=loader.get_template('login.html')
    # documento=doc_externo.render()

    # return render(request, "proyectoinicial/login.html")#HttpResponse(documento)
    return render(request, "proyectoInicial/login.html")


#Vista Gerente

# def gerente_general(request):

#     # doc_externo=loader.get_template('gerente_general.html')
#     # documento=doc_externo.render()

#     # return HttpResponse(documento)
#     return render(request, "proyectoinicial/gerente_general.html")#HttpResponse(documento)


# def gerente_revisar_informe_personal(request):
#     return render(request, "proyectoinicial/gerente_revisar_informe_personal.html")

# def gerente_revisar_informe_productos(request):
#     return render(request, "proyectoinicial/gerente_revisar_informe_productos.html")

# def gerente_informe_mensual_productos(request):
#     return render(request, "proyectoinicial/gerente_informe_mensual_productos.html")

# def gerente_registrar_turno(request):
#     return render(request, "proyectoinicial/gerente_registrar_turno.html")


#Vista Supervisor

# def supervisor_general(request):
#     return render(request, "proyectoinicial/supervisor_general.html")


# def supervisor_generar_informe(request):
#     return render(request, "proyectoinicial/supervisor_generar_informe.html")

# def supervisor_registrar_turno(request):
#     return render(request, "proyectoinicial/supervisor_registrar_turno.html")


# def supervisor_registrar_supervision(request):
#     return render(request, "proyectoinicial/supervisor_registrar_supervision.html")


#Vista Cajero

# def cajero_general(request):
#     return render(request, "proyectoinicial/cajero_general.html")


# def cajero_registrar_venta(request):
#     return render(request, "proyectoinicial/cajero_registrar_venta.html")


# def cajero_registrar_turno(request):
#     return render(request, "proyectoinicial/cajero_registrar_turno.html")


#Vista Reponedor

# def reponedor_general(request):
#     return render(request, "proyectoinicial/reponedor_general.html")


# def reponedor_tareas(request):
#     return render(request, "proyectoinicial/reponedor_tareas.html")


# def reponedor_registrar_turno(request):
#     return render(request, "proyectoinicial/reponedor_registrar_turno.html")
