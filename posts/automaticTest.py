# -- coding: utf-8 --
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\chromedriver.exe")
    # Sebastian añada su ruta por tener mac :c, para el chromedriver

    def test_title(self):
        self.browser.get('localhost:8000')
        self.assertIn('Home CatalogoCTE', self.browser.title)
        self.browser.implicitly_wait(100)