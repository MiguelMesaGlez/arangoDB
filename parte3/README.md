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
I. Búsqueda de los aeropuertos de un país
II. Búsqueda del país de un aeropuerto
III. Modificación de los traits con y sin filtrado
IV. Conocer situación geográfica de los aeropuertos
V. Conocer aeropuertos más cercanos a una persona
VI. Creación índice Geoespacial
VII. Conocer aeropuertos más cercanos a una persona por rango
VIII. Vuelos salientes de un país en concreto


# Consultas AQL
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
  ```batch 
    UPDATE "KeflavikInternationalAirport" 
      WITH { elevation_ft: 182 
      } IN Airports
  ```

  - Delete
  
  ```batch 
    REMOVE "KeflavikInternationalAirport" 
      IN Airports
  ```
  También podemos llevar a cabo la eliminación de todos los documentos de una colección de la siguiente manera:
  
  ```batch 
    FOR airport IN Airports
        REMOVE airport IN Airports      
  ```


#### I.- Búsqueda de los aeropuertos de un país

```batch 
  FOR airports IN Aiports
      FILTER airport.iso_country == "ES"
      RETURN airport.name
 ```

#### II.- Búsqueda del país de un aeropuerto

```batch 
  FOR airports IN Aiports
      FILTER airport.name == "London Luton Airport"
      RETURN airport.iso_country
 ```

#### III.- Modificación de los traits con y sin filtrado
```batch
FOR c IN Travellers
    RETURN MERGE(c, { traits: DOCUMENT("Traits", c.traits)[*].es } )
```
Modificamos el valor de un atributo, de esta manera no es necesario modificar todos los documentos que contienen dicho atributo.
```batch
UPDATE "Y" WITH { en: "efficient" } IN Traits
```
Mostramos nuevamente los viajeros y sus atributos para observar el cambio.
```batch
FOR c IN Travellers
  RETURN MERGE(c, { traits: DOCUMENT("Traits", c.traits)[*].es } )
```

#### IV.- Conocer situación geográfica de los aeropuertos


#### V.- Conocer aeropuertos más cercanos a una persona


#### VI.- Creación de un índice tipo: Geoespacial


#### VII.- Conocer aeropuertos más cercanos  a una persona por rango


#### VII.- Vuelos salientes en modo de grafo de un país

