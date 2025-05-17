
# PIA Programacion Basica

Proyecto basado en la creacion de un programa que utilice informacion de PokeAPI para realizar graficas, calculos y medidas estadisticas con la informacion que ofrece la API.


## Integrantes
 - Sebastian Calderon Carrillo **2087472**
 - Hector Alan Hernandez Gonzalez **2082913**
 - Leonardo Isaac Vela Cortes **2154477**
 - Diego Ernesto Camarillo Salazar **1996387**
 - Joel De Jesus Galvan Campos **2159634**

## FAQ

#### Que fenómeno o situación se desea analizar?

Se busca analizar las diferentes estadísticas de los pokémons base. Estadísticas como ataque, defensa, vida, velocidad, altura y peso.

#### Porque es relevante?

Existen personas que dedican mucho tiempo a competir en cosas relacionadas con Pokémon, por lo que les y nos es de ayuda para analizar cuáles serían nuestras mejores opciones para utilizar contra algún rival. 


## Funciones

#### actualizar_jsons_de_pokemones(api)
Actualiza todo el cache del cual posteriormente se obtendra informacion. No retorna nada.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api` | `string` | **Required**. Es el link principal de la API|

#### extraer_names_de_endpoint_a_list(endpoint)
Extrae todas las posibles variables de un endpoint como los nombres de pokemones, de items, de ubicaciones, etc. Retorna una lista.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `endpoint` | `string` | **Required**. Nombre del endpoint del cual se extareran los nombres (pokemon, item, locations, versions)|

#### extraer_informacion_json_a_dict(json_name)
Utiliza un json y lo convierte en diccionario de python. Retorna el diccionario
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `json_name` | `string` | **Required**. Nombre del archvio .json, sin incluir extension.|

#### extraer_stats_pokemon_a_dict(nombre)
Retorna un diccionario de todos los valores base que tiene un pokemon (hp, defense, height, weight, etc.)
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `nombre` | `string` | **Required**. Nombre del pokemon del cual se quiere obtener los stats|

#### crear_grafica_de_barras_de_atributo_pokemones(pokemones,atributo)
Crea una grafica de barras comparando el atributo escogido de todos los pokemones ingresados. De igual manera, exporta un pdf de la grafica creada.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pokemones` | `list` | **Required**. Lista de strings de cada uno de los nombres de los pokemones a evaluar|
| `atributo` | `string` | **Required**. Atributo a graficar (hp, defense, etc.)|

#### crear_grafica_de_barras_de_alturas_pokemones(pokemones)
Crea una grafica de barras comparando las alturas de todos los pokemones ingresados. De igual manera, exporta un pdf de la grafica creada.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pokemones` | `list` | **Required**. Lista de strings de cada uno de los nombres de los pokemones a evaluar|

#### crear_grafica_de_barras_de_pesos_pokemones(pokemones)
Crea una grafica de barras comparando los pesos de todos los pokemones ingresados. De igual manera, exporta un pdf de la grafica creada.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pokemones` | `list` | **Required**. Lista de strings de cada uno de los nombres de los pokemones a evaluar|

#### exportar_excel_info_pokemones(pokemones)
Crea un excel con toda la informacion de cada uno de los pokemones ingresados
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pokemones` | `list` | **Required**. Lista de strings de cada uno de los nombres de los pokemones a evaluar|

#### obtener_media(pokemones,stat)
Imprime y retorna la media aritmetica del stat ingresado de todos los pokemones ingresados.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pokemones` | `list` | **Required**. Lista de strings de cada uno de los nombres de los pokemones a evaluar|
| `stat` | `string` | **Required**. Atributo a evaluar (hp, defense, speed, etc.)|

#### obtener_mediana(pokemones,stat)
Imprime y retorna la mediana del stat ingresado de todos los pokemones ingresados.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pokemones` | `list` | **Required**. Lista de strings de cada uno de los nombres de los pokemones a evaluar|
| `stat` | `string` | **Required**. Atributo a evaluar (hp, defense, speed, etc.)|

#### obtener_moda(pokemones,stat)
Imprime y retorna la moda del stat ingresado de todos los pokemones ingresados.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `pokemones` | `list` | **Required**. Lista de strings de cada uno de los nombres de los pokemones a evaluar|
| `stat` | `string` | **Required**. Atributo a evaluar (hp, defense, speed, etc.)|