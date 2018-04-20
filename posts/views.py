# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from azure.storage.blob import BlockBlobService
from posts.forms import UserForm, UserUpdateForm, UserChangePassword, UserUpdateGTIForm, \
    HerramientaForm, HerramientaUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from posts.models import Perfil, Herramienta
from decouple import config

# Create your views here.

def index(request):
    herramientas = Herramienta.objects.all()

    context = {'herramientas': herramientas}
    return render(request, 'index.html',context)

#autenticación
def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('catalogo:index'))
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('catalogo:index'))
        else:
            mensaje = 'Nombre de usuario o clave no valido'
    return render(request, 'login.html', {'mensaje': mensaje})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('catalogo:index'))

#Herramientas
def herramienta_create(request):
    if request.method == 'POST':
        form = HerramientaForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombre = cleaned_data.get('nombre')
            sistemaOperativo = cleaned_data.get('sistemaOperativo')
            plataforma = cleaned_data.get('plataforma')
            fichaTecnica = cleaned_data.get('fichaTecnica')
            licencia = cleaned_data.get('licencia')
            estado = 1
            revisor1 = 0
            revisor2 = 0
            autor = request.user.id
            descripcion = cleaned_data.get('descripcion')
            urlReferencia = cleaned_data.get('urlReferencia')
            logo = 'default'
            id_anterior = 0

            logoL = True if 'logo' in request.FILES else False
            if logoL:
                myfile = request.FILES['logo']
                chu = myfile.chunks()
                st = ''
                file = str(st)
                for chunk in chu:
                    a = chunk
                    file = file + a
                url = guardarDarUrl(file, myfile.name)
                logo = url

            herramienta = Herramienta.objects.create(id_anterior=id_anterior,nombre=nombre,
                                                     sistemaOperativo=sistemaOperativo,plataforma=plataforma,fichaTecnica=fichaTecnica,licencia=licencia,estado=estado,
                                                     revisor1=revisor1, revisor2=revisor2, autor=autor, descripcion=descripcion,urlReferencia=urlReferencia,logo=logo)
            herramienta.save()

            return HttpResponseRedirect(reverse('catalogo:index'))
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
                st = ''
                file = str(st)
                for chunk in chu:
                    a = chunk
                    file = file + a
                url = guardarDarUrl(file, myfile.name)
                logo = url
            id_anterior = pk
            revisor1 = 0
            revisor2 = 0
            estado = 1
            autor = request.user.id

            herramienta_new = Herramienta.objects.create(id_anterior=id_anterior, nombre=nombre,
                                                     sistemaOperativo=sistemaOperativo, plataforma=plataforma,
                                                     fichaTecnica=fichaTecnica, licencia=licencia, estado=estado,
                                                     revisor1=revisor1, revisor2=revisor2, autor=autor,
                                                     descripcion=descripcion, urlReferencia=urlReferencia, logo=logo)
            herramienta_new.save()

            return render(request, 'herramienta_detail.html',{'herramienta': herramienta})
    else:
        form = HerramientaUpdateForm(instance=herramienta)
    return render(request, 'herramienta_update.html', {'form': form, 'id':pk})

def herramienta_delete(request, pk):
    herramienta = Herramienta.objects.get(id=pk)
    if request.method == 'POST':
        herramienta.delete()
        return HttpResponseRedirect(reverse('catalogo:index'))
    return render(request, 'herramienta_delete.html',{'object': herramienta})

def herramienta_detail(request, pk):
    herramienta = Herramienta.objects.get(id=pk)
    context = {'herramienta': herramienta}
    return render(request, 'herramienta_detail.html', context)


def herramientas_estados(request):
    if request.user.is_authenticated():
        herramientas_r = Herramienta.objects.all().filter(estado=1).exclude(autor=request.user.id).exclude(revisor1=request.user.id)
        herramientas_p = Herramienta.objects.all().filter(estado=2)
        context = {'herramientas_r': herramientas_r, 'herramientas_p': herramientas_p}
        return render(request, 'vigia.html', context)
    else:
        herramientas = Herramienta.objects.all().filter(estado=3)
        context = {'herramientas': herramientas}
        return render(request, 'index.html', context)

def herramienta_revisar(request,pk):
    if request.user.is_authenticated():
        herramienta = Herramienta.objects.get(id=pk)
        if herramienta.revisor1 == 0:
            herramienta.revisor1 = request.user.id
        else:
            herramienta.revisor2 = request.user.id
            herramienta.estado = 2
        herramienta.save()
        messages.success(request, 'Revisado con exito', extra_tags='alert alert-success')
        return redirect(reverse('catalogo:vigia'))

    else:
        herramientas = Herramienta.objects.all().filter(estado=3)
        context = {'herramientas': herramientas}
        return render(request, 'index.html', context)

def herramienta_publicar(request,pk):
    if request.user.is_authenticated():
        herramienta = Herramienta.objects.get(id=pk)
        herramienta.estado = 3
        messages.success(request, 'Publicado con exito', extra_tags='alert alert-success')

        print("herramienta.id_anterior" + str(herramienta.id_anterior))
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






#Manejo de cuentas de usuario
def usuario_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            roles = cleaned_data.get('roles')



            user_model = User.objects.create_user(username=username, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.save()

            user = User.objects.get(username=username)
            profile_model = Perfil.objects.get(user_id=user.id)
            profile_model.role = roles[0]

            fotoSubio = True if 'foto' in request.FILES else False
            if fotoSubio:
                myfile = request.FILES['foto']
                chu = myfile.chunks()
                st = ''
                file = str(st)
                for chunk in chu:
                    a = chunk
                    file = file + a
                url = guardarDarUrl(file, myfile.name)
                profile_model.fotoUrl = url

            profile_model.save()

            return HttpResponseRedirect(reverse('catalogo:users_list'))
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user_model = User.objects.get(id=pk)
    if request.method == 'POST':

        form = UserUpdateForm(request.POST, request.FILES, instance=user_model)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            email = cleaned_data.get('email')
            roles = cleaned_data.get('roles')

            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            if user_model.username != username:
                user_model.username = username

            user_model.save()
            print(user_model.username + " " + username)

            profile_model = Perfil.objects.get(user_id=user_model.id)
            fotoSubio = True if 'foto' in request.FILES else False
            if fotoSubio:
                myfile = request.FILES['foto']
                chu = myfile.chunks()
                st = ''
                file = str(st)
                for chunk in chu:
                    a = chunk
                    file = file + a
                url = guardarDarUrl(file, myfile.name)
                profile_model.fotoUrl = url
            profile_model.role = roles[0]
            profile_model.save()
            return HttpResponseRedirect(reverse('catalogo:users_list'))
    else:
        form = UserUpdateForm(instance=user_model)
    return render(request, 'user_update.html', {'form': form})

def user_updateGTI(request, pk):
    user_model = User.objects.get(id=pk)
    if request.method == 'POST':

        form = UserUpdateGTIForm(request.POST, request.FILES, instance=user_model)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            email = cleaned_data.get('email')
            roles = cleaned_data.get('roles')
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            if user_model.username != username:
                user_model.username = username

            user_model.save()
            print(user_model.username + " " + username)

            profile_model = Perfil.objects.get(user_id=user_model.id)
            fotoSubio = True if 'foto' in request.FILES else False
            if fotoSubio:
                myfile = request.FILES['foto']
                chu = myfile.chunks()
                st = ''
                file = str(st)
                for chunk in chu:
                    a = chunk
                    file = file + a
                url = guardarDarUrl(file, myfile.name)
                profile_model.fotoUrl = url
            profile_model.role = roles[0]
            profile_model.save()
            return HttpResponseRedirect(reverse('catalogo:index'))
    else:
        form = UserUpdateGTIForm(instance=user_model)
    return render(request, 'user_update.html', {'form': form})

def user_change_password(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UserChangePassword(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Su contraseña fue exitosamente cambiada!', extra_tags='alert alert-success')
                return HttpResponseRedirect(reverse('catalogo:index'))
        else:
            form = UserChangePassword(request.user)
        return render(request, 'user_change_password.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('catalogo:login'))

def users_list(request):
    if request.user.is_authenticated() and request.user.perfil.role == 1:
        usuarios = User.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'user_list_detail.html', context)


# guardar en AZURE
def guardarDarUrl(file, filemane):
    baseUrl = 'https://catalogo2018storage.blob.core.windows.net/pictures/'
    sas = '?sv=2017-07-29&ss=bf&srt=co&sp=rwdlac&se=2018-05-19T00:27:02Z&st=2018-04-01T16:27:02Z&spr=https,http&sig=iJy3%2BhD2JhuYvXTRfsXT2qTM2p08tfhNGAfb%2BG5YR6w%3D'
    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name=config('ACCOUNT_NAME', default=''),
                                          account_key=config('ACCOUNT_KEY', default=''))

    # Upload the created file, use local_file_name for the blob name
    block_blob_service.create_blob_from_bytes('pictures', filemane, file)

    return baseUrl+filemane+sas