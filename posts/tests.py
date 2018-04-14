# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from posts.models import TestModel, Herramienta


# Create your tests here.
class TestModelTestCase(TestCase):
    def setUp(self):
        TestModel.objects.create(nombre = 'name')

    def test_full_name(self):
        tester = TestModel.objects.get(nombre='name')
        self.assertEqual(tester.full_name(), 'name')



class HerramientaModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(version = "Version Prueba",nombre = "prueba", urlReferencia="www.google.com",sistemaOperativo="Windows",plataforma="Plataforma Prueba",fichaTecnica="Ficha tecnica prueba",licencia="gratis",estado=1,revisiones=0)
#
    def test_estado_herramienta(self):
        tester = Herramienta.objects.get(nombre ='prueba')
        self.assertEqual(tester.estado_herramienta(), 1)

    def test_nombre_herramienta(self):
        tester = Herramienta.objects.get(nombre ='prueba')
        self.assertEqual(tester.nombre_herramienta(), 'prueba')


