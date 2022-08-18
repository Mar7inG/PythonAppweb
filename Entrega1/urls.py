from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
   



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Appventas/', include("Appventas.urls")),
    path('',include("Appventas.urls"))
      

    
   
]

#Para las imagenes. Se instalo con pip install Pillow para usar ImageField
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Crear super usuario: python manage.py createsuperuser
