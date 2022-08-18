
 


from multiprocessing import context
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from Appventas.models import accesorios, bicicletas, repuestos, indumentaria,EnviarMensajes
from Appventas.forms import EditarUsuario, accesoriosFormulario, bicisFormulario, repuestosFormulario, indumentariaFormularios, enviarMensaje
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm , UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin #solo funciona con las vistas basadas en clases
from django.contrib.auth.decorators import login_required#decorador para vistas basadas en funciones.Aumenta la funcionalidad de una funcion.
# Views de simple acceso
def Nosotros(request):#Template de Nostros

    return render(request, "QuienesSomos.html")



def Formularios(request):#Template de Formularios

    return render(request, "Formularios.html")

def inicio(request):#Template de Inivcio

    return render(request, "inicio.html")

#Enviar Mensaje
def IrEnviarMensaje(request):
    print("method:", request.method)
    if request.method == 'POST':
            print("1° IF")
            MensajeEnviado=enviarMensaje(request.POST)

            if MensajeEnviado.is_valid():
                print("2do IF")
                data=MensajeEnviado.cleaned_data# si le pongo parentesis o corchetes y entre comillas una variable en particular pide solo esa
                mensaje=EnviarMensajes(nombre=data["Nombre"],correo=["Correo"],telefono=["Telefono"],mensaje=["Mensaje"])
                mensaje.save()
                return render(request,"Save.html")
    else:
        print("method:", request.method)
        MensajeEnviado=enviarMensaje()
        return render (request,"EnviarMensaje.html",{"MensajeEnviar":MensajeEnviado})



def Save(request):#Template de confirmacion de guardado.

    return render(request, "Save.html")
#Formularios
@login_required
def Formulariobicis(request):#Template cargar una bici en la tabla

    if request.method == 'POST':
        BiciFormulario=bicisFormulario(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",BiciFormulario ) 

        if BiciFormulario.is_valid():
            print("Entro al 2° if")
            data=BiciFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            bici=bicicletas(marca=data['Marca'],modelo=data['Modelo'],rodado=data['Rodado'],color=data['Color'],precio=data['Precio'],codigo=data['Codigo'],descripcion=data['Descripcion'])
            bici.save()
            return render(request, "Save.html")
       # else:
        #    return render (request,"inicio2.html")
    else:
        BiciFormulario=bicisFormulario()
        return render(request,"FormularioBicicletas.html", {"BiciFormulario": BiciFormulario})

@login_required
def Formularioindumentarias(request):#Template cargar una indumentaria en la tabla


    if request.method == 'POST':
        InduFormulario=indumentariaFormularios(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",InduFormulario ) 

        if InduFormulario.is_valid():
            print("Entro al 2° if")
            data=InduFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            Indu=indumentaria(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],talle=data['Talle'],precio=data['Precio'],codigo=data['Codigo'],descripcion=data['Descripcion'])
            Indu.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        InduFormulario=indumentariaFormularios()
        return render(request,"FormularioIndumentaria.html", {"IndumentariaFormularios": InduFormulario})

@login_required
def Formulariorepuestos(request):#Template cargar un repuesto en la tabla

    if request.method == 'POST':
                        #forms.py
        RepuFormulario=repuestosFormulario(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",RepuFormulario ) 

        if RepuFormulario.is_valid():
            print("Entro al 2° if")
            data=RepuFormulario.cleaned_data
            #En la tabla que creo con la clase (models) le cargo los datos del formulario de Django(forms)
                     #models.py   (como se lee esto?: tipo=data['Tipo'])          
            repuesto=repuestos(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],codigo=data['Codigo'],descripcion=data['Descripcion'],precio=data['Precio'])
            repuesto.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        RepuFormulario=repuestosFormulario()
        return render(request,"FormularioRepuestos.html", {"RepuestosFormularios":RepuFormulario})

@login_required
def Formularioaccesorios(request):#Template cargar un repuesto en la tabla

    if request.method == 'POST':
                        #forms.py
        AccFormulario=accesoriosFormulario(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",AccFormulario ) 

        if AccFormulario.is_valid():
            print("Entro al 2° if")
            data=AccFormulario.cleaned_data
            #En la tabla que creo con la clase (models) le cargo los datos del formulario de Django(forms)
                     #models.py   (como se lee esto?: tipo=data['Tipo'])          
            repuesto=accesorios(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],precio=data['Precio'],codigo=data['Codigo'],descripcion=data['Descripcion'])
            repuesto.save()
            return render(request, "Save.html")
        else:
            return render (request,"inicio2.html")
    else:
        AccFormulario=accesoriosFormulario()
        return render(request,"FormularioAccesorios.html", {"AccesorioFormularios":AccFormulario})   


#VER FORMULARIOS
def LeerBicis (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioBicicletas=bicicletas.objects.all()
    contexto={"Bicicletas":FormularioBicicletas}
    return render (request, "VerFormulario_Bicicletas.html",contexto)

def LeerRepu (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioRepuestos=repuestos.objects.all()
    contexto={"Repuestos":FormularioRepuestos}
    return render (request, "VerFormulario_Repuestos.html",contexto)



def LeerIndum (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioIndumentaria=indumentaria.objects.all()
    contexto={"Indumentaria":FormularioIndumentaria}
    return render (request, "VerFormulario_Indumentaria.html",contexto)

def LeerAcc (request):
    print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 

    FormularioAccesorios=accesorios.objects.all()
    contexto={"Accesorios":FormularioAccesorios}
    return render (request, "VerFormulario_Accesorios.html",contexto)


#BUSQUEDA BICIS

def Busquedabicis(request):

    return render (request, "BusquedaBici.html")

def ResultBici(request):
    print(request.GET)

    if request.GET["modelo"]: 
       
        modelo=request.GET["modelo"]
      
        modelos=bicicletas.objects.filter(modelo__icontains=modelo)
        
        return render (request,"BusquedaBicicleta.html", {"modelos": modelos , "modelo":modelo})
    else:
       
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaBicicleta.html")
    

#BUSQUEDA INDUMENTARIA
def BusquedaIndu(request):

    return render (request, "BusquedaIndu.html")

def ResultIndu(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
        
        tipos=indumentaria.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaIndumentaria.html", {"tipos": tipos ,"tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaIndumentaria.html")
 

#BUSQUEDA RESPUESTO
def BusquedaRepues(request):

    return render (request, "BusquedaRepu.html")

def ResultRepues(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
        
        tipos = repuestos.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaRepuesto.html", {"tipos": tipos , "tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaRepuesto.html")
    
#BUSQUEDA ACCESORIOS
def BusquedaAcc(request):

    return render (request, "BusquedaAcc.html")

def ResultAcc(request):
    print(request.GET)

    if request.GET["tipo"]: 
        
        tipo=request.GET["tipo"]
       
        tipos=accesorios.objects.filter(tipo__icontains=tipo)
        
        return render (request,"BusquedaAccesorios.html", {"tipos": tipos , "tipo":tipo})
    else:
        
        respuesta="No enviaste datos"
        return render(respuesta,"BusquedaAccesorios.html")

#ELIMINAR DATOS

def eliminarbici(request, id):

    if request.method == "POST":


       bicicleta = bicicletas.objects.get(id = id)
       bicicleta.delete()

       #vuelvo al menu
       bicicleta = bicicletas.objects.all() #trae todas las bicicletas

       contexto = {"bicicletas" : bicicleta}
 
       return render (request, "VerFormulario_Bicicletas.html", contexto)

def eliminarIndumentaria(request, id):

    if request.method == "POST":


       indumentarias = indumentaria.objects.get(id = id)
       indumentarias.delete()

       #vuelvo al menu
       Indumentaria = indumentaria.objects.all() #trae todas las bicicletas

       contexto = {"indumentaria" : Indumentaria}
 
       return render (request, "VerFormulario_Indumentaria.html", contexto)

def eliminarrepuestos(request, id):

    if request.method == "POST":


       repuesto = repuestos.objects.get(id = id)
       repuesto.delete()

       #vuelvo al menu
       repuesto = indumentaria.objects.all() #trae todas las bicicletas

       contexto = {"indumentaria" : repuesto}
 
       return render (request, "VerFormulario_Repuestos.html", contexto)

def eliminaraccesorios(request, id):

    if request.method == "POST":


       accesorio = accesorios.objects.get(id = id)
       accesorio.delete()

       #vuelvo al menu
       accesorio = accesorios.objects.all() #trae todas las bicicletas

       contexto = {"indumentaria" : accesorio}
 
       return render (request, "VerFormulario_Accesorios.html", contexto)

#EDITAR

def editarbicis(request, id):

    bicicleta = bicicletas.objects.get(id = id)

    if request.method == 'POST':

        BiciFormulario=bicisFormulario(request.POST)

        if BiciFormulario.is_valid():
            print("Entro al 2° if")
            data=BiciFormulario.cleaned_data
        
            bicicleta.codigo = data ["codigo"]
            bicicleta.marca = data ["marca"]
            bicicleta.modelo = data ["modelo"]
            bicicleta.rodado = data ["rodado"]
            bicicleta.color = data ["color"]
            bicicleta.descripcion = data ["descripcion"]
            bicicleta.precio = data ["precio"]

            bicicleta.save()
            return render(request, "Save.html")
    
    else:
        BiciFormulario=bicisFormulario(initial={
            "codigo": bicicleta.codigo,
            "marca": bicicleta.marca,
            "modelo": bicicleta.modelo,
            "rodado": bicicleta.rodado,
            "color": bicicleta.color,
            "descripcion": bicicleta.descripcion,
            "precio": bicicleta.precio,
        

        })
        return render(request,"EditarBicicletas.html", {"BiciFormulario": BiciFormulario , "id": bicicleta.id})

def editarrepuestos(request, id):

    repuesto = repuestos.objects.get(id = id)

    if request.method == 'POST':
        
        repuFormulario=repuestosFormulario(request.POST)

        if repuFormulario.is_valid():
            print("Entro al 2° if")
            data=repuFormulario.cleaned_data
        
            repuesto.codigo = data ["codigo"]
            repuesto.marca = data ["marca"]
            repuesto.tipo = data ["tipo"]
            repuesto.modelo = data ["modelo"]
            repuesto.descripcion = data ["repuesto"]
            repuesto.precio = data ["repuesto"]

            repuesto.save()
            return render(request, "Save.html")
    
    else:
        repuFormulario=repuestosFormulario(initial={
            "codigo": repuesto.codigo,
            "marca": repuesto.marca,
            "modelo": repuesto.modelo,
            "tipo": repuesto.tipo,
            "descripcion": repuesto.descripcion,
            "precio": repuesto.precio,
        })
        return render(request,"EditarRepuestos.html", {"RepuFormulario": repuFormulario , "id": repuesto.id})

def editarindumentaria(request, id):

    indument = indumentaria.objects.get(id = id)

    if request.method == 'POST':
        
        induFormulario=indumentariaFormularios(request.POST)

        if induFormulario.is_valid():
            print("Entro al 2° if")
            data=induFormulario.cleaned_data
        
            indument.codigo = data ["codigo"]
            indument.marca = data ["marca"]
            indument.modelo = data ["modelo"]
            indument.descripcion = data ["repuesto"]
            indument.precio = data ["repuesto"]
            indument.tipo = data ["tipo"]
            indument.talle = data ["talle"]

            indument.save()
            return render(request, "Save.html")
    
    else:
        induFormulario=indumentariaFormularios(initial={
            "codigo": indument.codigo,
            "marca": indument.marca,
            "modelo": indument.modelo,
            "tipo": indument.tipo,
            "talle":indument.talle,
            "descripcion": indument.descripcion,
            "precio": indument.precio,
        })
        return render(request,"EditarIndumentaria.html", {"InduFormulario": induFormulario , "id": indument.id})


def editaraccesorios(request, id):

    acc = accesorios.objects.get(id = id)

    if request.method == 'POST':
        
        accFormulario=accesoriosFormulario(request.POST)

        if accFormulario.is_valid():
           
            data=accFormulario.cleaned_data
        
            acc.codigo = data ["codigo"]
            acc.marca = data ["marca"]
            acc.modelo = data ["modelo"]
            acc.descripcion = data ["repuesto"]
            acc.precio = data ["repuesto"]
            acc.tipo = data ["tipo"]
            acc.talle = data ["talle"]

            acc.save()
            return render(request, "Save.html")
    
    else:
        accFormulario=accesoriosFormulario(initial={
            "codigo": acc.codigo,
            "marca": acc.marca,
            "modelo": acc.modelo,
            "tipo": acc.tipo,
            "talle":acc.talle,
            "descripcion": acc.descripcion,
            "precio": acc.precio,
        })
        return render(request,"EditarAccesorios.html", {"AccFormulario": accFormulario , "id": acc.id})

#LOGIN
def iniciar_sesion(request):

    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            print("Entro al is valid")
            usuario=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            user=authenticate(username=usuario,password=clave)

            if user is not None:
                print("Entro al is not none")
                login(request,user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                print("Entro al is not none ELSE")
                form = AuthenticationForm()
                return render (request, "Login.html", {"mensaje":"Error!",'form':form}) 
        else:
                print("Entro al is valid ELSE")
                form = AuthenticationForm()
                return render (request, "Login.html", {"mensaje":"Error, datos incorrectos. \n Vuelva a intentarlo.",'form':form}) 
    else:
        print("Entro al metodo GET: ",request.method)
        form = AuthenticationForm()
        return render (request, "Login.html", {'form':form})

#Registrarse
def IrRegistrarse(request):
    return render (request, "LoginRegistro.html")

def registrarse(request):

    if request.method =="POST":
        print("1)method:", request.method)
        form=UserCreationForm(request.POST)
        #form=UserRegisterForm(request.POST)
        if form.is_valid():
            print("2)method:", request.method)
            username = form.cleaned_data['username']
            form.save()
            return render(request,'Save.html',{"mensaje":f"Usuario {username} creado."})
        else:
            form=UserCreationForm()
            return render (request, 'LoginRegistro.html',{"mensaje":f"Usuario no valido. Vuelva a Intentarlo.","form": form})
        
    else:
        form=UserCreationForm()
        return render (request,'LoginRegistro.html', {"form": form})

# #Perfil Usuario


def EditarPerfil(request):

    usuario=request.user
    
    if request.method == "POST":
         
        formularioPerfil=EditarUsuario (request.POST)


        if formularioPerfil.is_valid():
                
                data=formularioPerfil.cleaned_data

                usuario.first_name=data["first_name"]
                usuario.last_name=data["last_name"]
                usuario.email=data["email"]
                #usuario.password1=data["password1"]
                #usuario.password2=data["password2"]

                usuario.save()

                return render(request, "Save.html", {"mensaje":"Datos actualizados con exito.."})
    else:
          
        formularioPerfil=EditarUsuario (initial={'Nombre':usuario.first_name,'Apellido':usuario.last_name,'Email':usuario.email})
        #formularioPerfil=UserChangeForm (instance=request.user)
        
    return render (request, "LoginPerfil.html", {"PerfilFormulario":formularioPerfil}) 
        
   


