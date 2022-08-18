
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class producto (models.Model):
   #id=models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    
    class Meta:
        abstract = True

# Create your models here.
class bicicletas(producto):

    rodado = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
   
    def __str__(self):
        return f"{self.marca, self.modelo, self.rodado, self.color, self.precio, self.codigo, self.descripcion}"


class repuestos(producto):#Borre fabricante
    tipo = models.CharField(max_length=30)
   
    def __str__(self):
        return f"{self.marca, self.tipo, self.modelo, self.precio, self.codigo, self.descripcion}"
    

class indumentaria(producto):
    tipo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    

    def __str__(self):
        return f"{self.marca, self.modelo, self.precio, self.talle, self.codigo, self.descripcion}"

class accesorios(producto):#Borre fabricante
    tipo = models.CharField(max_length=30)
   
    def __str__(self):
        return f"{self.marca, self.modelo, self.tipo, self.precio, self.codigo, self.descripcion}"

class perfiles(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono= models.IntegerField() 
    emial=models.EmailField(max_length=100)
    
    class Meta:
        abstract=True

class empleado(perfiles):
   cargo=models.CharField(max_length=30)

   def __str__(self):
    return f"{self.nombre,self.apellido, self.telefono,self.emial,self.cargo}"

class cliente(perfiles):
    edad=models.IntegerField()

    def __str__(self):
     return f"{self.nombre,self.apellido, self.telefono,self.emial,self.edad}"


class EnviarMensajes(models.Model):

    nombre=models.CharField(max_length=30)
    correo=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=30)
    mensaje=models.CharField(max_length=100)
       
    def __str__(self):
        return f"{self.nombre,self.correo,self.telefono, self.mensaje}"

#Comentar todo: selecciono . 1°ctrl+k . 2°ctrl+c (comentar) 2°ctrl+u (descomentar)

#Avatar
class Avatar(models.Model):

    #vinculo con el usuario
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #Subcarpeta avatares de media
    imagen=models.ImageField(upload_to='avatares', null=True,blank=True)
    