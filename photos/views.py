# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm
from users.forms import LoginForm
from django.urls import reverse
# Create your views here.
def home(request):

   #Esta función devuelve el home de mi página

    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-create_at')
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        # cargar la plantilla de detalle
        context = {
            'photo': photo,
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto')  # 404 not found

def create(request):
    """
    Muestra un formulario para crear una foto y la crea si la petición es POST
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """

    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST)  # Instanciamos el formulario con los datos del POST
        if form.is_valid():             # Preguntar si es válido
            new_photo = form.save()      #Guarda el objeto Photo y me lo devuelve
            form = PhotoForm()
            success_message = '¡Guardado con éxito!'
            success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += 'Ver foto'
            success_message += '</a>'
    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'photos/new_photo.html', context)



    #html = '<ul>'
    #for photo in photos:
        #html += '<li>' + photo.name + '</li>'
    #html += '</ul>'
    #return HttpResponse(html)
