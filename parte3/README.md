# Parte III: Demo 🛠️

### Antes de comenzar

Primeros pasos antes de comenzar la DEMO, a continuación realizaremos una serie de operaciones necesarias para llevar a cabo la posterior realización de consultas en nuestra base de datos, para ello deberemos realizar lo siguiente:

  - Ingresaremos a *localhost:8529* como **root** 
  - Creación de base de datos **Airports**
  - Creación de un nuevo usuario 
    ej. userArango password: mypwd
  - Concesión de permisos sobre este nuevo usuario
  - Exit de la base de datos _system
  - Exit como usuario **root**
  - Ingresamos a "localhost:8529" como **userArango**
  - Seleccionamos la base de datos **Airports** para trabajar sobre ella

En segundo lugar realizaremos una serie de consultas para probar la potencia que puede llegar a alcanzar ArangoDB, asi como para conocer el tipo de consultas que podemos realizar con los datos seleccionados.

### Índice de consultas AQL

0. Operaciones CRUD básicas
1. Búsqueda de los aeropuertos de un país
2. Búsqueda del país de un aeropuerto
3. Modificación de los traits filtrando por un campo y añadir .campo
4. Conocer situación geográfica de los aeropuertos
5. Conocer aeropuertos más cercanos a una persona
6. Creación índice Geoespacial
7. Conocer aeropuertos más cercanos a una persona por rango
8. Vuelos salientes de un país en concreto



#### 0.- Operaciones CRUD básicas

  - Create
  ```batch
      INSERT {  
          "_key": "KeflavikInternationalAirport",
          "type": "large_airport",
          "name": "Keflavik International Airport",
          "latitude_deg": 63.9850006103516,
          "longitude_deg": -22.605600357055696,
          "elevation_ft": 171,
          "continent": "EU",
          "iso_country": "IS",
          "iso_region": "IS-2",
          "municipality": "Reykjavík",
          "coordinates":[63.9850006103516, -22.605600357055696]
      } INTO Airports
  ```
  - Read
  ```batch
    FOR airport IN Airports
      RETURN airport
  ```

  - Update
  ```
  UPDATE "KeflavikInternationalAirport" 
      WITH { elevation_ft: 182 
      } IN Airports
  ```

  - Delete
  
  ```
  REMOVE "KeflavikInternationalAirport" 
  IN Airports
  ```
  También podemos llevar a cabo la eliminación de todos los documentos de una colección de la siguiente manera:
  
  ```FOR airport IN Airports
        REMOVE airport IN Airports      
  ```


#### 1.- Búsqueda de los aeropuertos de un país



#### 2.- Búsqueda del país de un aeropuerto



#### 3.- Modificación de los traits filtrando


#### 4.- Conocer situación geográfica de los aeropuertos


#### 5.- Conocer aeropuertos más cercanos a una persona


#### 6.- Creación de un índice tipo: Geoespacial


#### 7.- Conocer aeropuertos más cercanos  a una persona por rango


#### 8.- Vuelos salientes en modo de grafo de un país

