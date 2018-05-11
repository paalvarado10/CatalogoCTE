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
    sistemaOperativo = models.CharField(max_length=80, null=False, blank=False)
    plataforma = models.CharField(max_length=50, null=True, blank=True)
    fichaTecnica = models.CharField(max_length=2000, null=False, blank=False)
    licencia = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.CharField(max_length=520, null=False, blank=False)
    logo = models.CharField(max_length=500, null=False, blank=False)
    revisor1 = models.IntegerField(null=True, blank=True)
    revisor2 = models.IntegerField(null=True, blank=True)
    autor = models.IntegerField(null=False, blank=False)

    PENDIETE_REVISION = 1
    PENDIENTE_PUBLICACION = 2
    PUBLICADO = 3
    BLOQUEADO = 4
    HISTORIC = 5
    BORRADOR = 6
    ESTADO_CHOICES = (
        (PENDIETE_REVISION, 'Pendiente de Revisión'),
        (PENDIENTE_PUBLICACION, 'Pendiente de Publicación'),
        (PUBLICADO, 'Publicado'),
        (BLOQUEADO, 'Bloqueado'),
        (HISTORIC, 'Histórico'),
        (BORRADOR, 'Borrador')
    )
    estado = models.PositiveSmallIntegerField(choices=ESTADO_CHOICES, null=True, blank=True)

    def comparar(self,otra_herramienta):
        return {'id_nombre':self.nombre == otra_herramienta.nombre,
                'id_urlReferencia': self.urlReferencia == otra_herramienta.urlReferencia,
                'id_sistemaOperativo': self.sistemaOperativo == otra_herramienta.sistemaOperativo,
                'id_plataforma': self.plataforma == otra_herramienta.plataforma,
                'id_fichaTecnica': self.fichaTecnica == otra_herramienta.fichaTecnica,
                'id_licencia': self.licencia == otra_herramienta.licencia,
                'id_descripcion' : self.descripcion == otra_herramienta.descripcion,
                'id_logo': self.logo == otra_herramienta.logo}



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
    HISTORIC = 5
    BORRADOR = 6
    ESTADO_CHOICES = (
        (PENDIETE_REVISION, 'Pendiente de Revisión'),
        (PENDIENTE_PUBLICACION, 'Pendiente de Publicación'),
        (PUBLICADO, 'Publicado'),
        (BLOQUEADO, 'Bloqueado'),
        (HISTORIC, 'Histórico'),
        (BORRADOR, 'Borrador')
    )
    estado = models.PositiveSmallIntegerField(choices=ESTADO_CHOICES, null=True, blank=True)


class RecursoActividad(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.CharField(max_length=500, null=False, blank=False)


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


class RecursoTutorial(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, null=False, blank=False)
    descripcion = models.CharField(max_length=500, null=False, blank=False)
