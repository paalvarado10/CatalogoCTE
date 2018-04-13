# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from azure.storage.blob import BlockBlobService
from posts.forms import UserForm, UserUpdateForm, UserChangePassword
from django.contrib.auth.models import User
from django.contrib import messages
from posts.models import Perfil
from decouple import config

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        usuarios = User.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'index.html', context)
    else:
        return HttpResponseRedirect(reverse('catalogo:login'))


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

def addUsuario(request):
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

            return HttpResponseRedirect(reverse('catalogo:index'))
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
            return HttpResponseRedirect(reverse('catalogo:index'))
    else:
        form = UserUpdateForm(instance=user_model)
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