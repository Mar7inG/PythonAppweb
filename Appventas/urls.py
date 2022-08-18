from django.contrib import admin
from django.urls import path
from Appventas.views import (
    BusquedaAcc, EditarPerfil, Formularioaccesorios, Formulariobicis, Formularioindumentarias, Formulariorepuestos, LeerAcc, ResultAcc, editaraccesorios, editarbicis, editarindumentaria,
    editarrepuestos, eliminarIndumentaria, eliminaraccesorios, eliminarbici, eliminarrepuestos, iniciar_sesion, inicio, 
    Busquedabicis, registrarse, LeerIndum, LeerBicis, LeerRepu, ResultBici, BusquedaIndu, BusquedaRepues, ResultIndu, ResultRepues,
    Nosotros, Formularios, IrEnviarMensaje, IrRegistrarse
)
from django.contrib.auth.views import LogoutView
#from Appventas.views import BusquedaIndu, BusquedaRepuesto, RespuestaBuscarIndu, RespuestaBuscarRepuesto
                                  


urlpatterns = [
    
     #Simple accesow
    path('', inicio, name="INICIO"),
    path('Formularios', Formularios ,name="Formularios"),
    path('Nosotros/', Nosotros,name="Nosotros"),
    path('EnviarMensaje/',IrEnviarMensaje,name="EnviarMensaje"),
    #CARGAR DATOS
    path('FormularioBici/', Formulariobicis, name="bici_formulario"),
    path('repu_formulario/', Formulariorepuestos, name="repu_formulario"),
    path('indu_formulario/', Formularioindumentarias, name="indu_formulario"),
    path('acc_formulario/', Formularioaccesorios, name="acc_formulario"),
    #VER FORULARIOS
    path('Leerindumentria/', LeerIndum, name="Leerindume"),
    path('LeerBicicletas/', LeerBicis, name="LeerBicis"),
    path('LeerRepuestos/',LeerRepu, name="LeerRepues") ,
    path('LeerAccesorios/',LeerAcc, name="LeerAcc") ,     
    #BUSCAR
    #en el template. con "direccion"(sin /) entre las comillas, y con "{% url 'name'%}" va el name.         
    path('BusquedaBici/', Busquedabicis, name="Buscar1"),#Ir pagina de busqueda bicis
    path('IrBici/', ResultBici, name="Busqueda1"),#Buscar bici
    path('BuscarRepuesto/',BusquedaRepues,name="Buscar2"),
    path('IrRepues/',ResultRepues,name="Busqueda2"),
    path('BuscarIndumentaria/',BusquedaIndu, name="Buscar3"),
    path('Irndumentaria/', ResultIndu, name="Busqueda3"),
    path('BuscarAccesorio/', BusquedaAcc, name="BuscarAcc"),
    path('IrAccesorio/', ResultAcc, name="ResultAcc"),
    #ELIMINAR
    path('eliminarbici/<int:id>', eliminarbici, name="Eliminarbici"),
    path('eliminarindu/<int:id>', eliminarIndumentaria, name="Eliminarindu"),
    path('eliminarrepu/<int:id>', eliminarrepuestos, name="Eliminarrepu"),
    path('eliminaracc/<int:id>', eliminaraccesorios, name="Eliminaracc"),
    #EDITAR
    path('editarbicis/<int:id>', editarbicis, name="Editarbicis"),
    path('editarrepu/<int:id>', editarrepuestos, name="Editarrepu"),
    path('editarindu/<int:id>', editarindumentaria, name="Editarindu"),
    path('editaracc/<int:id>', editaraccesorios, name="Editaracc"),
    #LOGIN
    path('login', iniciar_sesion, name='Login'),
    path('IrRegistro', IrRegistrarse,name="IrRegistro" ),
    path('registrarse', registrarse, name='Registrarse'),
    path('logout', LogoutView.as_view(template_name='logout.html'),name='Logout'),
    path('loginPerfil', EditarPerfil, name="Perfil"),
    
    #Imagenes/Avatars
    
]

