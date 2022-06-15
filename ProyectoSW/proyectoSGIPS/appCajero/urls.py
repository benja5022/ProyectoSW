from django.urls import path

from appCajero import views


urlpatterns = [

    path('', views.cajero_general, name="cajero"),
    path('cajero_registrar_venta/', views.cajero_registrar_venta, name="login"),
    path('cajero_registrar_turno/', views.cajero_registrar_turno, name="login"),

]
