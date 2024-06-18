# Lista de entrenadores y sus Pokémons
entrenadores = [
    ["Ash Ketchum", 7, 50, 120, [
        ["Pikachu", 35, "Eléctrico", None],
        ["Charizard", 40, "Fuego", "Volador"],
        ["Bulbasaur", 30, "Planta", "Veneno"]
    ]],
    ["Goh", 2, 10, 40, [
        ["Starmie", 30, "Agua", "Psíquico"],
        ["Psyduck", 25, "Agua", None]
    ]],
    ["Leon", 10, 5, 100, [
        ["Gyarados", 35, "Agua", "Volador"],
        ["Onix", 38, "Roca", "Tierra"],
        ["Geodude", 28, "Roca", "Tierra"]
    ]],
    ["Chloe", 1, 8, 30, [
        ["Vulpix", 20, "Fuego", None],
        ["Blastoise", 50, "Agua", None]
    ]],
    ["Raihan", 4, 15, 60, [
        ["Umbreon", 45, "Siniestro", None],
        ["Nidoking", 40, "Veneno", "Tierra"]
    ]]
]

# a. Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            return len(entrenador[4])
    return 0

# b. Listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_tres_torneos(entrenadores):
    return [entrenador[0] for entrenador in entrenadores if entrenador[1] > 3]

# c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel(entrenadores):
    mayor_torneos_ganados = max(entrenadores, key=lambda entrenador: entrenador[1])
    pokemon_mayor_nivel = max(mayor_torneos_ganados[4], key=lambda pokemon: pokemon[1])
    return pokemon_mayor_nivel

# d. Mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            return entrenador
    return None

# e. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %
def entrenadores_con_porcentaje_batallas(entrenadores):
    return [
        entrenador[0]
        for entrenador in entrenadores
        if (entrenador[3] / (entrenador[2] + entrenador[3])) * 100 > 79
    ]

# f. Entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
def entrenadores_con_pokemons_tipo(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        tiene_fuego_planta = any(pokemon[2] == "Fuego" for pokemon in entrenador[4]) and any(pokemon[2] == "Planta" for pokemon in entrenador[4])
        tiene_agua_volador = any(pokemon[2] == "Agua" and pokemon[3] == "Volador" for pokemon in entrenador[4])
        if tiene_fuego_planta or tiene_agua_volador:
            resultado.append(entrenador[0])
    return resultado

# g. El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            return sum(pokemon[1] for pokemon in entrenador[4]) / len(entrenador[4])
    return 0

# h. Determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return sum(1 for entrenador in entrenadores if any(pokemon[0] == nombre_pokemon for pokemon in entrenador[4]))

# i. Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon[0] for pokemon in entrenador[4]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            resultado.append(entrenador[0])
    return resultado

# j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especificos(entrenadores):
    pokemons_especificos = {"Tyrantrum", "Terrakion", "Wingull"}
    return [
        entrenador[0]
        for entrenador in entrenadores
        if any(pokemon[0] in pokemons_especificos for pokemon in entrenador[4])
    ]

# Ejemplos de uso
print(f"a. Cantidad de Pokémons de Ash Ketchum: {cantidad_pokemons(entrenadores, 'Ash Ketchum')}")
print(f"b. Entrenadores con más de tres torneos ganados: {entrenadores_mas_de_tres_torneos(entrenadores)}")
print(f"c. Pokémon de mayor nivel del entrenador con más torneos ganados: {pokemon_mayor_nivel(entrenadores)}")
print(f"d. Datos de Ash Ketchum: {mostrar_datos_entrenador(entrenadores, 'Ash Ketchum')}")
print(f"e. Entrenadores con porcentaje de batallas ganadas mayor al 79 %: {entrenadores_con_porcentaje_batallas(entrenadores)}")
print(f"f. Entrenadores con Pokémons de tipo fuego y planta o agua/volador: {entrenadores_con_pokemons_tipo(entrenadores)}")
print(f"g. Promedio de nivel de los Pokémons de Ash Ketchum: {promedio_nivel_pokemons(entrenadores, 'Ash Ketchum')}")
print(f"h. Cantidad de entrenadores con Pikachu: {cantidad_entrenadores_con_pokemon(entrenadores, 'Pikachu')}")
print(f"i. Entrenadores con Pokémons repetidos: {entrenadores_con_pokemons_repetidos(entrenadores)}")
print(f"j. Entrenadores con Tyrantrum, Terrakion o Wingull: {entrenadores_con_pokemons_especificos(entrenadores)}")