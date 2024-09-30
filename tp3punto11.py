from collections import deque

class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return f"{self.nombre} de {self.planeta}"

def agregar_personaje(cola, nombre, planeta):
    personaje = Personaje(nombre, planeta)
    cola.append(personaje)

def mostrar_personajes_por_planeta(cola, planetas_interes):
    print("Personajes de Alderaan, Endor y Tatooine:")
    for personaje in cola:
        if personaje.planeta in planetas_interes:
            print(personaje)

def mostrar_planeta_natal(cola, nombres_interes):
    for personaje in cola:
        if personaje.nombre in nombres_interes:
            print(f"El planeta natal de {personaje.nombre} es {personaje.planeta}")

def insertar_antes_de_personaje(cola, nombre_nuevo, planeta_nuevo, nombre_referencia):
    nuevo_personaje = Personaje(nombre_nuevo, planeta_nuevo)
    temp_cola = deque() 
    insertado = False

    while cola:
        personaje = cola.popleft()
        if personaje.nombre == nombre_referencia and not insertado:
            temp_cola.append(nuevo_personaje) 
            insertado = True
        temp_cola.append(personaje)

    return temp_cola

def eliminar_despues_de_personaje(cola, nombre_referencia):
    temp_cola = deque()  
    saltar_siguiente = False

    while cola:
        personaje = cola.popleft()
        if saltar_siguiente:
            saltar_siguiente = False  
            continue
        temp_cola.append(personaje)
        if personaje.nombre == nombre_referencia:
            saltar_siguiente = True 

    return temp_cola

cola_personajes = deque()

agregar_personaje(cola_personajes, "Luke Skywalker", "Tatooine")
agregar_personaje(cola_personajes, "Leia Organa", "Alderaan")
agregar_personaje(cola_personajes, "Han Solo", "Corellia")
agregar_personaje(cola_personajes, "Yoda", "Dagobah")
agregar_personaje(cola_personajes, "Jar Jar Binks", "Naboo")
agregar_personaje(cola_personajes, "C-3PO", "Tatooine")

planetas_interes = ["Alderaan", "Endor", "Tatooine"]
mostrar_personajes_por_planeta(cola_personajes, planetas_interes)
print()

nombres_interes = ["Luke Skywalker", "Han Solo"]
mostrar_planeta_natal(cola_personajes, nombres_interes)
print()

cola_personajes = insertar_antes_de_personaje(cola_personajes, "Obi-Wan Kenobi", "Stewjon", "Yoda")

cola_personajes = eliminar_despues_de_personaje(cola_personajes, "Jar Jar Binks")

print("\nPersonajes después de las operaciones:")
for personaje in cola_personajes:
    print(personaje)