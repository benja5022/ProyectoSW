from django.urls import path

from appGerente import views

urlpatterns = [

    path('', views.gerente_general, name="gerente"),
    path('gerente_revisar_informe_personal/', views.gerente_revisar_informe_personal, name="gerenteinfpersonal"),
    path('gerente_revisar_informe_productos/', views.gerente_revisar_informe_productos, name="gerenteinfproductos"),
    path('gerente_informe_mensual_productos/', views.gerente_informe_mensual_productos, name="gerenteinfmensual"),
    path('gerente_registrar_turno/', views.gerente_registrar_turno, name="gerenteturno"),

]
