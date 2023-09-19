from django.contrib import admin
from .models import Tipado_de_Tareas,Tareas
# Register your models here.


class Controler_Tipado(admin.ModelAdmin):
    
    list_display=('Titulo',)


class Controler_Tareas(admin.ModelAdmin):
    list_display=('titulo','autor','contenido','fecha_creado','fecha_Final')
    search_fields=('titulo','autor','fecha_creado','fecha_Final')



admin.site.register(Tipado_de_Tareas,Controler_Tipado)

admin.site.register(Tareas,Controler_Tareas)