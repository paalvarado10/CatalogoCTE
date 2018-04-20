# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Herramienta(models.Model):
    id_anterior = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    urlReferencia = models.CharField(max_length=500, null=False, blank=False)
    sistemaOperativo = models.CharField(max_length=50, null=False, blank=False)
    plataforma = models.CharField(max_length=50, null=True, blank=True)
    fichaTecnica = models.CharField(max_length=2000, null=False, blank=False)
    licencia = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.CharField(max_length=2000, null=False, blank=False)
    logo = models.CharField(max_length=500, null=False, blank=False)
    revisor1 = models.IntegerField(null=True, blank=True)
    revisor2 = models.IntegerField(null=True, blank=True)
    autor = models.IntegerField(null=False, blank=False)

    PENDIETE_REVISION = 1
    PENDIENTE_PUBLICACION = 2
    PUBLICADO = 3
    BLOQUEADO = 4
    ESTADO_CHOICES = (
        (PENDIETE_REVISION, 'Pendiente de Revisión'),
        (PENDIENTE_PUBLICACION, 'Pendiente de Publicación'),
        (PUBLICADO, 'Publicado'),
        (BLOQUEADO, 'Bloqueado'),
    )
    estado = models.PositiveSmallIntegerField(choices=ESTADO_CHOICES, null=True, blank=True)


    def __unicode__(self):
        return self or u''

    def nombre_herramienta(self):
        return self.nombre

    def estado_herramienta(self):
        return self.estado

    def version_herramienta(self):
        return self.version

    def url_herramienta(self):
        return self.urlReferencia

    def sistemaOperativo_herramienta(self):
        return self.sistemaOperativo

    def plataforma_herramienta(self):
        return self.plataforma

    def ficha_herramienta(self):
        return self.fichaTecnica

    def licencia_herramienta(self):
        return self.licencia

    def descripcion_herramienta(self):
        return self.descripcion

    def logo_herramienta(self):
        return self.logo


class Perfil(models.Model):
    ADMINISTRADOR = 1
    USER_GTI = 2
    ROLE_CHOICES = (
        (ADMINISTRADOR, 'Administrador'),
        (USER_GTI, 'Miembro GTI'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fotoUrl = models.CharField(max_length=500, null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()


class Actividad(models.Model):
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    id_anterior = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=500, null=False, blank=False)
    instrucciones = models.CharField(max_length=500, null=False, blank=False)
    url = models.CharField(max_length=200, null=True, blank=True)

    revisor1 = models.IntegerField(null=True, blank=True)
    revisor2 = models.IntegerField(null=True, blank=True)
    autor = models.IntegerField(null=False, blank=False)

    PENDIETE_REVISION = 1
    PENDIENTE_PUBLICACION = 2
    PUBLICADO = 3
    BLOQUEADO = 4
    ESTADO_CHOICES = (
        (PENDIETE_REVISION, 'Pendiente de Revisión'),
        (PENDIENTE_PUBLICACION, 'Pendiente de Publicación'),
        (PUBLICADO, 'Publicado'),
        (BLOQUEADO, 'Bloqueado'),
    )
    estado = models.PositiveSmallIntegerField(choices=ESTADO_CHOICES, null=True, blank=True)

    def __unicode__(self):
        return self

    def herramienta_actividad(self):
        return self.herramienta.nombre

    def version_actividad(self):
        return self.version

    def nombre_actividad(self):
        return self.nombre

    def descripcion_actividad(self):
        return self.descripcion

    def instrucciones_actividad(self):
        return self.instrucciones

    def url_actividad(self):
        return self.url

    def estado_actividad(self):
        return self.estado



class RecursoActividad(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.CharField(max_length=500, null=False, blank=False)


    def __unicode__(self):
        return self

    def url_recurso_actividad(self):
        return self.url

    def descripcion_recurso_actividad(self):
        return self.descripcion

    def actividad_recurso_actividad(self):
        return self.actividad.nombre



class Tutorial(models.Model):
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    id_anterior = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    funcionalidad = models.CharField(max_length=500, null=False, blank=False)
    revisor1 = models.IntegerField(null=True, blank=True)
    revisor2 = models.IntegerField(null=True, blank=True)
    autor = models.IntegerField(null=False, blank=False)
    PENDIETE_REVISION = 1
    PENDIENTE_PUBLICACION = 2
    PUBLICADO = 3
    BLOQUEADO = 4
    ESTADO_CHOICES = (
        (PENDIETE_REVISION, 'Pendiente de Revisión'),
        (PENDIENTE_PUBLICACION, 'Pendiente de Publicación'),
        (PUBLICADO, 'Publicado'),
        (BLOQUEADO, 'Bloqueado'),
    )
    estado = models.PositiveSmallIntegerField(choices=ESTADO_CHOICES, null=True, blank=True)
    revisor1 = models.IntegerField(null=True, blank=True)
    revisor2 = models.IntegerField(null=True, blank=True)
    autor = models.IntegerField(null=False, blank=False)

    def __unicode__(self):
        return self

    def herramienta_tutorial(self):
        return self.herramienta.nombre

    def version_tutorial(self):
        return self.version

    def nombre_tutorial(self):
        return self.nombre

    def funcionalidad_tutorial(self):
        return self.funcionalidad

    def estado_tutorial(self):
        return self.estado


class RecursoTutorial(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.CharField(max_length=500, null=False, blank=False)

    def __unicode__(self):
        return self

    def tutorial_recurso_tutorial(self):
        return self.tutorial.nombre

    def url_recurso_tutorial(self):
        return self.url

    def descripcion_recurso_tutorial(self):
        return self.descripcion
