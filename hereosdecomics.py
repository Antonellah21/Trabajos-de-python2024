# Definición de la lista de superhéroes (nombre, año, casa, biografía)
superheroes = [
    ["Linterna Verde", 1959, "DC", "Biografía de Linterna Verde..."],
    ["Wolverine", 1974, "Marvel", "Biografía de Wolverine..."],
    ["Dr. Strange", 1963, "Marvel", "Biografía de Dr. Strange..."],
    ["Iron Man", 1963, "Marvel", "Biografía de Iron Man con traje..."],
    ["Batman", 1939, "DC", "Biografía de Batman con armadura..."],
    ["Superman", 1938, "DC", "Biografía de Superman..."],
    ["Capitana Marvel", 1967, "Marvel", "Biografía de Capitana Marvel..."],
    ["Mujer Maravilla", 1941, "DC", "Biografía de Mujer Maravilla..."],
    ["Flash", 1940, "DC", "Biografía de Flash..."],
    ["Star-Lord", 1976, "Marvel", "Biografía de Star-Lord..."]
]


def eliminarLinternaVerde(superheroes):
    for heroe in superheroes:
        if heroe[0] == "Linterna Verde":
            superheroes.remove(heroe)


def obtenerAnioWolverine(superheroes):
    for heroe in superheroes:
        if heroe[0] == "Wolverine":
            return heroe[1]



def cambiarCasaDrStrange(superheroes):
    for heroe in superheroes:
        if heroe[0] == "Dr. Strange":
            heroe[2] = "Marvel"


def mostrarHeroesConTraje(superheroes):
    nombres = []
    for heroe in superheroes:
        if "traje" in heroe[3] or "armadura" in heroe[3]:
            nombres.append(heroe[0])
    return nombres


def mostrarHeroesAntesDe1963(superheroes):
    nombres_casas = []
    for heroe in superheroes:
        if heroe[1] < 1963:
            nombres_casas.append((heroe[0], heroe[2]))
    return nombres_casas


def mostrarCasaCapitanaMujer(superheroes):
    casas = {}
    for heroe in superheroes:
        if heroe[0] == "Capitana Marvel" or heroe[0] == "Mujer Maravilla":
            casas[heroe[0]] = heroe[2]
    return casas


def mostrarInfoFlashStarLord(superheroes):
    info = {}
    for heroe in superheroes:
        if heroe[0] == "Flash" or heroe[0] == "Star-Lord":
            info[heroe[0]] = {"Año": heroe[1],
                              "Casa": heroe[2], "Biografía": heroe[3]}
    return info


def listarHeroesPorLetra(superheroes, letras):
    nombres = []
    for heroe in superheroes:
        if heroe[0][0] in letras:
            nombres.append(heroe[0])
    return nombres


def contarSuperheroesPorCasa(superheroes):
    casas = {"Marvel": 0, "DC": 0}
    for heroe in superheroes:
        casas[heroe[2]] += 1
    return casas


eliminarLinternaVerde(superheroes)
anio_wolverine = obtenerAnioWolverine(superheroes)

cambiarCasaDrStrange(superheroes)

heroes_con_traje = mostrarHeroesConTraje(superheroes)

heroes_antes_de_1963 = mostrarHeroesAntesDe1963(superheroes)

casas_capitana_mujer = mostrarCasaCapitanaMujer(superheroes)

info_flash_starlord = mostrarInfoFlashStarLord(superheroes)

heroes_letras = listarHeroesPorLetra(superheroes, "BMS")

contar_casas = contarSuperheroesPorCasa(superheroes)

print("a. Lista de superhéroes después de eliminar a Linterna Verde:")
for heroe in superheroes:
    print(heroe)
print()
print("Año de aparición de Wolverine:", anio_wolverine)
print()

print("Lista de superhéroes después de cambiar la casa de Dr. Strange a Marvel:")
for heroe in superheroes:
    print(heroe)
print()
print("Superhéroes con 'traje' o 'armadura':", heroes_con_traje)

print("Superhéroes cuya fecha de aparición es anterior a 1963:")

for heroe in heroes_antes_de_1963:
    print(heroe[0], "(", heroe[1], ")")

print("Casa de Capitana Marvel y Mujer Maravilla:", casas_capitana_mujer)

print("Información de Flash y Star-Lord:")

for nombre, info in info_flash_starlord.items():
    print(nombre)
    print("Año:", info["Año"])
    print("Casa:", info["Casa"])


print(" Superhéroes que comienzan con B, M o S:", heroes_letras)

print("Número de superhéroes por casa de cómic:", contar_casas)
