import json

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect

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


def NuevoCliente(request):
	if request.is_ajax():
		try:		
			id_cliente = int(request.GET.get('id',None))
			first_name = request.GET.get('nombre',None)
			last_name = request.GET.get('apellido',None)
			email = request.GET.get('email',None)
			fecha_ingreso = request.GET.get('fe_ingreso',None)
			fecha_nacimiento = request.GET.get('id',None)
			cuil = request.GET.get('dni',None)
			sexo = request.GET.get('sexo',None)
			peso = request.GET.get('id',None)
			estatura = request.GET.get('estatura',None)
			username = first_name.lower() + last_name.lower()
		except Exception as e:
			print("************")
			print(str(e))

		estado = 'ok'
		try:
			c = Clientes.objects.create(
				#pk=id_cliente,
				username=username,
				first_name=first_name,
				last_name=last_name,
				email=email, 
				#fecha_ingreso=fecha_ingreso,
				#fecha_nacimiento=fecha_nacimiento, 
				cuil=cuil, 
				peso=peso, 
				estatura=estatura				
				)
		except Exception as e:
			estado='mal'
			print("***************")
			print(str(e))
		
		data = json.dumps(estado)
		mimetype = 'application/json'
		return HttpResponse(data, mimetype)
	else:
		return Http404
