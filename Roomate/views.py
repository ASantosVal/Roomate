from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib import auth
from . import forms

idioma = "es"


# Iniciar sesi&oacute;n
def login(request):
	c = {}
	c.update(csrf(request)) #actualizar la autenticidad de la redireccion
	return render_to_response('accounts/login.html',c)

#comprobar si el usuario esta registrado
def auth_view(request):
	username = request.POST.get('username','') #almacenamos el nombre de usuario
	password = request.POST.get('password','') #almacenamos la contrase&ntilde;a
	user = auth.authenticate(username=username,password=password) # iniciamos session con dichos datos
	if user is not None: #si el usuario y la contrase&ntilde;a son validos
		auth.login(request, user)
		return redirect('main') #le redirigimos a la pagina de Inicio
	else:
		return redirect('invalid') # si no son validos los datos, se redirige al usuario a una pagina de error

#redirige al usuario a una pagina de error
def invalid_login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('web/'+idioma+'/invalid_login.html',c)

# Cerrar sesi&oacute;n
def logout(request):
	auth.logout(request)
	c = {}
	c.update(csrf(request))
	return render_to_response('web/'+idioma+'/welcome.html',c)

# Registrar un nuevo usuario
def register_new_user(request):
	if request.method == "POST": #si el usuario le dio al boton de registrarse
		form = forms.RegistrationForm(request.POST); #generar un formulario con los datos metido por el usuario
		if form.is_valid(): #comprobar si son validos dichos datos
			new_user = form.save(commit=True) #si son validos, los guardamos
			return redirect('register_success') #redireccion a una pagina que muestra un mensaje de usuario creado
	else:
		form = forms.RegistrationForm(); #si el usuario esta entrando en la pagina de registro, le mostramos un formulario vacio
	return render(request, 'web/'+idioma+'/register.html', {'form': form})

#mostrar mensaje de usuario creado
def user_created(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('web/'+idioma+'/registro_completado.html',c)
