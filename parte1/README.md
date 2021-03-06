# Parte 1: Instalación 🔧

Dependiendo del sistema operativo que posea su ordenador, deberá tener en cuenta una serie de factores para realizar la correcta instalación de ArangoDB. Se puede acceder a más información y descargar los paquetes necesarios para la instalacion seleccionando el sistema operativo deseado en el siguiente link: https://www.arangodb.com/download-major/ 

## Linux (linea de comando)

1.  Lo primero que vamos a hacer es añadir un repositorio apt de arangoDB al sistema. En este caso utilizaremos la version 3.7.X, la última versión disponible en el momento. Desde el repositorio de arangoDB y elegiremos la opción para Ubuntu.

    ```
      $ echo 'deb https://download.arangodb.com/arangodb37/DEBIAN/ /' | sudo tee /etc/apt/sources.list.d/arangodb.list
    ```

2.  Importamos la GPG key para firmar los paquetes.
    ```
      $ wget -q https://download.arangodb.com/arangodb37/DEBIAN/Release.key -O- | sudo apt-key add - 
    ```

3.  Actualizar el sistema e instalar arangoDB

    ```
      $ sudo apt update
      $ sudo apt -y install apt-transport-https
      $ sudo apt -y install arangodb3
    ```
    Durante la instalación aparecerán ciertas preguntas sobre la configuración que se utilizará para la instalación. 

    * Configurar la contraseña para root. Introducir la contraseña y confirmarla (password)
      
      <kbd>
        <img src="https://github.com/MiguelMesaGlez/arangoDB/blob/main/ficherosAdicionales/imagenes/configuracion1.png" width="750">
      </kbd>
     
    * Seleccionar si actualizar automaticamente los ficheros de la base de datos.
      
      <kbd> 
        <img src="https://github.com/MiguelMesaGlez/arangoDB/blob/main/ficherosAdicionales/imagenes/configuracion3.png" width="750">
      </kbd>
     
    * Elegir motor de almacenamiento de la base de datos a utilizar.
      * auto
      * rocksdb (default)
      * mmfiles
    
    * Configurar para crear un backup de los archivos de la base de datos antes de hacer una actualización
      
      <kbd>
        <img src="https://github.com/MiguelMesaGlez/arangoDB/blob/main/ficherosAdicionales/imagenes/configuracion4.png" width="750">
      </kbd>

4. Iniciar arangoDB
   ```
     $ sudo systemctl start arangodb3
     $ sudo systemctl enable arangodb3
   ```

   Para comprobar que se ha inciaciado correctamente, podemos utilizar el siguiente comando:
   ```
     $ systemctl status arangodb3
   ```
   Una vez ejecutado, se mostrará la siguiente información por pantalla y comprobaremos que el estado sea **active(running)**.
   ```
   ● arangodb3.service - ArangoDB database server
        Loaded: loaded (/lib/systemd/system/arangodb3.service; enabled; vendor preset: enabled)
        Active: active (running) since Mon 2020-12-28 20:28:54 CET; 4 days ago
       Process: 657 ExecStartPre=/usr/bin/install -g arangodb -o arangodb -d /var/tmp/arangodb3 (code=exited, status=0/SUCCESS)
       Process: 661 ExecStartPre=/usr/bin/install -g arangodb -o arangodb -d /var/run/arangodb3 (code=exited, status=0/SUCCESS)
       Process: 666 ExecStartPre=/usr/bin/env chown -R arangodb:arangodb /var/log/arangodb3 (code=exited, status=0/SUCCESS)
       Process: 679 ExecStartPre=/usr/bin/env chmod 700 /var/log/arangodb3 (code=exited, status=0/SUCCESS)
       Process: 683 ExecStartPre=/usr/bin/env chown -R arangodb:arangodb /var/lib/arangodb3 (code=exited, status=0/SUCCESS)
       Process: 686 ExecStartPre=/usr/bin/env chmod 700 /var/lib/arangodb3 (code=exited, status=0/SUCCESS)
       Process: 691 ExecStartPre=/usr/bin/env chown -R arangodb:arangodb /var/lib/arangodb3-apps (code=exited, status=0/SUCCESS)
       Process: 693 ExecStartPre=/usr/bin/env chmod 700 /var/lib/arangodb3-apps (code=exited, status=0/SUCCESS)
      Main PID: 696 (arangod)
         Tasks: 28 (limit: 131072)
        Memory: 2.2G
        CGroup: /system.slice/arangodb3.service
                └─696 /usr/sbin/arangod --uid arangodb --gid arangodb --pid-file /var/run/arangodb3/arangod.pid --temp.path /var/tmp/arangodb3 --log.foreground-tty true

   dic 28 20:28:58 mbd-VirtualBox arangod[696]: 2020-12-28T19:28:58Z [696] INFO [3bb7d] {cluster} Starting up with role SINGLE
   dic 28 20:28:59 mbd-VirtualBox arangod[696]: 2020-12-28T19:28:59Z [696] INFO [6ea38] using endpoint 'http+tcp://127.0.0.1:8529' for non-encrypted requests
   dic 28 20:28:59 mbd-VirtualBox arangod[696]: 2020-12-28T19:28:59Z [696] INFO [a1c60] {syscall} file-descriptors (nofiles) hard limit is 131072, soft limit is 131072
   dic 28 20:28:59 mbd-VirtualBox arangod[696]: 2020-12-28T19:28:59Z [696] INFO [3844e] {authentication} Authentication is turned on (system only), authentication for unix sockets>
   dic 28 20:28:59 mbd-VirtualBox arangod[696]: 2020-12-28T19:28:59Z [696] WARNING [b387d] found existing lockfile '/var/lib/arangodb3/LOCK' of previous process with pid 5925, but>
   dic 28 20:29:09 mbd-VirtualBox arangod[696]: 2020-12-28T19:29:09Z [696] INFO [c1b63] {arangosearch} ArangoSearch maintenance: [1..1] commit thread(s), [1..1] consolidation thre>
   dic 28 20:29:10 mbd-VirtualBox arangod[696]: 2020-12-28T19:29:09Z [696] INFO [cf3f4] ArangoDB (version 3.7.5 [linux]) is ready for business. Have fun!
   ene 01 15:07:58 mbd-VirtualBox arangod[696]: 2021-01-01T14:07:44Z [696] WARNING [3ad54] {engines} slow background settings sync: 3.767773 s
   ene 01 15:07:58 mbd-VirtualBox arangod[696]: 2021-01-01T14:07:58Z [696] WARNING [8bcee] {queries} slow query: 'FOR s in @@collection FILTER s.time >= @start SORT s.time DESC LI>
   ene 01 22:35:41 mbd-VirtualBox arangod[696]: 2021-01-01T21:35:41Z [696] WARNING [3ad54] {engines} slow background settings sync: 1.138017 s
   ```

5. Lanzar la shell de arangoDB
   ```
     $ arangosh
   ```
   Una vez ejecutado este comando solo será necasario introducir la contraseña para el usuario root que hemos creado durante la instalación para acceder a la shell de ArangoDB
   ```
   Please specify a password: 

                                           _     
     __ _ _ __ __ _ _ __   __ _  ___  ___| |__  
    / _` | '__/ _` | '_ \ / _` |/ _ \/ __| '_ \ 
   | (_| | | | (_| | | | | (_| | (_) \__ \ | | |
    \__,_|_|  \__,_|_| |_|\__, |\___/|___/_| |_|
                           |___/                 

   arangosh (ArangoDB 3.7.5 [linux] 64bit, using jemalloc, build tags/v3.7.5-0-g265062801f, VPack 0.1.33, RocksDB 6.8.0, ICU 64.2, V8 7.9.317, OpenSSL 1.1.1h  22 Sep 2020)
   Copyright (c) ArangoDB GmbH

   Command-line history will be persisted when the shell is exited. You can use `--console.history false` to turn this off
   Connected to ArangoDB 'http+tcp://127.0.0.1:8529, version: 3.7.5 [SINGLE, server], database: '_system', username: 'root'

   Type 'tutorial' for a tutorial or 'help' to see common examples
   127.0.0.1:8529@_system> 
   ```

<br>

## MacOS

1. Antes de nada, deberá tener instalado el paquete brew para realizar la instalación, para ello debemos ejecutar el siguiente comando
  
   ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   Se podrá encontrar más información en la siguiente url https://brew.sh/index_es

2. Para realizar la instalación de ArangoDB en el sistema operativo MacOS deberemos ejecutar el siguiente comando en un terminal del ordenador, y se instalará la última version estable de la misma.                  

   ```
     brew install arangodb
   ```
 
3. Para realizar la creación de la instancia de ArangoDB en el sistema operativo MacOS deberemos ejecutar el siguiente comando en un terminal del ordenador, y se instalará la última version estable de la misma.                  

   ``` 
     /usr/local/Cellar/arangodb/<VERSION>/sbin/arangod &
   ```  
  
4. El archivo para modificar la configuración predeterminada de ArangoDB es arango.conf, en el encontraremos detallados los parametros que podremos modificar en caso de ser necesario, accederemos a él mediante el siguiente comando:
  
   ```      
     /usr/local/etc/arangodb3/arangod.conf
   ```
  
5. Por otra parte, para finalizar con la instación, en caso de querer ejecutar arango desde el termina, deberemos instalar el Shell, para lo cual ejecutaremos la siguiente línea:
  
   ```
     /usr/local/Cellar/arangodb/<VERSION>/bin/arangosh
   ```
   

 6. Para lanzar una instancia de Arango una vez que lo tengamos instalado deberemos ejecutar el siguiente comando

    ``` 
      /usr/local/sbin/arangod &
    ```

    Si prefirieramos llevar a cabo la consultas y operaciones que realicemos a través de la interfaz web, deberemos lanzar el siguiente comando,   el cual nos permitirá acceder a la dirección *localhost:8529* y obtendremos una página donde introduciremos el usuario root sin contraseña para poder empezar a trabajar.

    ``` 
        arangosh
    ```

    En caso de querer parar la instancia lanzada de Arangodb, únicamente deberemos parar el proceso, para esto ejecutaremos el siguiente comando

    ``` 
        sudo brew services stop arangodb
    ```

    o en su defecto
    
    ``` 
        brew services stop arangodb
    ```
     
    Se podrá encontrar más información en la siguiente url https://www.arangodb.com/docs/stable/installation-mac-osx.html

<br>

## Windows 

1.  Para realizar la instalación de ArangoDB en Windows se necesita descargar el Paquete NSIS que contiene dos archivos.
    - Servidor 3.7.5
    - Herramientas cliente 3.7.5

2.  Al descargar el primer archivo, obtienes una ventanilla para iniciar la instalación del interfaz ArangoDB 3.7.5.

    <kbd>
      <img src="https://github.com/MiguelMesaGlez/arangoDB/blob/main/ficherosAdicionales/imagenes/window1.png" width="400" >
    </kbd>

3.  La instalación tiene una duración de 2 a 5 minutos y tienes que registrar una contraseña para poder iniciar más adelante y por default, el usuario es root y el programa crea un acceso directo en tu escritorio de Windows.

    <kbd>
      <img src="https://github.com/MiguelMesaGlez/arangoDB/blob/main/ficherosAdicionales/imagenes/window2.png" width="400" >
    </kbd>

4.  En el segundo archivo obtienes las herramientas clientes de ArangoDB, la cual te abre una ventana azul para seguir con las instrucciones.

    <kbd>
      <img src="https://github.com/MiguelMesaGlez/arangoDB/blob/main/ficherosAdicionales/imagenes/window3.png" width="400" >
    </kbd>

5.  Una vez instalado, te permite iniciar Arango DB iniciando primero la contraseña que hemos registrado en la instalación.

    <kbd>
      <img src="https://github.com/MiguelMesaGlez/arangoDB/blob/main/ficherosAdicionales/imagenes/window4.png" width="400" >
    </kbd>
