from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Clientes
from .forms import formClientes

class Listar(ListView):
	model = Clientes	
	template_name = 'clientes/listaDeClientes.html'
	context_object_name = "clientes"

class Crear(CreateView):
	model = Clientes
	template_name = 'clientes/nuevoCliente.html'
	form_class = formClientes

	def get_success_url(self, **kwargs):
		return reverse('clientes:listar')
