# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .. import azure_storage
from posts.forms import ActividadForm, ActividadUpdateForm, ActividadRevisionForm, ActividadForm
from django.contrib import messages
from posts.models import Perfil, Actividad
from .borradores_view import *


# Actividades
def actividad_create(request, pk):
    herramienta = Herramienta.objects.get(id=pk)
    if request.method == 'POST':
        form = ActividadForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            instrucciones = cleaned_data.get('instrucciones')
            estado = cleaned_data.get('estado')
            revisor1 = 0
            revisor2 = 0
            autor = request.user.id
            descripcion = cleaned_data.get('descripcion')
            url = cleaned_data.get('url')
            id_anterior = 0

            actividad = Actividad.objects.create(herramienta=herramienta, id_anterior=id_anterior, nombre=nombre,
                                                 instrucciones=instrucciones, estado=estado,
                                                 revisor1=revisor1, revisor2=revisor2, autor=autor,
                                                 descripcion=descripcion, url=url)

            actividad.save()
            messages.success(request, 'Se ha creado con éxito la Actividad ' +
                             str(actividad.nombre) + ', los cambios serán publicados '
                                                     'hasta terminar el proceso de vigía',
                             extra_tags='alert alert-success')
            return redirect(reverse('catalogo:index'))
    else:
        form = ActividadForm()
    return render(request, 'actividad_create.html', {'form': form, 'id': pk})


def actividad_update(request, pk):
    actividad = Actividad.objects.get(id=pk)
    if request.method == 'POST':
        form = ActividadUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            descripcion = cleaned_data.get('descripcion')
            instrucciones = cleaned_data.get('instrucciones')
            url = cleaned_data.get('url')
            estado = cleaned_data.get('estado')

            if int(estado) == 6 and actividad.estado == 6:
                actividad.nombre = nombre
                actividad.url = url
                actividad.instrucciones = instrucciones
                actividad.descripcion = descripcion
                actividad.save()
                messages.success(request, 'Se han guardado los cambios de ' + str(actividad.nombre),
                                 extra_tags='alert alert-success')
                return borradores_list(request)
            elif int(estado) == 1 and actividad.estado == 6:
                actividad.nombre = nombre
                actividad.url = url
                actividad.instrucciones = instrucciones
                actividad.descripcion = descripcion
                actividad.estado = 1
                actividad.save()
                messages.success(request, 'La actividad ' + str(actividad.nombre) +
                                 ' se ha enviado a gestión de conocimiento', extra_tags='alert alert-success')
                return borradores_list(request)
            elif actividad.estado == 3:
                actividad.estado = 4
                actividad.save()

                revisor1 = 0
                revisor2 = 0
                autor = request.user.id
                actividad_n = Actividad.objects.create(id_anterior=pk, nombre=nombre,
                                                           instrucciones=instrucciones, estado=estado,
                                                           revisor1=revisor1, revisor2=revisor2, autor=autor,
                                                           descripcion=descripcion, url=url)
                actividad_n.save()
                if estado == 1:
                    messages.success(request, 'La actividad ' + str(actividad.nombre) +
                                     ' se ha enviado a gestión de conocimiento', extra_tags='alert alert-success')
                else:
                    messages.success(request, 'Se han guardado los cambios de ' + str(actividad.nombre),
                                     extra_tags='alert alert-success')
                return redirect(reverse('catalogo:index'))
    else:
        form = ActividadUpdateForm(instance=actividad)

    return render(request, 'actividad_update.html', {'form': form, 'id': pk})


def actividad_update_revision(request, pk):
    actividad = Actividad.objects.get(id=pk)

    if request.method == 'POST':
        form = ActividadRevisionForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            actividad.nombre = cleaned_data.get('nombre')
            actividad.instrucciones = cleaned_data.get('instrucciones')
            actividad.descripcion = cleaned_data.get('descripcion')
            actividad.url = cleaned_data.get('url')

            actividad.save()
            return actividad_revisar(request, pk)
    else:
        disable = disable_list(actividad)
        form = ActividadRevisionForm(instance=actividad)
        return render(request, 'actividad_update_revision.html', {'form': form, 'id': pk, 'disable': disable})


def disable_list(actividad):
    if not actividad.id_anterior == 0:
        temp = list(Actividad.objects.all().filter(id=actividad.id_anterior).exclude(estado=5))
        actividad_old = temp.pop()
        return actividad.comparar(actividad_old)
    else:
        return None


def actividad_detail(request, pk):
    actividad = Actividad.objects.get(id=pk)
    if request.user.is_authenticated():
        if request.method == 'POST':
            return eliminar_actividad(actividad, request)

        elif actividad.estado == 3:
            context = {'actividad': actividad}
            return render(request, 'actividad_detail.html', context)
        elif actividad.estado == 6:
            return actividad_borrador(actividad, request)
        elif actividad.estado == 4:
            return actividad_bloqueada(actividad, request, pk)
        elif actividad.estado == 1:
            return actividad_revision(actividad, request)
        elif actividad.estado == 2:
            return actividad_publicacion(actividad, request)
        else:
            if actividad.estado == 3:
                context = {'actividad': actividad}
                return render(request, 'actividad_detail.html', context)
    else:
        if actividad.estado == 3 or actividad.estado == 4:
            context = {'actividad': actividad}
            return render(request, 'actividad_detail.html', context)


def eliminar_actividad(actividad, request):
    actividad.delete()
    messages.success(request, 'Se ha eliminado con éxito a ' + str(actividad.nombre),
                     extra_tags='alert alert-success')
    return redirect(reverse('catalogo:index'))


def actividad_borrador(actividad, request):
    actividad_old = None
    if not actividad.id_anterior == 0:
        temp = list(Actividad.objects.all().filter(id=actividad.id_anterior).exclude(estado=5))
        actividad_old = temp.pop()
    context = {'actividad': actividad, 'actividad_old': actividad_old}
    return render(request, 'actividad_detail.html', context)


def actividad_bloqueada(actividad, request, pk):
    temp = list(Actividad.objects.all().filter(id_anterior=pk).exclude(estado=5))
    actividad_old = temp.pop()
    autor = Perfil.objects.get(id=actividad_old.autor)
    estado = 'en revisión' if actividad_old.estado == 1 else \
        'en edición en borrador' if actividad_old.estado == 6 else 'pendiente a publicarse'
    msg = 'Esta es una versión que será modificada, ' + str(autor.user.first_name) + \
          ' ' + str(autor.user.last_name) + ' la ha modificado y está ' + str(estado) + \
          '. por tal motivo no es posible crear ediciones'
    context = {'actividad': actividad, 'actividad_old': actividad_old}
    messages.warning(request, msg, extra_tags='alert alert-warning')
    return render(request, 'actividad_detail.html', context)


def actividad_revision(actividad, request):
    autor = Perfil.objects.get(id=actividad.autor)
    msg = 'Esta instancia fue realizada por: ' + str(autor.user.first_name) + ' ' + str(autor.user.last_name)
    messages.warning(request, msg, extra_tags='alert alert-warning')
    if actividad.id_anterior == 0:
        context = {'actividad': actividad}
        return render(request, 'actividad_detail.html', context)
    else:
        actividad_old = Actividad.objects.get(id=actividad.id_anterior, estado=4)
        context = {'actividad': actividad, 'actividad_old': actividad_old}
        return render(request, 'actividad_detail.html', context)


def actividad_publicacion(actividad, request):
    autor = Perfil.objects.get(id=actividad.autor)
    msg = 'Esta instancia fue realizada por: ' + str(autor.user.first_name) + ' ' + str(autor.user.last_name)
    if not actividad.revisor1 == 0 and not actividad.revisor2 == 0:
        revisor1 = Perfil.objects.get(id=actividad.revisor1)
        revisor2 = Perfil.objects.get(id=actividad.revisor2)
        msg = msg + '. Los revisores fueron: ' + str(revisor1.user.first_name) + ' ' \
              + str(revisor1.user.last_name) + ' y ' + str(revisor2.user.first_name) \
              + ' ' + str(revisor2.user.last_name)
    messages.warning(request, msg, extra_tags='alert alert-warning')
    if actividad.id_anterior == 0:
        context = {'actividad': actividad}
        return render(request, 'actividad_detail.html', context)
    else:
        actividad_old = Actividad.objects.get(id=actividad.id_anterior, estado=4)
        context = {'actividad': actividad, 'actividad_old': actividad_old}
        return render(request, 'actividad_detail.html', context)


def actividad_vigia(request):
    if request.user.is_authenticated():
        actividads_r = Actividad.objects.all().filter(estado=1).exclude(autor=request.user.id). \
            exclude(revisor1=request.user.id)
        actividads_p = Actividad.objects.all().filter(estado=2)
        context = {'actividads_r': actividads_r, 'actividads_p': actividads_p}
        return render(request, 'vigia.html', context)
    else:
        actividads = Actividad.objects.all().filter(estado=3)
        context = {'actividads': actividads}
        return render(request, 'index.html', context)


def actividad_revisar(request, pk):
    if request.user.is_authenticated():
        actividad = Actividad.objects.get(id=pk)
        if actividad.revisor1 == 0:
            actividad.revisor1 = request.user.id
        else:
            actividad.revisor2 = request.user.id
            actividad.estado = 2
        actividad.save()
        messages.success(request, 'Ha revisado con éxito a ' + str(actividad.nombre),
                         extra_tags='alert alert-success')
        return redirect(reverse('catalogo:vigia'))

    else:
        # actividad = Actividad.objects.all().filter(estado=3)
        return redirect(reverse('catalogo:vigia'))


def actividad_publicar(request, pk):
    if request.user.is_authenticated():
        actividad = Actividad.objects.get(id=pk)
        actividad.estado = 3
        messages.success(request, 'Ha sido publicado con éxito a ' + str(actividad.nombre),
                         extra_tags='alert alert-success')

        if not actividad.id_anterior == 0:
            actividad_delete = Actividad.objects.get(id=actividad.id_anterior)
            actividad_delete.delete()

        actividad.id_anterior = 0
        actividad.save()
        return redirect(reverse('catalogo:vigia'))
    else:
        actividads = Actividad.objects.all().filter(estado=3)
        context = {'actividads': actividads}
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
