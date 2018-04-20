# -- coding: utf-8 --
from unittest import TestCase


from selenium import webdriver
from selenium.webdriver.common.by import By



class FunctionalTest(TestCase):
    global URL
    # URL = 'https://catalogodevelop.herokuapp.com/'
    URL = 'http://127.0.0.1:8000/'


    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\chromedriver.exe")
        # Sebastian añada su ruta por tener mac :c, para el chromedriver
        # self.browser = webdriver.Chrome("/Users/BarraganJeronimo/PycharmProjects/chromedriver")
        self.browser.implicitly_wait(2)

    def test_1_title(self):
        self.browser.get(URL)
        self.assertIn('Inicio Catalogo', self.browser.title)
        self.browser.close()

    def test_2_login_admin(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        aref = self.browser.find_element_by_id('usuario_loqueado_info')
        self.assertIn('Cuenta: Admin Conecta-te', aref.text)

    def test_3_agregar_herramienta(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('boton_agregar_herramienta').click()
        nombre_herramienta = self.browser.find_element_by_id('id_nombre')
        nombre_herramienta.send_keys("Herramienta Test")
        url_herramienta = self.browser.find_element_by_id('id_urlReferencia')
        url_herramienta.send_keys("www.testHerramienta.com")
        sistema_operativo_herramienta = self.browser.find_element_by_id('id_sistemaOperativo')
        sistema_operativo_herramienta.send_keys("Windows")
        plataforma_herramienta = self.browser.find_element_by_id('id_plataforma')
        plataforma_herramienta.send_keys("Plataforma Test")
        ficha_tecnica_herramienta = self.browser.find_element_by_id('id_fichaTecnica')
        ficha_tecnica_herramienta.send_keys("Ficha Tecnica Test")
        licencia_herramienta = self.browser.find_element_by_id('id_licencia')
        licencia_herramienta.send_keys("Ficha Tecnica Test")
        descripcion_herramienta = self.browser.find_element_by_id('id_descripcion')
        descripcion_herramienta.send_keys("Descripcion Test")
        self.browser.find_element_by_id('boton_add').click()
        a = self.browser.find_element_by_id('Herramienta Test')
        self.assertTrue(a)

    def test_4_editar_herramienta(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('Herramienta Test').click()
        self.browser.find_element_by_id('editar_herramienta_btn').click()
        descripcion_herramienta = self.browser.find_element_by_id('id_nombre')
        descripcion_herramienta.clear()
        descripcion_herramienta.send_keys('Updated_name_test')
        self.browser.find_element_by_id('boton_actualizar_herramienta').click()
        nombre = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Updated_name_test', nombre)

    def test_5_eliminar_herramienta(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('Updated_name_test').click()
        self.browser.find_element_by_id('eliminar_herramienta_btn').click()
        self.browser.find_element_by_id('boton_eliminar_herramienta').click()
        try:
            self.browser.find_element_by_id('Updated_name_test')
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_6_crear_miembro_git(self):
        self.browser.get('localhost:8000')
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('cuentasUsuario').click()
        self.browser.find_element_by_id('boton_crear_usuario').click()
        username_usuario_prueba = self.browser.find_element_by_id('id_username')
        username_usuario_prueba.send_keys("pruebaCrearUsuario")
        nombre_usuario_prueba = self.browser.find_element_by_id('id_first_name')
        nombre_usuario_prueba.send_keys("Crear")
        apellido_usuario_prueba = self.browser.find_element_by_id('id_last_name')
        apellido_usuario_prueba.send_keys("Usuario")
        correo_usuario_prueba = self.browser.find_element_by_id('id_email')
        correo_usuario_prueba.send_keys("prueba@hotmail.com")
        clave_usuario_prueba = self.browser.find_element_by_id('id_password')
        clave_usuario_prueba.send_keys("clavePrueba")
        clave_usuario_prueba_2 = self.browser.find_element_by_id('id_password2')
        clave_usuario_prueba_2.send_keys("clavePrueba")
        roles_usuario_prueba = self.browser.find_element_by_id('id_roles')
        for option in roles_usuario_prueba.find_elements_by_tag_name('option'):
            if option.text == 'Miembro GTI':
                option.click()  # select() in earlier versions of webdriver
                break
        self.browser.find_element_by_id('boton_add_usuario').click()
        creado = self.browser.find_element_by_id('Crear Usuario').text
        self.assertIn('Crear Usuario', creado)

    def test_7_login_miembro_gti(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
        aref = self.browser.find_element_by_id('usuario_loqueado_info')
        print(aref.text)
        self.assertIn('Cuenta: Fabian Medina', aref.text)


    def test_8_agregar_herramienta(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('boton_agregar_herramienta').click()
        nombre_herramienta = self.browser.find_element_by_id('id_nombre')
        nombre_herramienta.send_keys("Herramienta Test")
        url_herramienta = self.browser.find_element_by_id('id_urlReferencia')
        url_herramienta.send_keys("www.testHerramienta.com")
        sistema_operativo_herramienta = self.browser.find_element_by_id('id_sistemaOperativo')
        sistema_operativo_herramienta.send_keys("Windows")
        plataforma_herramienta = self.browser.find_element_by_id('id_plataforma')
        plataforma_herramienta.send_keys("Plataforma Test")
        ficha_tecnica_herramienta = self.browser.find_element_by_id('id_fichaTecnica')
        ficha_tecnica_herramienta.send_keys("Ficha Tecnica Test")
        licencia_herramienta = self.browser.find_element_by_id('id_licencia')
        licencia_herramienta.send_keys("Ficha Tecnica Test")
        descripcion_herramienta = self.browser.find_element_by_id('id_descripcion')
        descripcion_herramienta.send_keys("Descripcion Test creada por Miembro GTI")
        self.browser.find_element_by_id('boton_add').click()
        a = self.browser.find_element_by_id('Herramienta Test')
        self.assertTrue(a)


    def test_9_editar_herramienta_miembro_gti(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('Herramienta Test').click()
        self.browser.find_element_by_id('editar_herramienta_btn').click()
        descripcion_herramienta = self.browser.find_element_by_id('id_nombre')
        descripcion_herramienta.clear()
        descripcion_herramienta.send_keys('Updated_name_test')
        self.browser.find_element_by_id('boton_actualizar_herramienta').click()
        nombre = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Updated_name_test', nombre)


    def test_10_visualizacion_herramienta_usuario_cte(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('Foros de Moodle').click()
        h=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Foros de Moodle', h)
