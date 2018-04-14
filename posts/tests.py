# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from posts.models import TestModel, Herramienta, Actividad, RecursoActividad


# Create your tests here.
class TestModelTestCase(TestCase):
    def setUp(self):
        TestModel.objects.create(nombre='name')

    def test_full_name(self):
        tester = TestModel.objects.get(nombre='name')
        self.assertEqual(tester.full_name(), 'name')


# TEST MODELO HERRAMIENTA
class HerramientaModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(version="Version Prueba", nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba", fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, revisiones=0, logo="logo")

    def test_estado_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.estado_herramienta(), 1)

    def test_nombre_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
        self.assertEqual(tester.nombre_herramienta(), 'prueba')

    def test_version_herramienta(self):
        tester = Herramienta.objects.get(nombre='prueba')
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


# TEST PARA EL MODELO DE ACTIVIDAD
class ActividadModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(version="Version Prueba", nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba", fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, revisiones=0, logo="logo")
        herramienta=Herramienta.objects.get(nombre='prueba')
        Actividad.objects.create(herramienta=herramienta, version="Version Prueba", nombre="actividadprueba", descripcion="descActividad", instrucciones="instruccionesPrueba", url="www.actividad.com", estado=1, revisiones=0)

    def test_version_actividad(self):
        tester=Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.version_actividad(), 'Version Prueba')

    def test_descripcion_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.descripcion_actividad(), 'descActividad')

    def test_instrucciones_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.instrucciones_actividad(), 'instruccionesPrueba')

    def test_url_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.url_actividad(), 'www.actividad.com')

    def test_estado_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.estado_actividad(), 1)

    def test_revisiones_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.revisiones_actividad(), 0)

    def test_herramienta_actividad(self):
        tester = Actividad.objects.get(nombre='actividadprueba')
        self.assertEqual(tester.herramienta_actividad(), 'prueba')


# TEST RECURSO ACTIVIDAD
class RecursoActividadModelCase(TestCase):
    def setUp(self):
        Herramienta.objects.create(version="Version Prueba", nombre="prueba", urlReferencia="www.google.com", sistemaOperativo="Windows", plataforma="Plataforma Prueba", fichaTecnica="Ficha tecnica prueba", descripcion="desc", licencia="gratis", estado=1, revisiones=0, logo="logo")
        herramienta=Herramienta.objects.get(nombre ='prueba')
        Actividad.objects.create(herramienta=herramienta, version="Version Prueba", nombre="actividadprueba", descripcion="descActividad", instrucciones="instruccionesPrueba", url="www.actividad.com", estado=1, revisiones=0)
        actividad=Actividad.objects.get(nombre='actividadprueba')
        RecursoActividad.objects.create(actividad=actividad, url="www.recurso.com", descripcion="descRecurso")

    def test_actividad_recurso_actividad(self):
        tester = RecursoActividad.objects.get(descripcion='descRecurso')
        self.assertEqual(tester.actividad_recurso_actividad(), 'actividadprueba')

    def test_url_recurso_actividad(self):
        tester = RecursoActividad.objects.get(descripcion='descRecurso')
        self.assertEqual(tester.url_recurso_actividad(), 'www.recurso.com')

    def test_descripcion_recurso_actividad(self):
        tester = RecursoActividad.objects.get(descripcion='descRecurso')
        self.assertEqual(tester.descripcion_recurso_actividad(), 'descRecurso')
