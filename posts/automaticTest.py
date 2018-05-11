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

    def test_01_title(self):
        self.browser.get(URL)
        self.assertIn('Inicio Catalogo', self.browser.title)
        self.browser.close()

    def test_02_login_admin(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_id('cuentasUsuario').click()
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_id('vigia').click()
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.assertIn('Inicio Catalogo', self.browser.title)

    #PRUEBA EN LA QUE EL ADMIN CREA UNA HERRAMIENTA, DOS USUARIOS DISTINTOS GIT LA REVISAN
    # Y EL ADMIN PUBLICA LA EDICION
    def test_03_agregar_herramienta(self):
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
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('palvarado')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('pablo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTA DE ELEMENTOS POR PUBLICAR
        self.browser.find_element_by_id('vigia').click()
    # DETALLE DE ELEMENTO POR PUBLICAR
        self.browser.find_element_by_link_text('Abrir').click()
    # PUBLICACION DE ELEMENTO
        self.browser.find_element_by_id('publicar_herramienta_btn').click()
        self.browser.find_element_by_id('catalogoIndex').click()
        try:
            self.browser.find_element_by_id('Herramienta Test')
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    #PRUEBA EN LA QUE EL ADMIN EDITA UNA HERRAMIENTA, DOS USUARIOS DISTINTOS GIT LA REVISAN
    # Y EL ADMIN PUBLICA LA EDICION
    def test_04_editar_herramienta(self):
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
        descripcion_herramienta.send_keys('Updated name test')
        self.browser.find_element_by_id('boton_actualizar_herramienta').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('palvarado')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('pablo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTA DE ELEMENTOS POR PUBLICAR
        self.browser.find_element_by_id('vigia').click()
    # DETALLE DE ELEMENTO POR PUBLICAR
        self.browser.find_element_by_link_text('Abrir').click()
    # PUBLICACION DE ELEMENTO
        self.browser.find_element_by_id('publicar_herramienta_btn').click()
        self.browser.find_element_by_id('catalogoIndex').click()
        try:
            self.browser.find_element_by_id('Updated name test')
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_05_eliminar_herramienta(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('Updated name test').click()
        self.browser.find_element_by_id('eliminar_herramienta_btn').click()
        nombre_herramienta = self.browser.find_element_by_id('herramienta_name')
        nombre_herramienta.send_keys('Updated name test')
        self.browser.find_element_by_id('eliminar_herramienta_btn_modal').click()
        try:
            self.browser.find_element_by_id('Updated name test')
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test_06_crear_miembro_git(self):
        self.browser.get(URL)
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

    # PRUEBAS MIEMBRO GIT

    def test_07_login_miembro_gti(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('vigia').click()
        self.browser.implicitly_wait(5)
        aref = self.browser.find_element_by_id('usuario_loqueado_info')
        self.assertIn('Cuenta: Fabian Medina', aref.text)

    #PRUEBA EN LA QUE UN MIEMBRO GIT CREA UNA HERRAMIENTA, DOS USUARIOS DISTINTOS GIT LA REVISAN
    # Y EL ADMIN PUBLICA LA EDICION

    def test_08_agregar_herramienta(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('juan')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('sebas9064')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('boton_agregar_herramienta').click()
        nombre_herramienta = self.browser.find_element_by_id('id_nombre')
        nombre_herramienta.send_keys("Crear Test")
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
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('palvarado')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('pablo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTA DE ELEMENTOS POR PUBLICAR
        self.browser.find_element_by_id('vigia').click()
    # DETALLE DE ELEMENTO POR PUBLICAR
        self.browser.find_element_by_link_text('Abrir').click()
    # PUBLICACION DE ELEMENTO
        self.browser.find_element_by_id('publicar_herramienta_btn').click()
        self.browser.find_element_by_id('catalogoIndex').click()
        try:
            self.browser.find_element_by_id('Crear Test')
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)
        self.assertIn('Inicio Catalogo', self.browser.title)
    #PRUEBA EN LA QUE UN MIEMBRO GIT EDITA LA HERRAMIENTA, DOS USUARIOS DISTINTOS GIT LA REVISAN
    # Y EL ADMIN PUBLICA LA EDICION
    def test_09_editar_herramienta_miembro_gti(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('juan')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('sebas9064')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('Crear Test').click()
        self.browser.find_element_by_id('editar_herramienta_btn').click()
        descripcion_herramienta = self.browser.find_element_by_id('id_nombre')
        descripcion_herramienta.clear()
        descripcion_herramienta.send_keys('Updated test')
        self.browser.find_element_by_id('boton_actualizar_herramienta').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('fmedina')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('fmedina2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('palvarado')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('pablo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTADO DE ELEMENTOS EN ESTADO DE REVISION
        self.browser.find_element_by_id('vigia').click()
    # MIEMBRO GIT ACCEDE AL DETALLE DE UN ELEMENTO EN REVISION
        self.browser.find_element_by_link_text('Abrir').click()
    # MIEMBRO GIT REVISA EL ELEMENTO
        self.browser.find_element_by_id('revisar_herramienta_btn').click()
        self.browser.find_element_by_id('usuario_loqueado_info').click()
        self.browser.find_element_by_xpath('//a[@href="/logout/"]').click()
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
    # LISTA DE ELEMENTOS POR PUBLICAR
        self.browser.find_element_by_id('vigia').click()
    # DETALLE DE ELEMENTO POR PUBLICAR
        self.browser.find_element_by_link_text('Abrir').click()
    # PUBLICACION DE ELEMENTO
        self.browser.find_element_by_id('publicar_herramienta_btn').click()
        self.browser.find_element_by_id('catalogoIndex').click()
        try:
            self.browser.find_element_by_id('Updated test')
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_11_visualizacion_herramienta_usuario_cte(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('Sicua plus foros').click()
        self.assertIn('Sicua plus foros', self.browser.title)

    def test_12_editar_miembro_git(self):
        self.browser.get(URL)
        self.browser.find_element_by_id('id_login').click()
        nombre_usuario = self.browser.find_element_by_name('username')
        nombre_usuario.send_keys('admin')
        clave = self.browser.find_element_by_id('password')
        clave.send_keys('catalogo2018')
        self.browser.find_element_by_id('boton_login').click()
        self.browser.find_element_by_id('cuentasUsuario').click()
        self.browser.find_element_by_xpath('//a[@href="/user_update/8"]').click()
        username_usuario_prueba = self.browser.find_element_by_id('id_username')
        username_usuario_prueba.clear()
        username_usuario_prueba.send_keys('Update')
        self.browser.find_element_by_id('cambios').click()
        self.assertIn('Cuentas de usuarios', self.browser.title)