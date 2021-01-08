# Parte III: Demo 🛠️

### Antes de comenzar

Primeros pasos antes de comenzar la DEMO, a continuación realizaremos una serie de operaciones necesarias para llevar a cabo la posterior realización de consultas en nuestra base de datos, para ello deberemos realizar lo siguiente:

  - Lanzaremos ArangoDB mediante la consola
    ``` 
      /usr/local/sbin/arangod &
    ```
    
  - Ingresaremos a *localhost:8529* como **root** (sin contraseña)
    ``` 
      arangosh
    ```
    
  - Creación de base de datos **Airports**
    ``` 
      > db._createDatabase('Airports');
    ```
    
  - Creación de un nuevo usuario 
    ej. userArango password: mypwd
    ```batch
      > const users = require('@arangodb/users');
      > users.save('userArango', 'mypwd');
    ```
    
  - Concesión de permisos sobre este nuevo usuario
    ``` 
      users.grantDatabase('userArango', 'Airports', 'rw');
    ```
  - Exit de la base de datos _system
  - Exit como usuario **root**
    ``` 
      ctrl + C
    ```
  - Ingresamos a *localhost:8529* como **userArango** y seleccionamos la base de datos **Airports** para trabajar sobre ella
    ``` 
      arangosh --server.endpoint tcp://127.0.0.1:8529 --server.username userArango --server.database Airports
    ```

En segundo lugar realizaremos una serie de consultas para probar la potencia que puede llegar a alcanzar ArangoDB, asi como para conocer el tipo de consultas que podemos realizar con los datos seleccionados.

### Índice de consultas AQL
0. Operaciones **CRUD** en colecciones
1. Operación de **FILTRADO** en colecciones
2. Operación **MERGE** en colecciones
3. Aplicar **FUNCIONES** en las colecciones
4. Aplicar **OPERACIONES** en las colecciones
5. Creación de un índice tipo: **Geoespacial**
6. Aplicar **GRAFOS** en las colecciones
7. Comparación del **RENDIMIENTO** 

<br> 

# Consultas AQL
#### 0.- Operaciones CRUD en colecciones

  - Create
    ``` 
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
    ``` 
      FOR airport IN Airports
        RETURN airport
    ```

  - Update
    ```  
      UPDATE "KeflavikInternationalAirport" 
        WITH { elevation_ft: 182 
        } IN Airports
    ```
  
    ``` 
      RETURN DOCUMENT("Airports", "KeflavikInternationalAirport")
    ```

  - Delete
  
    ```  
      REMOVE "KeflavikInternationalAirport" 
        IN Airports
    ```
    También podemos llevar a cabo la eliminación de todos los documentos de una colección de la siguiente manera:
  
    ```  
      FOR airport IN Airports
         REMOVE airport IN Airports      
    ```

<br>

#### I.- Operación de FILTRADO en colecciones

Realizar una consulta en la cual se establece un filtro en el que podemos clasificar por el pais de situación del aeropuerto.

```  
  FOR airport IN Airports
      FILTER airport.iso_country == "ES"
      RETURN airport.name
 ```
Se puede filtrar por cualquier tipo de campo que pertenezca a la colección, en este caso se ha optado por filtrar según el nombre del un aeropuerto.

```  
  FOR airport IN Airports
      FILTER airport.name == "London Luton Airport"
      RETURN airport.iso_country
 ```
 
<br>

#### II.- Operación MERGE en colecciones
En este caso podemos optar por dos tipos de merge entre las colecciones, puede ser uno con ul filtro, en el cual añadimos el campo que más nos interese para obtener los resultados requerido, o por otra parte sin ningún tipo de filtro.

- Modificar un trait sin filtrado
  ``` 
    FOR c IN Travellers
        RETURN MERGE(c, { traits: DOCUMENT("Traits", c.traits)[*].es } )
  ```
  > Modificamos el valor de un atributo, de esta manera no es necesario modificar todos los documentos que contienen dicho atributo.
    ``` 
      UPDATE "Y" WITH {en: "Young Card" , es: "Carnet Joven" } IN Traits
    ```
  > Mostramos nuevamente los viajeros y sus atributos para observar el cambio.
    ``` 
      FOR c IN Travellers
        RETURN MERGE(c, { traits: DOCUMENT("Traits", c.traits)[*].es } )
    ```

- Mostrar un trait con filtrado
  ``` 
      FOR traveller IN Travellers
          FILTER traveller.age < 18
          LET traveller_full = MERGE (traveller, 
                  {
                  traits: DOCUMENT("Traits", traveller.traits)[*].es
                  }
              )
          RETURN {
              nombre: traveller_full.name,
              eded:traveller_full.age,
              caracteristicas:traveller_full.traits
          }
  ```

<br>

#### III.- Aplicar FUNCIONES en las colecciones
En este caso aplicamos dos funciones diferentes que nos aporta ArangoDB las cuales son: *Geo_Point* y *Distance*, estas resultan bastante útiles cuando se quiere
conocer situación geográfica de los aeropuertos.

``` 
    FOR traveller IN Travellers
        LIMIT 1
        FOR airport IN Airports
            SORT DISTANCE(traveller.latitude_deg, traveller.longitude_deg, airport.latitude_deg, airport.longitude_deg)
            LIMIT 3
            RETURN GEO_POINT(airport.longitude_deg, airport.latitude_deg)

```
<br>

#### IV.- Aplicar OPERACIONES en las colecciones
Podemos aplicar otro tipo de operaciones, como pueden ser *Limit* y *Sort* las cuales nos permiten realizar variaciones sobre el resultado de nuestra consulta, esto resulta útil a la hora de conocer aeropuertos más cercanos a una persona, donde podemos establecer un limite de visionado en la salida.

``` 
    FOR traveller IN Travellers
        LIMIT 1
        FOR airport IN Airports
            SORT DISTANCE(traveller.latitude_deg, traveller.longitude_deg, airport.latitude_deg, airport.longitude_deg)
            LIMIT 3
            RETURN {
                name:traveller.name,
                airport: airport.name,
                travellerLat:traveller.latitude_deg,
                travellerLon:traveller.longitude_deg,
                airportLat:airport.latitude_deg,
                airportLon:airport.longitude_deg
            }
```
Otra operación a tener en cuenta puede ser *Collect*, en este caso nos permite realizar la agrupación entre los distintos campos de nuestra colección mediante un campo. También nos permite realizar operaciones de agregación.

``` 
FOR airport IN Airports
  COLLECT country = airport.iso_country INTO groups = airport.name
  RETURN {
    "country":country,
    "airportsInCountry":groups
  }  
```

``` 
FOR airport IN Airports
  COLLECT country = airport.iso_country WITH COUNT INTO length
  SORT length DESC
  RETURN {
    "country":country,
    "airportsInCountry":length
  }  
```

<br>

#### V.- Creación de un índice tipo: Geoespacial

Para llevar a cabo operaciones de geolocalización, deberemos crear un índice de tipo Geo, para ello, habrá que realizar los siguientes pasos:
- Acceder al *tab* colecciones
- Acceder click a la colección de Airports
- Acceder en el *tab* de *Indexes*
- Hacer click en el botón con el símbolo de "+"
- Cambiar el tipo a *Geo Index*
- Escribir *coordinates* en el campo Fields
- Escribir el nombre que deseemos en el campo Nombre
- Hacer click en crear

<img src= "https://github.com/MiguelMesaGlez/arangoDB/blob/demo/ficherosAdicionales/imagenes/GeoJson.png" width = "600">

Ejemplo práctico del uso de un índice Geoespacial, con el cual buscamos conocer aquellos aeropuertos más cercanos a una persona estableciendo un rango en concreto, el cual puede ser modificado en función de las necesidades.

``` 
FOR traveller in Travellers 
    LET coordviajero = [traveller.coordinates[0], traveller.coordinates[1]]
        FOR airport IN Airports
            LET distance = DISTANCE(airport.coordinates[0], airport.coordinates[1], traveller.coordinates[0], traveller.coordinates[1])
            SORT traveller.name, distance
            FILTER distance < 200 * 1000

            RETURN {
            viajero: traveller.name,
            debe_ir_a: airport.name,
            latitude_airport: airport.coordinates[0],
            longitude_airport: airport.coordinates[1],
            latitude_viajero: traveller.coordinates[0],
            longitude_viajero: traveller.coordinates[1],
            distance: (distance/1000)
            }
```

<br>


#### VI.- Aplicar GRAFOS en las colecciones
ArangoDB presenta una gran utilidad a la hora de realizar grafos con nuestros datos, podemos establecer una serie de atributos que nos permiten devolver los vuelos salientes, de entrada o todos los que se realizan desde de un país. 

``` 
FOR airport IN Airports
    FILTER airport.iso_country == "ES"
        FOR v, e, p IN 1..1 OUTBOUND 
            airport Flights
            RETURN p
```

<br>

#### VII.- Comparación del RENDIMIENTO 
Mediante una misma consulta sobre una colección dada, se ha experimentado con la creación de diferentes índices, mediante su ejecución se ha llegado a la conclusión de que estos mejoran notablemente el tiempo de ejecución cuando se usan grandes cantidades de datos.

A modo de ejemplo, lo primero que haremos sera ejecutar la consulta y comprobar tanto el tiempo como el plan de ejecución de esta.
``` 
FOR flight IN Flights2
  FILTER flight.day == "15" AND flight.month == "1"
  RETURN flight
```

Después crearemos el primero de los indices que se creará sobre el campo mes. NOTA: los pasos que describiremos a continuación se deben realizar desde la interzar web de ArangoDB.

- Acceder al *tab* colecciones
- Acceder click a la colección de Flights2
- Acceder en el *tab* de *Indexes*
- Hacer click en el botón con el símbolo de "+"
- Cambiar el tipo a *Persistent Index*
- Escribir *month* en el campo Fields
- Escribir el nombre que deseemos en el campo Nombre 
- Hacer click en crear

Una vez creado el indice podemos volver a lanzar la consulta y comprobar cual ha sido la mejoría respecto a la ejecución anterior. Hecho esto podemos pasar a crear el segundo indice. Para ello, solo habrá que repetir los mismos pasas que en el anterior, cambiando la información introducida en el campo Fields por *day,month* y introduciendo un nombre distinto. Tras ejecutar la misma query podremos ver una mayor mejoría.

Finalmente, vamos a realizar una leve modificiación sobre la consulta y ver que ocurre.

``` 
FOR flight in Flights2
  FILTER TO_NUMBER(flight.day) > 15 AND flight.month == "1"
  RETURN flight
```

Observando el plan de ejecución, podemos ver como el indice que se utiliza es el creado sobre el campo mes, ya que este tipo de indices al ser no ordenados solo sirven para busquedas exactas y no para rangos. 
