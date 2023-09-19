# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 00:56:28 2023

@author: JC
"""

from django.urls import path
from Visor_Tareas import views

urlpatterns=[
    path('Visor_Tareas/',views.Visor_Tareas,name='Visor'),
    path('Crear_Tareas/',views.Crear_Tareas.as_view(),name='Crear'),
    
    path('Visor_T_Mes/<int:mes>/',views.Visor_T_Mes,name='Visor_Mes'),
    
    ]