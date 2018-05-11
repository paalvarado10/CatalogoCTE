from django.shortcuts import render
from posts.models import Herramienta


def borradores_list(request):
    if request.user.is_authenticated():
        herramientas_b = Herramienta.objects.all().filter(estado=6).filter(autor=request.user.id)
        context = {'herramientas_b': herramientas_b}
        return render(request, 'borradores_list_detail.html', context)
    else:
        herramientas = Herramienta.objects.all().filter(estado=3)
        context = {'herramientas': herramientas}
        return render(request, 'index.html', context)
