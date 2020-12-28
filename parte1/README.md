# Parte 1: Instalación 🔧

1.  Lo primero que vamos a hacer es crear el directorio para instalar arangoDB en /opt.

```bash
  $ sudo mkdir /opt/arangoDB
  $ sudo chown mbd. /opt/arangoDB
```

2.  Ahora hay que añadir un repositorio apt de arangoDB al sistema. En este caso utilizaremos la version 3.7.X, la última versión disponible en el momento. Desde el repositorio de arangoDB y elegiremos la opción para Ubuntu.

```batch
  $ echo 'deb https://download.arangodb.com/arangodb37/DEBIAN/ /' | sudo tee /etc/apt/sources.list.d/arangodb.list
```

3.  Importamos la GPG key para firmar los paquetes.
```batch
  $ wget -q https://download.arangodb.com/arangodb37/DEBIAN/Release.key -O- | sudo apt-key add - 
```

4.  Actualizar el sistema e instalar arangoDB

```batch
  $ sudo apt update
  $ sudo apt -y install apt-transport-https
  $ sudo apt -y install arangodb3
```
Durante la instalación aparecerán ciertas preguntas sobre la configuración que se utilizará para la instalación. 

   4.1. Configurar la contraseña para root.   
    Introducir la contraseña y confirmarla (password)
    
   4.2.  Seleccionar si actualizar automaticamente los ficheros de la base de datos.
    
   4.3.  Elegir motor de almacenamiento de la base de datos a utilizar. (Este paso no me ha salido)
      auto
      rocksdb
      mmfiles
    
   4.4. Configurar para crear un backup de los archivos de la base de datos antes de hacer una actualización

5. Iniciar arangoDB
```batch
  $ sudo systemctl start arangodb3
  $ sudo systemctl enable arangodb3
```

Para comprobar que se ha inciaciado correctamente, podemos utilizar el siguiente comando y debería aparecer como "running".
```batch
  $ systemctl status arangodb3
```

6. Lanzar la shell de arangoDB
```batch
  $ arangosh
```
