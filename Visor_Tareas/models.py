from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Tipado_de_Tareas(models.Model):
    
    Titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='Visor')
    
    def __str__(self):
        return self.Titulo


class Tareas(models.Model):
    
    titulo=models.CharField(max_length=50)
    tipo=models.ForeignKey(Tipado_de_Tareas, on_delete=models.CASCADE)
    contenido=models.CharField(max_length=50)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creado=models.DateTimeField(auto_now_add=True)
    
    fecha_Final=models.DateField()
    
    hora=models.TimeField()
    
    
    def __str__(self):
        return self.titulo