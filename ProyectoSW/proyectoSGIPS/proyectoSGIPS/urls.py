"""proyectoSGIPS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from proyectoSGIPS.views import login, gerente_general, gerente_revisar_informe_personal, gerente_revisar_informe_productos, gerente_informe_mensual_productos, gerente_registrar_turno, supervisor_general, supervisor_generar_informe, supervisor_registrar_turno, supervisor_registrar_supervision, cajero_general, cajero_registrar_venta, cajero_registrar_turno, reponedor_general, reponedor_tareas, reponedor_registrar_turno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proyectoInicial.urls')),
    path('appGerente/', include('appGerente.urls')),
    path('appCajero/', include('appCajero.urls')),
    path('appReponedor/', include('appReponedor.urls')),
    path('appSupervisor/', include('appSupervisor.urls')),
]
