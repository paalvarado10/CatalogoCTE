# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .. import azure_storage
from posts.forms import HerramientaForm, HerramientaUpdateForm
from django.contrib import messages
from posts.models import Perfil, Herramienta


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
            estado = 1
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
            herramienta.estado = 4
            herramienta.save()
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            sistemaOperativo = cleaned_data.get('sistemaOperativo')
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

            id_anterior = pk
            revisor1 = 0
            revisor2 = 0
            estado = 1
            autor = request.user.id
            herramienta_n = Herramienta.objects.create(id_anterior=id_anterior, nombre=nombre,
                                                       sistemaOperativo=sistemaOperativo, plataforma=plataforma,
                                                       fichaTecnica=fichaTecnica, licencia=licencia, estado=estado,
                                                       revisor1=revisor1, revisor2=revisor2, autor=autor,
                                                       descripcion=descripcion, urlReferencia=urlReferencia, logo=logo)
            herramienta_n.save()
            messages.success(request, 'Se ha editado con éxito la herramienta '+
                             str(herramienta.nombre)+', los cambios serán publicados hasta terminar el proceso de vigía',
                             extra_tags='alert alert-success')
            return render(request, 'herramienta_detail.html',{'herramienta': herramienta})
    else:
        herramienta.sistemaOperativo = texto_a_lista(herramienta.sistemaOperativo)
        form = HerramientaUpdateForm(instance=herramienta)


    return render(request, 'herramienta_update.html', {'form': form, 'id':pk})


def herramienta_detail(request, pk):
    herramienta = Herramienta.objects.get(id=pk)
    if request.user.is_authenticated():
        if request.method == 'POST' and request.user.perfil.role == 1:
            herramienta.delete()
            messages.success(request, 'Ha eliminado con éxito a ' + str(herramienta.nombre),
                             extra_tags='alert alert-success')
            return redirect(reverse('catalogo:index'))
        elif herramienta.estado == 3:
            context = {'herramienta': herramienta}
            return render(request, 'herramienta_detail.html', context)

        elif herramienta.estado == 4:
            temp = list(Herramienta.objects.all().filter(id_anterior=pk).exclude(estado=5))
            herramienta_old = temp.pop()
            autor = Perfil.objects.get(id=herramienta_old.autor)
            estado = 'en revisión' if herramienta_old.estado == 1 else 'pendiente a publicar se'
            msg = 'Esta es una versión que será modificada, ' + str(autor.user.first_name) +\
                ' ' + str(autor.user.last_name) + ' la ha modificado y está ' + str(estado) +\
                  '. por tal motivo no es posible crear ediciones'
            context = {'herramienta': herramienta, 'herramienta_old': herramienta_old}
            messages.warning(request,msg, extra_tags='alert alert-warning')
            return render(request, 'herramienta_detail.html', context)

        elif herramienta.estado == 1 or herramienta.estado == 2:
            if herramienta.id_anterior == 0:
                context = {'herramienta': herramienta}
                return render(request, 'herramienta_detail.html', context)
            else:
                try:
                    herramienta_old = Herramienta.objects.get(id=herramienta.id_anterior, estado=4)
                    autor = Perfil.objects.get(id=herramienta.autor)
                    context = {'herramienta': herramienta, 'herramienta_old': herramienta_old}
                    msg = 'Esta modificación fue realizada por: ' + str(autor.user.first_name) + ' ' + str(autor.user.last_name)

                    if not herramienta.revisor1 == 0 and not herramienta.revisor2 == 0:
                        revisor1 = Perfil.objects.get(id=herramienta.revisor1)
                        revisor2 = Perfil.objects.get(id=herramienta.revisor2)
                        msg = msg + ' y los revisores  fueron: ' + str(revisor1.user.first_name) + ' ' \
                              + str(revisor1.user.last_name) + ' y ' + str(revisor2.user.first_name) \
                                    + ' ' + str(revisor2.user.last_name)

                    messages.warning(request, msg, extra_tags='alert alert-warning')
                    return render(request, 'herramienta_detail.html', context)
                except Herramienta.DoesNotExist:
                    print("Base de datos inconsistente")
                except Herramienta.MultipleObjectsReturned:
                    print("Base de datos inconsistente")
        else:
            if herramienta.estado == 3:
                context = {'herramienta': herramienta}
                return render(request, 'herramienta_detail.html', context)

    else:
        if herramienta.estado == 3 or herramienta.estado == 4:
            context = {'herramienta': herramienta}
            return render(request, 'herramienta_detail.html', context)


def herramientas_vigia(request):
    if request.user.is_authenticated():
        herramientas_r = Herramienta.objects.all().filter(estado=1).exclude(autor=request.user.id). \
            exclude(revisor1=request.user.id)
        herramientas_p = Herramienta.objects.all().filter(estado=2)
        context = {'herramientas_r': herramientas_r, 'herramientas_p': herramientas_p}
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
        context = {'herramientas': herramientas}
        return render(request, 'index.html', context)


def herramienta_publicar(request, pk):
    if request.user.is_authenticated():
        herramienta = Herramienta.objects.get(id=pk)
        herramienta.estado = 3
        messages.success(request, 'Ha sido publicado con éxito a '+str(herramienta.nombre), extra_tags='alert alert-success')

        if not herramienta.id_anterior == 0:
            herramienta_delete = Herramienta.objects.get(id=herramienta.id_anterior)
            herramienta_delete.estado = 5
            herramienta_delete.save()
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
