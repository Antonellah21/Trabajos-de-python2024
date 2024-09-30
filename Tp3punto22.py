from collections import deque

cola_personajes = deque([
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"nombre": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
    {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
])

def buscar_personaje_por_superheroe(superheroe):
    for personaje in cola_personajes:
        if personaje["superheroe"] == superheroe:
            return personaje["nombre"]
    return None

nombre_personaje_capitana_marvel = buscar_personaje_por_superheroe("Capitana Marvel")
print(f"a. El nombre del personaje de Capitana Marvel es: {nombre_personaje_capitana_marvel}")

def superheroe_femeninos():
    return [personaje["superheroe"] for personaje in cola_personajes if personaje["genero"] == "F"]

superheroinas = superheroe_femeninos()
print(f"b. Los nombres de los superhéroes femeninos son: {superheroinas}")

def personajes_masculinos():
    return [personaje["nombre"] for personaje in cola_personajes if personaje["genero"] == "M"]

personajes_masc = personajes_masculinos()
print(f"c. Los nombres de los personajes masculinos son: {personajes_masc}")

def buscar_superheroe_por_personaje(nombre):
    for personaje in cola_personajes:
        if personaje["nombre"] == nombre:
            return personaje["superheroe"]
    return None

superheroe_scott_lang = buscar_superheroe_por_personaje("Scott Lang")
print(f"d. El nombre del superhéroe de Scott Lang es: {superheroe_scott_lang}")

def personajes_con_s():
    return [personaje for personaje in cola_personajes if personaje["nombre"].startswith("S")]

personajes_s = personajes_con_s()
print(f"e. Los personajes cuyos nombres comienzan con la letra 'S' son: {personajes_s}")

def buscar_superheroe_de_carol_danvers():
    for personaje in cola_personajes:
        if personaje["nombre"] == "Carol Danvers":
            return personaje["superheroe"]
    return None

superheroe_carol_danvers = buscar_superheroe_de_carol_danvers()
if superheroe_carol_danvers:
    print(f"f. Carol Danvers se encuentra en la cola, y su nombre de superhéroe es: {superheroe_carol_danvers}")
else:
    print("f. Carol Danvers no se encuentra en la cola.")