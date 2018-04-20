# -- coding: utf-8 --
from unittest import TestCase


from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        # self.browser = webdriver.Chrome("C:\\Users\\chromedriver.exe")
        # Sebastian añada su ruta por tener mac :c, para el chromedriver
        self.browser = webdriver.Chrome("/Users/BarraganJeronimo/PycharmProjects/chromedriver")
        self.browser.implicitly_wait(2)

    def test_1_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Inicio Catalogo', self.browser.title)
        self.browser.close()

    def test_2_login_admin(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        aref = self.browser.find_element_by_id('usuario_loqueado_info')
        self.assertIn('Cuenta: Admin Conecta-te', aref.text)

    # def test_3_agregar_herramienta(self):
    #     self.browser.get('http://localhost:8000')
    #     self.browser.find_element_by_id('id_login').click()
    #     nombre_usuario = self.browser.find_element_by_name('username')
    #     nombre_usuario.send_keys('admin')
    #     clave = self.browser.find_element_by_id('password')
    #     clave.send_keys('catalogo2018')
    #     self.browser.find_element_by_id('boton_login').click()
    #     self.browser.find_element_by_id('boton_agregar_herramienta').click()
    #     nombre_herramienta = self.browser.find_element_by_id('id_nombre')
    #     nombre_herramienta.send_keys("Herramienta Test")
    #     url_herramienta = self.browser.find_element_by_id('id_urlReferencia')
    #     url_herramienta.send_keys("www.testHerramienta.com")
    #     sistema_operativo_herramienta = self.browser.find_element_by_id('id_sistemaOperativo')
    #     sistema_operativo_herramienta.send_keys("Windows")
    #     plataforma_herramienta = self.browser.find_element_by_id('id_plataforma')
    #     plataforma_herramienta.send_keys("Plataforma Test")
    #     ficha_tecnica_herramienta = self.browser.find_element_by_id('id_fichaTecnica')
    #     ficha_tecnica_herramienta.send_keys("Ficha Tecnica Test")
    #     licencia_herramienta = self.browser.find_element_by_id('id_licencia')
    #     licencia_herramienta.send_keys("Ficha Tecnica Test")
    #     descripcion_herramienta = self.browser.find_element_by_id('id_descripcion')
    #     descripcion_herramienta.send_keys("Descripcion Test")
    #     self.browser.find_element_by_id('boton_add').click()
    #
    #     p = self.browser.find_element(By.XPATH, '//p[text()="Descripcion Test"]')
    #     self.assertIn('Descripcion Test', p.text)
    #
    #
    # def test_4_editar_herramienta(self):
    #     self.browser.get('localhost:8000')
    #     self.browser.find_element_by_id('id_login').click()
    #     nombre_usuario = self.browser.find_element_by_name('username')
    #     nombre_usuario.send_keys('admin')
    #     clave = self.browser.find_element_by_id('password')
    #     clave.send_keys('catalogo2018')
    #     self.browser.find_element_by_id('boton_login').click()
    #     aref = self.browser.find_element_by_xpath('//a[@href="/herramienta_update/491"]').click()
    #     descripcion_herramienta = self.browser.find_element_by_id('id_descripcion')
    #     descripcion_herramienta.send_keys('Sistema para el manejo de la informacion de los estudiantes y sus cursos')
    #     self.browser.find_element_by_id('boton_actualizar_herramienta').click()
    #
    #     p = self.browser.find_element(By.XPATH, '//p[text()="Sistema para el manejo de la informacion de los estudiantes y sus cursos"]')
    #     self.assertIn('Sistema para el manejo de la informacion de los estudiantes y sus cursos', p.text)
    #
    #
    # def test_5_eliminar_herramienta(self):
    #     self.browser.get('localhost:8000')
    #     self.browser.find_element_by_id('id_login').click()
    #     nombre_usuario = self.browser.find_element_by_name('username')
    #     nombre_usuario.send_keys('admin')
    #     clave = self.browser.find_element_by_id('password')
    #     clave.send_keys('catalogo2018')
    #     self.browser.find_element_by_id('boton_login').click()
    #     aref = self.browser.find_element_by_xpath('//a[@href="/herramienta_delete/494"]').click()
    #     self.browser.find_element_by_id('boton_eliminar_herramienta').click()
    #
    #     aref = self.browser.find_element_by_xpath('//a[@href="/logout/"]')
    #     self.assertIn('Salir', aref.text)
    #
    # def test_6_crear_miembro_git(self):
    #     self.browser.get('localhost:8000')
    #     self.browser.find_element_by_id('id_login').click()
    #     nombre_usuario = self.browser.find_element_by_name('username')
    #     nombre_usuario.send_keys('admin')
    #     clave = self.browser.find_element_by_id('password')
    #     clave.send_keys('catalogo2018')
    #     self.browser.find_element_by_id('boton_crear_usuario').click()
    #
    #     username_usuario_prueba = self.browser.find_element_by_id('id_username')
    #     username_usuario_prueba.send_keys("pruebaCrearUsuario")
    #     nombre_usuario_prueba = self.browser.find_element_by_id('id_first_name')
    #     nombre_usuario_prueba.send_keys("Prueba")
    #     apellido_usuario_prueba = self.browser.find_element_by_id('id_last_name')
    #     apellido_usuario_prueba.send_keys("Crear Usuario")
    #     correo_usuario_prueba = self.browser.find_element_by_id('id_email')
    #     correo_usuario_prueba.send_keys("prueba@hotmail.com")
    #     clave_usuario_prueba = self.browser.find_element_by_id('id_password')
    #     clave_usuario_prueba.send_keys("clavePrueba")
    #     clave_usuario_prueba_2 = self.browser.find_element_by_id('id_password2')
    #     clave_usuario_prueba_2.send_keys("clavePrueba")
    #     descripcion_herramienta = self.browser.find_element_by_id('id_roles')
    #     descripcion_herramienta.send_keys("Miembro GTI")
    #     self.browser.find_element_by_id('boton_add_usuario').click()
    #
    #     aref = self.browser.find_element_by_xpath('//li[text="usuario prueba  --- Miembro GTI"]')
    #     self.assertIn('usuario prueba  --- Miembro GTI', aref.text)
    #
    # def test_7_login_miembro_gti(self):
    #     self.browser.get('https://catalogodevelop.herokuapp.com/')
    #     self.browser.find_element_by_id('id_login').click()
    #     nombre_usuario = self.browser.find_element_by_name('username')
    #     nombre_usuario.send_keys('juan')
    #     clave = self.browser.find_element_by_id('password')
    #     clave.send_keys('sebas2018')
    #     self.browser.find_element_by_id('boton_login').click()
    #     aref = self.browser.find_element_by_xpath('//h3[text="Bienvenido Sebastian Barragan Miembro GTI"]')
    #     self.assertIn('Bienvenido Sebastian Barragan Miembro GTI', aref.text)
    #
    #
    # def test_8_agregar_herramienta(self):
    #     self.browser.get('localhost:8000')
    #     self.browser.find_element_by_id('id_login').click()
    #     nombre_usuario = self.browser.find_element_by_name('username')
    #     nombre_usuario.send_keys('juan')
    #     clave = self.browser.find_element_by_id('password')
    #     clave.send_keys('sebas2018')
    #     self.browser.find_element_by_id('boton_login').click()
    #     self.browser.find_element_by_id('boton_agregar_herramienta').click()
    #     nombre_herramienta = self.browser.find_element_by_id('id_nombre')
    #     nombre_herramienta.send_keys("Herramienta Test Miembro GTI")
    #     url_herramienta = self.browser.find_element_by_id('id_urlReferencia')
    #     url_herramienta.send_keys("www.testHerramienta.com")
    #     sistema_operativo_herramienta = self.browser.find_element_by_id('id_sistemaOperativo')
    #     sistema_operativo_herramienta.send_keys("Windows")
    #     plataforma_herramienta = self.browser.find_element_by_id('id_plataforma')
    #     plataforma_herramienta.send_keys("Plataforma Test")
    #     ficha_tecnica_herramienta = self.browser.find_element_by_id('id_fichaTecnica')
    #     ficha_tecnica_herramienta.send_keys("Ficha Tecnica Test")
    #     licencia_herramienta = self.browser.find_element_by_id('id_licencia')
    #     licencia_herramienta.send_keys("Ficha Tecnica Test")
    #     descripcion_herramienta = self.browser.find_element_by_id('id_descripcion')
    #     descripcion_herramienta.send_keys("Descripcion Test creada por Miembro GTI")
    #     self.browser.find_element_by_id('boton_add').click()
    #
    #     p = self.browser.find_element(By.XPATH, '//p[text()="Descripcion Test creada por Miembro GTI"]')
    #     self.assertIn('Descripcion Test creada por Miembro GTI', p.text)
    #
    #
    # def test_9_editar_herramienta_miembro_gti(self):
    #     self.browser.get('localhost:8000')
    #     self.browser.find_element_by_id('id_login').click()
    #     nombre_usuario = self.browser.find_element_by_name('username')
    #     nombre_usuario.send_keys('juan')
    #     clave = self.browser.find_element_by_id('password')
    #     clave.send_keys('sebas2018')
    #     self.browser.find_element_by_id('boton_login').click()
    #     aref = self.browser.find_element_by_xpath('//a[@href="/herramienta_update/491"]').click()
    #     descripcion_herramienta = self.browser.find_element_by_id('id_descripcion')
    #     descripcion_herramienta.send_keys('Sistema para el manejo de la informacion de los estudiantes y sus cursos (prueba)')
    #     self.browser.find_element_by_id('boton_actualizar_herramienta').click()
    #
    #     p = self.browser.find_element(By.XPATH, '//p[text()="Sistema para el manejo de la informacion de los estudiantes y sus cursos (prueba)"]')
    #     self.assertIn('Sistema para el manejo de la informacion de los estudiantes y sus cursos (prueba)', p.text)
    #
    # def test_10_visualizacion_herramienta_usuario_cte(self):
    #     self.browser.get('localhost:8000')
    #     aref = self.browser.find_element_by_name('boton_detalle')
    #     self.assertIn('Ver detalle', aref.text)
