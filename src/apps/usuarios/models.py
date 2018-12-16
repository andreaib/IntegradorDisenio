from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuarios(AbstractUser):
	
	def __str__(self):
		return self.first_name
