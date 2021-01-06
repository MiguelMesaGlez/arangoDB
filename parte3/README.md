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
  - Ingresamos a *localhost:8529* como **userArango**
  - Seleccionamos la base de datos **Airports** para trabajar sobre ella

En segundo lugar realizaremos una serie de consultas para probar la potencia que puede llegar a alcanzar ArangoDB, asi como para conocer el tipo de consultas que podemos realizar con los datos seleccionados.

### Índice de consultas AQL

0. Operaciones CRUD básicas
1. Búsqueda de los aeropuertos de un país
2. Búsqueda del país de un aeropuerto
3. Modificación de los traits con y sin filtrado
4. Conocer situación geográfica de los aeropuertos
5. Conocer aeropuertos más cercanos a una persona
6. Creación índice Geoespacial
7. Conocer aeropuertos más cercanos a una persona por rango
8. Vuelos salientes de un país en concreto


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
  FOR airport IN Airports
      FILTER airport.iso_country == "ES"
      RETURN airport.name
 ```

#### II.- Búsqueda del país de un aeropuerto

```batch 
  FOR airport IN Airports
      FILTER airport.name == "London Luton Airport"
      RETURN airport.iso_country
 ```

#### III.- Modificación de los traits con y sin filtrado
- Modificar un trait sin filtrado
```batch
FOR c IN Travellers
    RETURN MERGE(c, { traits: DOCUMENT("Traits", c.traits)[*].es } )
```
> Modificamos el valor de un atributo, de esta manera no es necesario modificar todos los documentos que contienen dicho atributo.
```batch
UPDATE "Y" WITH { en: "efficient" } IN Traits
```
> Mostramos nuevamente los viajeros y sus atributos para observar el cambio.
```batch
FOR c IN Travellers
  RETURN MERGE(c, { traits: DOCUMENT("Traits", c.traits)[*].es } )
```

- Modificar un trait con filtrado
```batch
    FOR traveller IN travellers
        FILTER traveller.age < 18
        LET traveller_full = MERGE (traveller, 
                {
                traits: DOCUMENT("traits", traveller.traits)[*].en
                }
            )
        RETURN {
            nombre: traveller_full.name,
            eded:traveller_full.age,
            caracteristicas:traveller_full.traits
        }
```


#### IV.- Conocer situación geográfica de los aeropuertos

```batch
    FOR t IN travellers
        LIMIT 1
        FOR airport IN Airports
            SORT DISTANCE(t.latitude_deg, t.longitude_deg, airport.latitude_deg, airport.longitude_deg)
            LIMIT 3
            RETURN GEO_POINT(airport.longitude_deg, airport.latitude_deg)

```


#### V.- Conocer aeropuertos más cercanos a una persona

```batch
    FOR t IN travellers
        LIMIT 1
        FOR a IN airports
            SORT DISTANCE(t.latitude_deg, t.longitude_deg, a.latitude_deg, a.longitude_deg)
            LIMIT 3
            RETURN {
                name:t.name,
                travellerLat:t.latitude_deg,
                travellerLon:t.longitude_deg,
                airportLat:a.latitude_deg,
                airportLon:a.longitude_deg
            }


```


#### VI.- Creación de un índice tipo: Geoespacial

Para llevar a cabo operaciones de geolocalización, deberemos crear un índice de tipo Geo, para ello, habrá que realizar los siguientes pasos:
- Acceder al *tab* colecciones
- Acceder click a la colección de Airports
- Acceder en el *tap* de *Indexes*
- Hacer click en el botón con el símbolo de "+"
- Cambiar el tipo a *Geo Index*
- Escribir *coordinates* en el campo Fields
- Escribir el nombre que deseemos en el campo Nombre
- Hacer click en crear

En caso de necesitar más información, les recomendamos visitar la siguiente url: 

<img src= "https://github.com/MiguelMesaGlez/arangoDB/blob/demo/ficherosAdicionales/imagenes/GeoJson.png" width = "750">

#### VII.- Conocer aeropuertos más cercanos  a una persona por rango

```batch
FOR a in Viajeros 
    LET coordviajero = [a.coordinates[0], a.coordinates[1]]
        FOR loc IN Airports
            LET distance = DISTANCE(loc.coordinates[0], loc.coordinates[1], a.coordinates[0], a.coordinates[1])
            SORT distance
            FILTER distance < 2000 * 1000

            RETURN {
            viajero: a.name,
            debe_ir_a: loc.name,
            latitude: loc.coordinates[0],
            longitude: loc.coordinates[1],
            latitude_viajero: a.coordinates[0],
            longitude_viajero: a.coordinates[1],
            distance: (distance/1000)
            }


```


#### VII.- Vuelos salientes en modo de grafo de un país

```batch
FOR airport IN airports
    FILTER airport.iso_country == "ES"
        FOR v, e, p IN 1..1 OUTBOUND 
            airport flights
            RETURN p
```

