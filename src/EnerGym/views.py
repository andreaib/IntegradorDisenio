from django.shortcuts import render

def LoginView(request):
	template = 'login.html'

	ctx = {

	}
	
	return render(request, template, ctx)