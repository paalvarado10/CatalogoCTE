# -- coding: utf-8 --
from unittest import TestCase

import sys
from selenium import webdriver
# from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\chromedriver.exe")
    # Sebastian añada su ruta por tener mac :c, para el chromedriver
        self.browser.implicitly_wait(2)

    def test_1_title(self):
        self.browser.get('localhost:8000')
        self.assertIn('Home CatalogoCTE', self.browser.title)
        self.browser.close()

    def test_2_login_admin(self):
        self.browser.get('localhost:8000')
        self.browser.find_element_by_id('id_login').click()
        nombreUsuario = self.browser.find_element_by_name('username')
        nombreUsuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        aref = self.browser.find_element_by_xpath('//a[@href="/logout/"]')
        self.assertIn('Salir', aref.text)