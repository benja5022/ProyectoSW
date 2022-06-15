from django.urls import path

from proyectoInicial import views


urlpatterns = [

    path('login/', views.login, name="login"),

    # path('gerente_general/', views.gerente_general, name="gerente"),
    # path('gerente_revisar_informe_personal/', views.gerente_revisar_informe_personal, name="gerenteinfpersonal"),
    # path('gerente_revisar_informe_productos/', views.gerente_revisar_informe_productos, name="gerenteinfproductos"),
    # path('gerente_informe_mensual_productos/', views.gerente_informe_mensual_productos, name="gerenteinfmensual"),
    # path('gerente_registrar_turno/', views.gerente_registrar_turno, name="gerenteturno"),

    # path('supervisor_general/', views.supervisor_general ,name="supervisor"),
    # path('supervisor_generar_informe/', views.supervisor_generar_informe ,name="supervisorinforme"),
    # path('supervisor_registrar_turno/', views.supervisor_registrar_turno, name="supervisorturno"),
    # path('supervisor_registrar_supervision/', views.supervisor_registrar_supervision, name="supervisorregistro"),

    # path('cajero_general/', views.cajero_general, name="cajero"),
    # path('cajero_registrar_venta/', views.cajero_registrar_venta, name="login"),
    # path('cajero_registrar_turno/', views.cajero_registrar_turno, name="login"),

    # path('reponedor_general/', views.reponedor_general, name="reponedor"),
    # path('reponedor_tareas/', views.reponedor_tareas, name="reponedortareas"),
    # path('reponedor_registrar_turno/', views.reponedor_registrar_turno, name="reponedorturno"),
]
