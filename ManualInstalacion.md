# Manual para la instalcion de la solución
## GITHUB
#### Clone la rama master del repositorio.

## Heroku
#### Crear cuenta de heroku
#### Dirijase a la pagina de [Heroku](https://www.heroku.com/) y cree una cuenta.

#### Una vez haya creado su cuenta, dirijase a el [dashboard](https://dashboard.heroku.com/apps) y cree una nueva aplicación.

#### Asignele un nombre a su aplicación, recordando que debe estar disponible.

#### Una vez creada, busque la opción resources y haga click en esta.

#### En la pestaña resources, para agregar la base de datos postgres, haga click en el boton Find more add-ons, y busque la opcion [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
#### Para obtener las variables de entorno de la base de datos, click en el add-on de heroku-postgres y ubiquese en la pantalla Settings, en este punto debe hacer click en el boton view Credentials. Esto le mostrara un listado de variables de entorno, las cuales debe completar en las variables de entorno que encontrara en los ajustes de su aplicacion en Heroku al hacer click en ```reveal config vars```.

#### Debe completar la variables de entorno de la siguiente forma:
*  ```NAME_DB``` las credenciales de su Database en heroku-postgres
*  ```USER_DB``` las credenciales de su User en heroku-postgres
*  ```PASSWORD_DB``` las credenciales de su Password en heroku-postgres
*  ```HOST_DB```las credenciales de su Host en heroku-postgres
#####
## Azure
#### Cree una cuenta en [Azure](https://azure.microsoft.com/es-es/free/students) , (se aconseja crear la cuenta con las credenciales uniandes, ya que tiene convenios con la plataforma) llene los campos con su informacion. Una vez creada, en el [portal](https://portal.azure.com) en el panel de servicios encontrar"a Cuentas de almacemamiento. 

Agregue una diligenciando el formulario, la creacion tenga en cuenta que el nombre que se le asigne 
se tendra que usar en las variables de entorno. Cuando se le notifique la creacion  entre a 
esta y seleccione los servicio Blobs, y agregue un contenedor llamado ```pictures```, y deje el nivel de acceso en privada. 

Solo resta sacar las variables de entorno nesesarias en la configuracion de heroku, vuelva al almacenamiento creado y 
en configuraciones obtenga las llaves de acceso. 

Tambien debe ir a firma de acceso compartido, en los servicios compatidos selesccione solo blob y en permiosos permitidos solo lectura 
configure un rango de fecha de caducidad adecuado. Lllenaod el formulario puede generar la d=cadena de conexion y sas
#### Debe completar la variables de entorno de la siguiente forma:
*  ```ACCOUNT_NAME``` el nombre de la cuenta de almacenamiento que asignooo
*  ```ACCOUNT_KEY``` clave de algun key en el msnu de claves de accceso 
*  ```SAS``` token sas generado en firma de acceso compartido 
*  ```SORAGE_URL`` https://```nombre del almacenamiento que ud creo```.blob.core.windows.net/pictures/
## Pycharm
