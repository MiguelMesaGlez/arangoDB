# Parte 1: Instalación
Comenzaremos por intalar la Community Edition de ArangoDB para Ubuntu, ya que vamos a realizar la instalación en nuestra máquina virtual. (Enterprise Edition solo da 2 semanas de prueba gratis y además solo incluye algunas funcionalidades adicionales) 

1. Lo primero que vamos a hacer es crear el directorio para instalar arangoDB en /opt.

```bash
$ sudo mkdir /opt/arangoDB
$ sudo chown mbd. /opt/arangoDB
```

2. Ahora hay que descargar la versión de arangoDB que queramos instalar. En este caso utilizaremos la version 3.7.5, la última versión disponible en el momento. Desde la site de arangoDB: https://www.arangodb.com/download-major/ y elegiremos la opción para Ubuntu. 
Tenemos que descargar el Server en el que se incluye todo lo necesario para instalar arangoDB, iniciar un servidor y acceder a este con las herramientas del cliente. (El Cliente solo contiene las herramientas para acceder a un servidor)

```bash
cd /opt/arangoDB
$ mv ~/Downloads/arangoDB3-linux-3.7.5.tar.gz .
$ tar -xvzf arangoDB3-linux-3.7.5.tar.gz
$ ln -s arangoDB3-linux-3.7.5 arangoDB
```

3. Antes de ralizar la instalación 
```bash
echo arangodb3 arangodb/password password arangoDB | debconf-set-selections
echo arangodb3 arangodb3/password_again password arangoDB | debconf-set-selections
```

3. Modificamos los ficheros de configuración (?)
