from django import forms

from apps.clientes.models import Clientes, SEXO_SUBTIPO_CHOICE

class formClientes(forms.ModelForm):
	username = forms.CharField( label="Nombre de Usuario",
							  	  required=True, 
							  	  widget=forms.TextInput(attrs={'class':'form-control',}) )

	first_name = forms.CharField( label="Nombre",
							  	  required=True, 
							  	  widget=forms.TextInput(attrs={'class':'form-control',}) )

	last_name = forms.CharField( label="Apellido",
							  	  required=True, 
							  	  widget=forms.TextInput(attrs={'class':'form-control',}) )

	email = forms.EmailField(	label="Correo",
								required=True,
								widget=forms.TextInput(attrs={'class':'form-control',}) )

	fecha_ingreso = forms.DateField( label='Fecha de Ingreso',
									required =True,
									widget=forms.SelectDateWidget(attrs={'class':'form-control',}) )
	
	fecha_nacimiento = forms.DateField( label='Fecha de Nacimiento',
									required =True,
									widget=forms.SelectDateWidget(attrs={'class':'form-control',}) )
	
	cuil = forms.CharField( label="CUIL",
							  	  required=True, 
							  	  widget=forms.TextInput(attrs={'class':'form-control',}) )
	
	sexo = forms.ChoiceField(choices=SEXO_SUBTIPO_CHOICE, 
									label="Sexo",
		                            widget=forms.Select(attrs={
		                            	'class':'form-control',
                            			'required':'required',
		                            	}))
	peso = forms.DecimalField( label="Peso",
							  	  required=True, 
							  	  widget=forms.TextInput(attrs={'class':'form-control',}))
	
	estatura = forms.DecimalField( label="Estatura",
							  	  required=True, 
							  	  widget=forms.TextInput(attrs={'class':'form-control',}))
	
	tiene_permiso = forms.BooleanField(label="Tiene Permiso Medico?",required=False,widget=forms.CheckboxInput(attrs={
					'type':'checkbox',
		}) )

	def __init__(self, *args, **kwargs):
		super(formClientes, self).__init__(*args, **kwargs)
	
	class Meta:
		model = Clientes
		fields = ['username','first_name','last_name','email', 'fecha_ingreso','fecha_nacimiento', 'cuil', 'sexo', 'peso', 'estatura', 'tiene_permiso' ]