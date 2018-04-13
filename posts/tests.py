# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from posts.models import TestModel

# Create your tests here.
class TestModelTestCase(TestCase):
    def setUp(self):
        TestModel.objects.create(nombre = "Nombre1")