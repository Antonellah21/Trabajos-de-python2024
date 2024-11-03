import heapq
import random

class GrafoCasa:
    def __init__(self):
        self.grafo = {} 

    def agregar_ambiente(self, ambiente):
        if ambiente not in self.grafo:
            self.grafo[ambiente] = []

    def agregar_conexion(self, ambiente1, ambiente2, peso):
        if ambiente1 in self.grafo and ambiente2 in self.grafo:
            self.grafo[ambiente1].append((peso, ambiente2))
            self.grafo[ambiente2].append((peso, ambiente1))

    def mostrar_grafo(self):
        for ambiente in self.grafo:
            conexiones = ', '.join([f"{destino} ({peso}m)" for peso, destino in self.grafo[ambiente]])
            print(f"{ambiente}: {conexiones}")

    def prim_mst(self):
        total_coste = 0
        ambiente_inicial = list(self.grafo.keys())[0]  
        visitados = set([ambiente_inicial])
        conexiones_min_heap = [(peso, ambiente_inicial, destino) for peso, destino in self.grafo[ambiente_inicial]]
        heapq.heapify(conexiones_min_heap)

        while conexiones_min_heap:
            peso, origen, destino = heapq.heappop(conexiones_min_heap)
            if destino not in visitados:
                visitados.add(destino)
                total_coste += peso
                for peso_siguiente, siguiente in self.grafo[destino]:
                    if siguiente not in visitados:
                        heapq.heappush(conexiones_min_heap, (peso_siguiente, destino, siguiente))

        return total_coste

    def dijkstra(self, inicio, destino):
        distancias = {ambiente: float('inf') for ambiente in self.grafo}
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            distancia_actual, ambiente_actual = heapq.heappop(cola_prioridad)

            if ambiente_actual == destino:
                return distancia_actual  

            for peso, vecino in self.grafo[ambiente_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return distancias[destino]

casa = GrafoCasa()
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

for ambiente in ambientes:
    casa.agregar_ambiente(ambiente)

conexiones = [
    ("cocina", "comedor"), ("cocina", "quincho"), ("cocina", "terraza"),
    ("comedor", "sala de estar"), ("comedor", "baño 1"), ("comedor", "terraza"),
    ("cochera", "quincho"), ("cochera", "patio"), ("cochera", "habitación 1"),
    ("quincho", "patio"), ("quincho", "sala de estar"), ("quincho", "cocina"),
    ("baño 1", "habitación 1"), ("baño 1", "sala de estar"), ("baño 1", "comedor"),
    ("baño 2", "habitación 2"), ("baño 2", "terraza"), ("baño 2", "sala de estar"),
    ("habitación 1", "habitación 2"), ("habitación 1", "patio"), ("habitación 1", "baño 1"),
    ("habitación 2", "terraza"), ("habitación 2", "baño 2"), ("habitación 2", "patio"),
    ("sala de estar", "terraza"), ("sala de estar", "cocina"), ("sala de estar", "patio"),
    ("terraza", "patio")
]

for ambiente1, ambiente2 in conexiones:
    peso = random.choice([5, random.randint(1, 10)])
    casa.agregar_conexion(ambiente1, ambiente2, peso)

print("Grafo de la casa:")
casa.mostrar_grafo()

total_metros_mst = casa.prim_mst()
print(f"\nTotal de metros de cables necesarios para conectar todos los ambientes (Árbol de Expansión Mínima): {total_metros_mst} metros")

distancia_corta = casa.dijkstra("habitación 1", "sala de estar")
print(f"\nDistancia más corta desde 'habitación 1' hasta 'sala de estar': {distancia_corta} metros")