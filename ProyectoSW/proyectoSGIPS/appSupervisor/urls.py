from django.urls import path

from appSupervisor import views


urlpatterns = [

    path('', views.supervisor_general ,name="supervisor"),
    path('supervisor_generar_informe/', views.supervisor_generar_informe ,name="supervisorinforme"),
    path('supervisor_registrar_turno/', views.supervisor_registrar_turno, name="supervisorturno"),
    path('supervisor_registrar_supervision/', views.supervisor_registrar_supervision, name="supervisorregistro"),
]
