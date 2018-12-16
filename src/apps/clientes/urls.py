from django.conf.urls import url, include

from . import views

app_name = "clientes"
urlpatterns = [
	url(r'^Nuevo/', views.Crear.as_view(), name='crear'),
	url(r'^listar/', views.Listar.as_view(), name='listar'),
]