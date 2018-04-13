# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

def index(request):
    return render(request, 'index.html')


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