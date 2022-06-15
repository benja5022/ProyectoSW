from django.urls import path

from appReponedor import views


urlpatterns = [

    path('', views.reponedor_general, name="reponedor"),
    path('reponedor_tareas/', views.reponedor_tareas, name="reponedortareas"),
    path('reponedor_registrar_turno/', views.reponedor_registrar_turno, name="reponedorturno"),
]
