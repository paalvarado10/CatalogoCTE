# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .. import azure_storage
from posts.forms import HerramientaForm, HerramientaUpdateForm, HerramientaRevisionForm
from django.contrib import messages
from posts.models import Perfil, Actividad
from .borradores_view import *


# Herramientas
def herramienta_create(request):
    if request.method == 'POST':
        form = HerramientaForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            sistemaoperativo = arreglo_a_texto(cleaned_data.get('sistemaOperativo'))
            plataforma = cleaned_data.get('plataforma')
            fichatecnica = cleaned_data.get('fichaTecnica')
            licencia = cleaned_data.get('licencia')
            estado = cleaned_data.get('estado')
            revisor1 = 0
            revisor2 = 0
            autor = request.user.id
            descripcion = cleaned_data.get('descripcion')
            urlreferencia = cleaned_data.get('urlReferencia')
            logo = 'default'
            id_anterior = 0

            logoL = True if 'logo' in request.FILES else False
            if logoL:
                myfile = request.FILES['logo']
                chu = myfile.chunks()
                archivo = ''
                for chunk in chu:
                    a = chunk
                    archivo = archivo + a
                url = azure_storage.guardar_archivo(archivo, myfile.name)
                logo = url

            herramienta = Herramienta.objects.create(id_anterior=id_anterior, nombre=nombre,
                                                     sistemaOperativo=sistemaoperativo, plataforma=plataforma,
                                                     fichaTecnica=fichatecnica, licencia=licencia, estado=estado,
                                                     revisor1=revisor1, revisor2=revisor2, autor=autor,
                                                     descripcion=descripcion, urlReferencia=urlreferencia, logo=logo)
            herramienta.save()
            messages.success(request, 'Se ha creado con éxito la herramienta ' +
                             str(herramienta.nombre) + ', los cambios serán publicados '
                                                       'hasta terminar el proceso de vigía',
                             extra_tags='alert alert-success')
            return redirect(reverse('catalogo:index'))
    else:
        form = HerramientaForm()
    return render(request, 'herramienta_create.html', {'form': form})


def herramienta_update(request, pk):
    herramienta = Herramienta.objects.get(id=pk)
    current_logo = herramienta.logo
    if request.method == 'POST':
        form = HerramientaUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            sistemaOperativo = arreglo_a_texto(cleaned_data.get('sistemaOperativo'))
            plataforma = cleaned_data.get('plataforma')
            fichaTecnica = cleaned_data.get('fichaTecnica')
            licencia = cleaned_data.get('licencia')
            descripcion = cleaned_data.get('descripcion')
            urlReferencia = cleaned_data.get('urlReferencia')
            logo = current_logo
            logoL = True if 'logo' in request.FILES else False
            if logoL:
                myfile = request.FILES['logo']
                chu = myfile.chunks()
                archivo = ''
                for chunk in chu:
                    a = chunk
                    archivo = archivo + a
                url = azure_storage.guardar_archivo(archivo, myfile.name)
                logo = url
            estado = cleaned_data.get('estado')

            if int(estado) == 6 and herramienta.estado == 6:
                herramienta.nombre = nombre
                herramienta.sistemaOperativo = sistemaOperativo
                herramienta.urlReferencia = urlReferencia
                herramienta.plataforma = plataforma
                herramienta.fichaTecnica = fichaTecnica
                herramienta.licencia = licencia
                herramienta.descripcion = descripcion
                herramienta.logo = logo
                herramienta.save()
                messages.success(request, 'Se han guardado los cambios de ' + str(herramienta.nombre),
                                 extra_tags='alert alert-success')
                return borradores_list(request)
            elif int(estado) == 1 and herramienta.estado == 6:
                herramienta.nombre = nombre
                herramienta.sistemaOperativo = sistemaOperativo
                herramienta.urlReferencia = urlReferencia
                herramienta.plataforma = plataforma
                herramienta.fichaTecnica = fichaTecnica
                herramienta.licencia = licencia
                herramienta.descripcion = descripcion
                herramienta.logo = logo
                herramienta.estado = 1
                herramienta.save()
                messages.success(request, 'La herramienta ' + str(herramienta.nombre) +
                                 ' se ha enviado a gestión de conocimiento', extra_tags='alert alert-success')
                return borradores_list(request)
            elif herramienta.estado == 3:
                herramienta.estado = 4
                herramienta.save()

                revisor1 = 0
                revisor2 = 0
                autor = request.user.id
                herramienta_n = Herramienta.objects.create(id_anterior=pk, nombre=nombre,
                                                           sistemaOperativo=sistemaOperativo, plataforma=plataforma,
                                                           fichaTecnica=fichaTecnica, licencia=licencia, estado=estado,
                                                           revisor1=revisor1, revisor2=revisor2, autor=autor,
                                                           descripcion=descripcion, urlReferencia=urlReferencia, logo=logo)
                herramienta_n.save()
                if estado == 1:
                    messages.success(request, 'La herramienta ' + str(herramienta.nombre) +
                                     ' se ha enviado a gestión de conocimiento', extra_tags='alert alert-success')
                else:
                    messages.success(request, 'Se han guardado los cambios de ' + str(herramienta.nombre),
                                     extra_tags='alert alert-success')
                return redirect(reverse('catalogo:index'))
    else:
        herramienta.sistemaOperativo = texto_a_lista(herramienta.sistemaOperativo)
        form = HerramientaUpdateForm(instance=herramienta)

    return render(request, 'herramienta_update.html', {'form': form, 'id': pk})


def herramienta_update_revision(request, pk):
    herramienta = Herramienta.objects.get(id=pk)

    if request.method == 'POST':
        form = HerramientaRevisionForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            herramienta.nombre = cleaned_data.get('nombre')
            herramienta.sistemaOperativo = arreglo_a_texto(cleaned_data.get('sistemaOperativo'))
            herramienta.plataforma = cleaned_data.get('plataforma')
            herramienta.fichaTecnica = cleaned_data.get('fichaTecnica')
            herramienta.licencia = cleaned_data.get('licencia')
            herramienta.descripcion = cleaned_data.get('descripcion')
            herramienta.urlReferencia = cleaned_data.get('urlReferencia')

            logoL = True if 'logo' in request.FILES else False
            if logoL:
                myfile = request.FILES['logo']
                chu = myfile.chunks()
                archivo = ''
                for chunk in chu:
                    a = chunk
                    archivo = archivo + a
                url = azure_storage.guardar_archivo(archivo, myfile.name)
                herramienta.logo = url

            herramienta.save()
            return herramienta_revisar(request, pk)
    else:
        herramienta.sistemaOperativo = texto_a_lista(herramienta.sistemaOperativo)
        disable = disable_list(herramienta)
        form = HerramientaRevisionForm(instance=herramienta)
        return render(request, 'herramienta_update_revision.html', {'form': form, 'id': pk, 'disable': disable})


def disable_list(herramienta):
    if not herramienta.id_anterior == 0:
        temp = list(Herramienta.objects.all().filter(id=herramienta.id_anterior).exclude(estado=5))
        herramienta_old = temp.pop()
        return herramienta.comparar(herramienta_old)

    else:
        return None


def herramienta_detail(request, pk):
    herramienta = Herramienta.objects.get(id=pk)
    actividades = Actividad.objects.all().filter(herramienta_id=pk)
    if request.user.is_authenticated():
        if request.method == 'POST':
            return eliminar_herramienta(herramienta, request)
        elif herramienta.estado == 3:
            context = {'herramienta': herramienta, 'actividades': actividades}
            return render(request, 'herramienta_detail.html', context)

        elif herramienta.estado == 6:
            return herramienta_borrador(herramienta, request)

        elif herramienta.estado == 4:
            return herramienta_bloqueada(herramienta, request, pk)

        elif herramienta.estado == 1:
            return herramienta_revision(herramienta, request)

        elif herramienta.estado == 2:
            return herramienta_publicacion(herramienta, request)
        else:
            if herramienta.estado == 3:
                context = {'herramienta': herramienta, 'actividades': actividades}
                return render(request, 'herramienta_detail.html', context)
    else:
        if herramienta.estado == 3 or herramienta.estado == 4:
            context = {'herramienta': herramienta, 'actividades': actividades}
            return render(request, 'herramienta_detail.html', context)


def eliminar_herramienta(herramienta, request):
    herramienta.delete()
    messages.success(request, 'Se ha eliminado con éxito a ' + str(herramienta.nombre),
                     extra_tags='alert alert-success')
    return redirect(reverse('catalogo:index'))


def herramienta_borrador(herramienta, request):
    herramienta_old = None
    if not herramienta.id_anterior == 0:
        temp = list(Herramienta.objects.all().filter(id=herramienta.id_anterior).exclude(estado=5))
        herramienta_old = temp.pop()
    context = {'herramienta': herramienta, 'herramienta_old': herramienta_old}
    return render(request, 'herramienta_detail.html', context)


def herramienta_bloqueada(herramienta, request, pk):
    temp = list(Herramienta.objects.all().filter(id_anterior=pk).exclude(estado=5))
    herramienta_old = temp.pop()
    autor = Perfil.objects.get(id=herramienta_old.autor)
    estado = 'en revisión' if herramienta_old.estado == 1 else \
        'en edición en borrador' if herramienta_old.estado == 6 else 'pendiente a publicarse'
    msg = 'Esta es una versión que será modificada, ' + str(autor.user.first_name) + \
          ' ' + str(autor.user.last_name) + ' la ha modificado y está ' + str(estado) + \
          '. por tal motivo no es posible crear ediciones'
    context = {'herramienta': herramienta, 'herramienta_old': herramienta_old}
    messages.warning(request, msg, extra_tags='alert alert-warning')
    return render(request, 'herramienta_detail.html', context)


def herramienta_revision(herramienta, request):
    autor = Perfil.objects.get(id=herramienta.autor)
    msg = 'Esta instancia fue realizada por: ' + str(autor.user.first_name) + ' ' + str(autor.user.last_name)
    messages.warning(request, msg, extra_tags='alert alert-warning')
    if herramienta.id_anterior == 0:
        context = {'herramienta': herramienta}
        return render(request, 'herramienta_detail.html', context)
    else:
        herramienta_old = Herramienta.objects.get(id=herramienta.id_anterior, estado=4)
        context = {'herramienta': herramienta, 'herramienta_old': herramienta_old}
        return render(request, 'herramienta_detail.html', context)


def herramienta_publicacion(herramienta, request):
    autor = Perfil.objects.get(id=herramienta.autor)
    msg = 'Esta instancia fue realizada por: ' + str(autor.user.first_name) + ' ' + str(autor.user.last_name)
    if not herramienta.revisor1 == 0 and not herramienta.revisor2 == 0:
        revisor1 = Perfil.objects.get(id=herramienta.revisor1)
        revisor2 = Perfil.objects.get(id=herramienta.revisor2)
        msg = msg + '. Los revisores fueron: ' + str(revisor1.user.first_name) + ' ' \
              + str(revisor1.user.last_name) + ' y ' + str(revisor2.user.first_name) \
              + ' ' + str(revisor2.user.last_name)
    messages.warning(request, msg, extra_tags='alert alert-warning')
    if herramienta.id_anterior == 0:
        context = {'herramienta': herramienta}
        return render(request, 'herramienta_detail.html', context)
    else:
        herramienta_old = Herramienta.objects.get(id=herramienta.id_anterior, estado=4)
        context = {'herramienta': herramienta, 'herramienta_old': herramienta_old}
        return render(request, 'herramienta_detail.html', context)


def herramientas_vigia(request):
    if request.user.is_authenticated():
        herramientas_r = Herramienta.objects.all().filter(estado=1).exclude(autor=request.user.id). \
            exclude(revisor1=request.user.id)
        herramientas_p = Herramienta.objects.all().filter(estado=2)

        actividades_r = Actividad.objects.all().filter(estado=1).exclude(autor=request.user.id). \
            exclude(revisor1=request.user.id)
        actividades_p = Actividad.objects.all().filter(estado=2)
        context = {'herramientas_r': herramientas_r, 'herramientas_p': herramientas_p, 'actividades_p': actividades_p, 'actividades_r': actividades_r}
        return render(request, 'vigia.html', context)
    else:
        herramientas = Herramienta.objects.all().filter(estado=3)
        context = {'herramientas': herramientas}
        return render(request, 'index.html', context)


def herramienta_revisar(request, pk):
    if request.user.is_authenticated():
        herramienta = Herramienta.objects.get(id=pk)
        if herramienta.revisor1 == 0:
            herramienta.revisor1 = request.user.id
        else:
            herramienta.revisor2 = request.user.id
            herramienta.estado = 2
        herramienta.save()
        messages.success(request, 'Ha revisado con éxito a '+str(herramienta.nombre), extra_tags='alert alert-success')
        return redirect(reverse('catalogo:vigia'))

    else:
        herramientas = Herramienta.objects.all().filter(estado=3)
        return redirect(reverse('catalogo:vigia'))


def herramienta_publicar(request, pk):
    if request.user.is_authenticated():
        herramienta = Herramienta.objects.get(id=pk)
        herramienta.estado = 3
        messages.success(request, 'Ha sido publicado con éxito a '+str(herramienta.nombre), extra_tags='alert alert-success')

        if not herramienta.id_anterior == 0:
            herramienta_delete = Herramienta.objects.get(id=herramienta.id_anterior)
            herramienta_delete.delete()

        herramienta.id_anterior = 0
        herramienta.save()
        return redirect(reverse('catalogo:vigia'))
    else:
        herramientas = Herramienta.objects.all().filter(estado=3)
        context = {'herramientas': herramientas}
        return render(request, 'index.html', context)


def arreglo_a_texto(lista):
    resp = ''
    for index, element in enumerate(lista):
        if index == 0:
            resp = element
        else:
            resp = resp + ', ' + element
    return resp


def texto_a_lista(lista):
    resp = lista.split(', ')
    return resp
