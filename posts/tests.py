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
        Herramienta.objects.create(version = "Version Prueba",nombre = "prueba", urlReferencia="www.google.com",sistemaOperativo="Windows",plataforma="Plataforma Prueba",fichaTecnica="Ficha tecnica prueba",descripcion="desc", licencia="gratis",estado=1,revisiones=0, logo="logo")
#
    def test_estado_herramienta(self):
        tester = Herramienta.objects.get(nombre ='prueba')
        self.assertEqual(tester.estado_herramienta(), 1)

    def test_nombre_herramienta(self):
        tester = Herramienta.objects.get(nombre ='prueba')
        self.assertEqual(tester.nombre_herramienta(), 'prueba')

    def test_version_herramienta(self):
        tester = Herramienta.objects.get(nombre ='prueba')
        self.assertEqual(tester.version_herramienta(), 'Version Prueba')

    def test_url_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.url_herramienta(), 'www.google.com')

    def test_sistemaOperativo_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.sistemaOperativo_herramienta(), 'Windows')

    def test_plataforma_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.plataforma_herramienta(), 'Plataforma Prueba')

    def test_ficha_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.ficha_herramienta(), 'Ficha tecnica prueba')

    def test_licencia_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.licencia_herramienta(), 'gratis')

    def test_descripcion_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.descripcion_herramienta(), 'desc')

    def test_logo_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.logo_herramienta(), 'logo')

