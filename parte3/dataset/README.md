# Dataset Aeropuertos

En este apartado se encuentran los distintos scripts que hemos utilizado para generar y formatear los datos, además de los archivos .json resultantes y que han sido importados posteriormente a las coleccioens de ArangoDB.  

### Scripts 

| Nombre del archivo | Descripción |
| --- | --- |
| Limpieza_datos_ArangoDB.ipynb  | Jupyter notebook donde se obtienen los datos de los aeropuertos, se limpian y se seleccionan los atributos deseados |
| generateFlights.py | Script de Python en el que se generan combinaciones de los aeropuertos generando datos de vuelos |


### Archivos

| Nombre del archivo | Descripción |
| --- | --- |
| Airports.json | Contiene información en formato JSON de los 150 aeropuertos más grandes de Europa. Esta formateado para ser importado como colección de documentos |
| Flights.json | Contiene información en formato JSON de 186 vuelos entre los aeropuertos de Europa incluidos en *Airports.json*. Esta formateado para ser importado como colección de aristas (edge) |
| Travellers.json | Contiene información en formato JSON de 10 viajeros. Esta formateado para ser importado como colección de documentos |
| Traits.json | Contiene información sobre las características de los viajeros. Esta formateado para ser importado como colección de documentos. La colección generada servirá como decodificadora |
| flights_X.json | Contiene información en formato JSON de X vuelos entre los aeropuertos de Europa incluidos en *Airports.json*. Esta formateado para ser importado como colección de aristas (edge) |
| airports.csv | Archivo .csv que contine los datos iniciales con toda la información inicial sobre los aeropuertos y sobre el que se ha aplicado el script *Limpieza_datos_ArangoDB.ipynb*. |

