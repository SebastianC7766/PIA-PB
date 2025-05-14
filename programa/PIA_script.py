import PIA_modulo

api = 'https://pokeapi.co/api/v2/'

# Actualizacion de API
PIA_modulo.actualizar_jsons_de_pokemones(api)

# Exportacion a excel
PIA_modulo.exportar_excel_info_pokemones(PIA_modulo.extraer_names_de_endpoint_a_list('pokemon'))

# Creacion de grafica de alturas (incluye exportacion pdf)
PIA_modulo.crear_grafica_de_barras_de_alturas_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'])

# Creacion de grafica de pesos (incluye exportacion pdf)
PIA_modulo.crear_grafica_de_barras_de_pesos_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'])

# Creacion de graficas individuales para cada atributo (Incluye exportacion pdf)
PIA_modulo.crear_grafica_de_barras_de_atributo_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'],'hp')
PIA_modulo.crear_grafica_de_barras_de_atributo_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'],'attack')
PIA_modulo.crear_grafica_de_barras_de_atributo_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'],'defense')
PIA_modulo.crear_grafica_de_barras_de_atributo_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'],'special-attack')
PIA_modulo.crear_grafica_de_barras_de_atributo_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'],'special-defense')
PIA_modulo.crear_grafica_de_barras_de_atributo_pokemones(['bulbasaur','farfetchd','charmander','charizard','metapod'],'speed')

# Obtencion de datos estadisticos
PIA_modulo.obtener_media(PIA_modulo.extraer_names_de_endpoint_a_list('pokemon'),'hp')
PIA_modulo.obtener_mediana(PIA_modulo.extraer_names_de_endpoint_a_list('pokemon'),'attack')
PIA_modulo.obtener_moda(PIA_modulo.extraer_names_de_endpoint_a_list('pokemon'),'defense')