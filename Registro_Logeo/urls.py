# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:00:57 2023

@author: JC
"""

from django.urls import path
from Registro_Logeo import views

urlpatterns = [
    path('Registro/',views.Registro.as_view(),name='Registro'),
    path('Logear/',views.Logear,name='Logear'),
    path('cerrar_session/',views.cerrar_session,name='Desconectar'),
    ]