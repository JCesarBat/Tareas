from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.


class Registro(View):
    
    def get(self,request):
        form=UserCreationForm()
        
        return render(request,'Registro_Logeo/Templates/Registro.html',{'Titulo':'Registro','form':form})
        
    def post(self,request):
        
        form=UserCreationForm(request.POST)
        if form.is_valid():
            
            usuario=form.save()
            
            login(request, usuario)
            return redirect('Visor')
        else:
            
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
                
            return render(request,'Registro_Logeo/Templates/Registro.html',{'Titulo':'Registro','form':form})
        
        
        
def cerrar_session(request):
    logout(request)
    
    return redirect('Logear')
    
                  
def Logear(request):
    form=AuthenticationForm()
    if request.method=='POST':
       
            usuario=authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            
            if usuario is None :
                
                for msg in form.error_messages:
                    messages.error(request,form.error_messages[msg])
                    
                return render(request, 'Registro_Logeo/Templates/Logear.html',{'Titulo':'Bienvenid','form':form})
            else:
                login(request, usuario)
                return redirect('Visor')
            
    
    return render(request, 'Registro_Logeo/Templates/Logear.html',{'Titulo':'Bienvenido','form':form})
    





    

