# -*- coding: utf-8 -*-
from django.shortcuts import render
from posts.models import Herramienta


def index(request):
    herramientas = Herramienta.objects.all()
    context = {'herramientas': herramientas}
    return render(request, 'index.html', context)
