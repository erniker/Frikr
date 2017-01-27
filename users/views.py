# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate,login as django_login
from users.forms import LoginForm

# Create your views here.
def login(request):
    error_messages=[]
    if request.method == 'POST':        #Vemos si la petición es POST (es cuando envian datos)
        form = LoginForm(request.POST)  #Instanciamos el formulario con los datos del POST
        if form.is_valid():             #Preguntar si es válido
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect('photos_home')
                else:
                    error_messages.append('El usuario no está activo')
    else:
        form = LoginForm()
    context = {
        'error': error_messages,
        'login_form': form
    }
    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('photos_home')