import heapq
from collections import defaultdict

class Maravilla:
    def __init__(self, nombre, paises, tipo):
        self.nombre = nombre
        self.paises = paises  
        self.tipo = tipo      

class GrafoMaravillas:
    def __init__(self):
        self.grafo = defaultdict(list) 
        self.maravillas = {}            

    def agregar_maravilla(self, nombre, paises, tipo):
        maravilla = Maravilla(nombre, paises, tipo)
        self.maravillas[nombre] = maravilla
        self.grafo[nombre] = []

    def agregar_arista(self, nombre1, nombre2, distancia):
        if nombre1 in self.grafo and nombre2 in self.grafo:
            self.grafo[nombre1].append((distancia, nombre2))
            self.grafo[nombre2].append((distancia, nombre1))

    def mostrar_grafo(self):
        for maravilla, conexiones in self.grafo.items():
            conexiones_str = ', '.join([f"{conectado} ({distancia} km)" for distancia, conectado in conexiones])
            print(f"{maravilla} -> {conexiones_str}")

    def prim_mst(self, tipo):
        inicio = next((nombre for nombre, maravilla in self.maravillas.items() if maravilla.tipo == tipo), None)
        if not inicio:
            return 0
        
        costo_total = 0
        visitados = set([inicio])
        aristas_min_heap = [(distancia, inicio, destino) for distancia, destino in self.grafo[inicio]]
        heapq.heapify(aristas_min_heap)

        while aristas_min_heap:
            distancia, origen, destino = heapq.heappop(aristas_min_heap)
            if destino not in visitados:
                visitados.add(destino)
                costo_total += distancia
                for siguiente_distancia, siguiente_destino in self.grafo[destino]:
                    if siguiente_destino not in visitados:
                        heapq.heappush(aristas_min_heap, (siguiente_distancia, destino, siguiente_destino))

        return costo_total

    def pais_con_dos_tipos(self):
        paises_tipos = defaultdict(set)
        for maravilla in self.maravillas.values():
            for pais in maravilla.paises:
                paises_tipos[pais].add(maravilla.tipo)
        
        paises_con_dos_tipos = [pais for pais, tipos in paises_tipos.items() if len(tipos) > 1]
        return paises_con_dos_tipos

    def pais_con_multiples_maravillas(self):
        pais_tipo_conteo = defaultdict(lambda: defaultdict(int))
        for maravilla in self.maravillas.values():
            for pais in maravilla.paises:
                pais_tipo_conteo[pais][maravilla.tipo] += 1

        paises_varias_maravillas = {pais: tipo for pais, tipos in pais_tipo_conteo.items() for tipo, count in tipos.items() if count > 1}
        return paises_varias_maravillas

grafo_maravillas = GrafoMaravillas()

grafo_maravillas.agregar_maravilla("Taj Mahal", ["India"], "arquitectónica")
grafo_maravillas.agregar_maravilla("Machu Picchu", ["Perú"], "arquitectónica")
grafo_maravillas.agregar_maravilla("Cristo Redentor", ["Brasil"], "arquitectónica")
grafo_maravillas.agregar_maravilla("Gran Muralla China", ["China"], "arquitectónica")
grafo_maravillas.agregar_maravilla("Coliseo", ["Italia"], "arquitectónica")
grafo_maravillas.agregar_maravilla("Chichen Itza", ["México"], "arquitectónica")
grafo_maravillas.agregar_maravilla("Petra", ["Jordania"], "arquitectónica")

grafo_maravillas.agregar_maravilla("Amazonas", ["Brasil", "Colombia", "Perú"], "natural")
grafo_maravillas.agregar_maravilla("Bahía de Ha-Long", ["Vietnam"], "natural")
grafo_maravillas.agregar_maravilla("Cataratas del Iguazú", ["Argentina", "Brasil"], "natural")
grafo_maravillas.agregar_maravilla("Isla Jeju", ["Corea del Sur"], "natural")
grafo_maravillas.agregar_maravilla("Parque Nacional de Komodo", ["Indonesia"], "natural")
grafo_maravillas.agregar_maravilla("Río Subterráneo de Puerto Princesa", ["Filipinas"], "natural")
grafo_maravillas.agregar_maravilla("Montaña de la Mesa", ["Sudáfrica"], "natural")

grafo_maravillas.agregar_arista("Taj Mahal", "Machu Picchu", 14000)
grafo_maravillas.agregar_arista("Taj Mahal", "Cristo Redentor", 15000)
grafo_maravillas.agregar_arista("Cristo Redentor", "Gran Muralla China", 19000)
grafo_maravillas.agregar_arista("Gran Muralla China", "Coliseo", 8000)
grafo_maravillas.agregar_arista("Coliseo", "Chichen Itza", 9000)
grafo_maravillas.agregar_arista("Chichen Itza", "Petra", 12000)

grafo_maravillas.agregar_arista("Amazonas", "Bahía de Ha-Long", 17000)
grafo_maravillas.agregar_arista("Amazonas", "Cataratas del Iguazú", 1800)
grafo_maravillas.agregar_arista("Cataratas del Iguazú", "Isla Jeju", 20000)
grafo_maravillas.agregar_arista("Isla Jeju", "Parque Nacional de Komodo", 4800)
grafo_maravillas.agregar_arista("Parque Nacional de Komodo", "Río Subterráneo de Puerto Princesa", 2200)
grafo_maravillas.agregar_arista("Río Subterráneo de Puerto Princesa", "Montaña de la Mesa", 13000)

print("Grafo de Maravillas:")
grafo_maravillas.mostrar_grafo()

print("\nÁrbol de expansión mínima para maravillas arquitectónicas:")
costo_mst_arq = grafo_maravillas.prim_mst("arquitectónica")
print(f"Costo total de conexión: {costo_mst_arq} km")

print("\nÁrbol de expansión mínima para maravillas naturales:")
costo_mst_nat = grafo_maravillas.prim_mst("natural")
print(f"Costo total de conexión: {costo_mst_nat} km")

paises_ambos_tipos = grafo_maravillas.pais_con_dos_tipos()
print("\nPaíses con maravillas arquitectónicas y naturales:", paises_ambos_tipos)

paises_multiples_maravillas = grafo_maravillas.pais_con_multiples_maravillas()
print("\nPaíses con más de una maravilla del mismo tipo:", paises_multiples_maravillas)