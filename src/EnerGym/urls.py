from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^login/$', views.LoginView, name='login'),
    
    url(r'^Clientes/', view=include('apps.clientes.urls', namespace='clientes')),
]
