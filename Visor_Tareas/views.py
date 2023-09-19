from django.shortcuts import render,redirect
from .models import Tareas,Tipado_de_Tareas
from .forms import Formulario_Crear_Tarea
from django.views.generic import View

# Create your views here.


def Visor_T_Mes(request,mes):
    if request.user.is_authenticated:
        
        if mes==1:
            nombre_mes='Enero'
        if mes==2:
            nombre_mes='Febrero'
        if mes==3:
            nombre_mes='Marzo'
        if mes==4:
            nombre_mes='Abril'
        if mes==5:
            nombre_mes='Mayo'
        if mes==6:
            nombre_mes='Junio'
        if mes==7:
            nombre_mes='Julio'
        if mes==8:
            nombre_mes='Agosto'
        if mes==9:
            nombre_mes='Septiembre'
        if mes==10:
            nombre_mes='Octubre'
        if mes==11:
            nombre_mes='Noviembre'
        if mes==12:
            nombre_mes='Diciembre'
        
        
        tareas=Tareas.objects.filter(autor=request.user.id)
        
        Lista_tareas=[]
        for tarea in tareas :
            if tarea.fecha_Final.month== mes:
                
                Lista_tareas.append(tarea)
        
        for i in range(len(Lista_tareas)):
            
            for j in range(len(Lista_tareas)):
                
                if Lista_tareas[i].fecha_Final < Lista_tareas[j].fecha_Final:
                    var=Lista_tareas[j]
                    Lista_tareas[j]=Lista_tareas[i]
                    Lista_tareas[i]=var
                      
 
        return render(request,'Visor_Tareas/Templates/Visor.html',{'Title':'Calendario de Tareas  de '+nombre_mes ,'tareas':Lista_tareas})
    else:
        return redirect('Logear')
        
    
        

def Visor_Tareas(request):
    if request.user.is_authenticated:
        
        tareas=Tareas.objects.filter(autor=request.user.id)
        Lista_tareas=[]
        for i in tareas :
            Lista_tareas.append(i)
        
        for i in range(len(Lista_tareas)):
            
            for j in range(len(Lista_tareas)):
                
                if Lista_tareas[i].fecha_Final < Lista_tareas[j].fecha_Final:
                    var=Lista_tareas[j]
                    Lista_tareas[j]=Lista_tareas[i]
                    Lista_tareas[i]=var
                    
            
            
                    
 
        return render(request,'Visor_Tareas/Templates/Visor.html',{'Title':'Calendario de Tareas','tareas':Lista_tareas})
    else:
        
        return redirect('Logear')
    
    
    
    
    

class Crear_Tareas(View):
    
        def get(self,request):
            if request.user.is_authenticated:
                form=Formulario_Crear_Tarea()
                
                Tipo=Tipado_de_Tareas.objects.all()
                
                diccio={'Titulo':'Crear Tareas','form':form,'Tipo':Tipo}
                return render(request, 'Visor_Tareas/Templates/Crear_T.html',diccio)
            
            else:
                return redirect('Logeo')
            
        def post(self,request) :
            
            Tipo=Tipado_de_Tareas()
            Tipo=Tipado_de_Tareas.objects.get(id=request.POST.get('radio_buton'))
            
            tarea=Tareas()
            
            tarea.titulo=request.POST.get('titulo')
            tarea.tipo=Tipo
            tarea.contenido= request.POST.get('contenido')
            tarea.autor=request.user
            tarea.fecha_Final=request.POST.get('fecha')
            tarea.hora=request.POST.get('Time')
            
            tarea.save()
            return redirect('Visor')
            
