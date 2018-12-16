from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.usuarios.models import Usuarios

SEXO_SUBTIPO_CHOICE = (
						('M', 'Masculino'),
						('F', 'Femenino'),
					)

class Clientes(Usuarios):
	fecha_ingreso = models.DateTimeField(blank=True, null=True)
	fecha_nacimiento = models.DateTimeField(blank=True, null=True)
	
	cuil = models.CharField(max_length=11,blank=True, null=True)
	
	

	sexo = models.CharField( choices=SEXO_SUBTIPO_CHOICE,
							max_length=1,
							default='M')

	peso = models.DecimalField(max_digits=5,
								decimal_places=2,
								blank=True, null=True)

	estatura = models.DecimalField(max_digits=5,
									decimal_places=2,
									blank=True, null=True)

	tiene_permiso = models.BooleanField(default=False)
	def __str__(self):
		return self.first_name
