import matplotlib.pyplot as plt
import requests
import json
import pandas
import jupyter

def actualizar_jsons_de_pokemones(api)->None:
    response = requests.get(api+'pokemon/?limit=100')
    if response.status_code == 200:
        with open(f'cache\\cache_pokemon.json', 'w') as f:
            json.dump(response.json(), f, indent=4)
    else:
        print(f'Error en actualizacion del json \'cache_pokemon.json\'\nEl status_code es: {response.status_code}\n')

    urls = list()
    with open('cache\\cache_pokemon.json', 'r') as f:
        for pokemon in json.loads(f.read())['results']:
            with open(f'cache\\{pokemon['name']}.json','w') as g:
                json.dump((requests.get(pokemon['url'])).json(),g,indent=4)

# Extrae todas las posibles variables de un endpoint
def extraer_names_de_endpoint_a_list(endpoint:str)->list:
    names = []
    with open(f'cache\\cache_{endpoint}.json', 'r') as f:
        contenido = f.read()
        dictionary = json.loads(contenido)
        for x in dictionary['results']:
            names.append(x['name'])
    return names

# Busca el API correspondiente al endpoint y name ingresado
# Ejemplo: endpoint=pokemon name='bulbasaur' retorna el contenido de 'https://pokeapi.co/api/v2/pokemon/1/'
def extraer_informacion_json_a_dict(json_name:str)->dict:
    with open(f'cache\\{json_name}.json', 'r') as f:
        dictionary = json.loads(f.read())
    return dictionary

# Del endpoint 'pokemon' obtiene los stats solamente ingresando el nombre del pokemon 
def extraer_stats_pokemon_a_dict(nombre:str)->dict:
    dictionary = dict()
    for stat in extraer_informacion_json_a_dict(nombre)['stats']:
        dictionary.update({stat['stat']['name']:stat['base_stat']})
    return dictionary
        
def crear_grafica_de_barras_de_atributo_pokemones(pokemones:list,atributo:str):
    stats = dict()
    
    # Update del diccionario 'stats'
    for pokemon in pokemones:
        stats.update({pokemon:extraer_stats_pokemon_a_dict(pokemon)[atributo]})
    
    # Configuracion pyplot
    x = [nombre for nombre, valor in stats.items()]
    y = [valor for nombre, valor in stats.items()]
    fig,ax = plt.subplots()
    p = ax.bar(x,y,width=1,color='blue',edgecolor='black',tick_label=[x.capitalize() for x in pokemones])
    ax.set_title(f'{atributo.capitalize()} de los Pokemones')
    ax.set_ylabel(f'{atributo.capitalize()}')
    ax.bar_label(p, label_type='center')
    fig.savefig(f'graficas\\Grafica de barras de {atributo} de pokemones.pdf')
    plt.show()

def crear_grafica_de_barras_de_alturas_pokemones(pokemones:list):
    stats = dict()
    
    # Update del diccionario 'stats'
    for pokemon in pokemones:
        stats.update({pokemon:extraer_informacion_json_a_dict(pokemon)['height']*10})
    
    # Configuracion pyplot
    x = [nombre for nombre, valor in stats.items()]
    y = [valor for nombre, valor in stats.items()]
    fig,ax = plt.subplots()
    p = ax.bar(x,y,width=1,color='green',edgecolor='black',tick_label=[x.capitalize() for x in pokemones],label='Cms')
    ax.set_title('Alturas de los Pokemones')
    ax.set_ylabel('Altura')
    ax.bar_label(p, label_type='center')
    fig.savefig('graficas\\Grafica de alturas de pokemones.pdf')
    ax.legend()
    plt.show()

def crear_grafica_de_barras_de_pesos_pokemones(pokemones:list):
    stats = dict()
    
    # Update del diccionario 'stats'
    for pokemon in pokemones:
        stats.update({pokemon:extraer_informacion_json_a_dict(pokemon)['weight']/10})
    
    # Configuracion pyplot
    x = [nombre for nombre, valor in stats.items()]
    y = [valor for nombre, valor in stats.items()]
    fig,ax = plt.subplots()
    p = ax.bar(x,y,width=1,color='yellow',edgecolor='black',tick_label=[x.capitalize() for x in pokemones], label='Kgs')
    ax.set_title('Peso de los Pokemones')
    ax.set_ylabel('Peso')
    ax.bar_label(p, label_type='center')
    fig.savefig('graficas\\Grafica de barras de pesos de pokemones.pdf')
    ax.legend()
    plt.show()

def exportar_excel_info_pokemones(pokemones:list):
    data = list() 
    columns = ['Name','height','weight','hp','attack','defense','special-attack','special-defense','speed']
    for pokemon in pokemones:
        temp = [pokemon, extraer_informacion_json_a_dict(pokemon)['height'],extraer_informacion_json_a_dict(pokemon)['weight']]
        for name,stat in extraer_stats_pokemon_a_dict(pokemon).items():
            temp.append(stat)
        data.append(temp)
    dataframe = pandas.DataFrame(data,columns=columns)
    dataframe.to_excel('excel\\info pokemones.xlsx')

def obtener_media(pokemones:list, stat:str)->float:
    lista = list()
    for pokemon in pokemones:
        lista.append(extraer_stats_pokemon_a_dict(pokemon)[f'{stat}'])
    media = sum(lista)/len(lista)
    print(f'Media de {stat} de pokemones ingresados: {media}')
    return media

def obtener_mediana(pokemones:list, stat:str)->float:
    lista = list()
    for pokemon in pokemones:
        lista.append(extraer_stats_pokemon_a_dict(pokemon)[f'{stat}'])

    lista = sorted(lista)
    mediana_exacta = False
    mediana = float()
    if len(lista)%2!=0:
        mediana_exacta = True
    if mediana_exacta == True:
        mediana = lista[(len(lista)//2)]
    elif mediana_exacta == False:
        mediana = ((lista[int((len(lista)/2)-1)])+(lista[int(len(lista)/2)]))/2
    print(f'Mediana de {stat} de pokemones ingresados: {mediana}')
    return mediana

def obtener_moda(pokemones:list, stat:str)->float:
    lista = list()
    for pokemon in pokemones:
        lista.append(extraer_stats_pokemon_a_dict(pokemon)[f'{stat}'])

    diccionario = dict()
    moda = -1
    repeticiones = -1
    for x in lista:
        if str(x) not in diccionario.keys():
            diccionario.update({str(x):1})
        else:
            diccionario[str(x)] = diccionario[str(x)]+1
    for key,value in diccionario.items():
        if value > repeticiones:
            repeticiones = value
            moda = float(key)
    print(f'Moda de {stat} de pokemones ingresados: {moda}')
    return moda