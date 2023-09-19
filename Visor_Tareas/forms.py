from django import forms


# -*- coding: utf-8 -*-

class Formulario_Crear_Tarea(forms.Form):
        titulo=forms.CharField(label='Titulo',required=True)
        contenido=forms.CharField(label='Contenido',required=True)
       
        
        
