# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class TestModel(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)

class Herramienta(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    urlReferencia = models.CharField(max_length=500, null=False, blank=False)
    sistemaOperativo = models.CharField(max_length=50, null=False, blank=False)
    plataforma = models.CharField(max_length=50, null=True, blank=True)
    fichaTecnica = models.CharField(max_length=200, null=False, blank=False)
    licencia = models.CharField(max_length=200, null=False, blank=False)

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
    revisiones = models.IntegerField(null=False, blank=False)


# Perfiles de Usuario
# ADMINISTRADOR: Administrador general de la aplicación
# CREADOR: Usuario c-te creador de contenidos
# REVISOR: Usuario c-te revisor borradores (también puede crear contenidos)
class Perfil(models.Model):
    ADMINISTRADOR = 1
    CREADOR = 2
    REVISOR = 3
    ROLE_CHOICES = (
        (ADMINISTRADOR, 'Administrador'),
        (CREADOR, 'MIEBROGIT'),
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