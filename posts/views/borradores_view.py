from django.shortcuts import render
from posts.models import Herramienta, Actividad


def borradores_list(request):
    if request.user.is_authenticated():
        herramientas_b = Herramienta.objects.all().filter(estado=6).filter(autor=request.user.id)
        actividades_b = Actividad.objects.all().filter(estado=6).filter(autor=request.user.id)
        context = {'herramientas_b': herramientas_b, 'actividades_b': actividades_b}
        return render(request, 'borradores_list_detail.html', context)
    else:
        herramientas = Herramienta.objects.all().filter(estado=3)
        actividades_b = Actividad.objects.all().filter(estado=6)
        context = {'herramientas': herramientas, 'actividades_b': actividades_b}
        return render(request, 'index.html', context)
