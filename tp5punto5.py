class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre        
        self.es_heroe = es_heroe    
        self.izquierdo = None       
        self.derecho = None         

class ArbolMCU:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, nombre, es_heroe):
        nuevo_nodo = Nodo(nombre, es_heroe)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)
    
    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.nombre < actual.nombre:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo_nodo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecho, nuevo_nodo)

    def listar_villanos_alfabeticamente(self):
        villanos = []
        
        def in_order(nodo):
            if nodo is not None:
                in_order(nodo.izquierdo)
                if not nodo.es_heroe:  
                    villanos.append(nodo.nombre)
                in_order(nodo.derecho)
        
        in_order(self.raiz)
        return villanos

    def listar_superheroes_con_c(self):
        superheroes_c = []
        
        def in_order(nodo):
            if nodo is not None:
                in_order(nodo.izquierdo)
                if nodo.es_heroe and nodo.nombre.startswith("C"):  
                    superheroes_c.append(nodo.nombre)
                in_order(nodo.derecho)
        
        in_order(self.raiz)
        return superheroes_c

    def contar_superheroes(self):
        contador = 0
        
        def in_order(nodo):
            nonlocal contador  
            if nodo is not None:
                in_order(nodo.izquierdo)
                if nodo.es_heroe:  
                    contador += 1
                in_order(nodo.derecho)
        
        in_order(self.raiz)
        return contador
    
    def listar_superheroes_descendente(self):
        superheroes_desc = []
        
        def in_order_inverso(nodo):
            if nodo is not None:
                in_order_inverso(nodo.derecho) 
                if nodo.es_heroe:  
                    superheroes_desc.append(nodo.nombre)
                in_order_inverso(nodo.izquierdo)
        
        in_order_inverso(self.raiz)
        return superheroes_desc

    def generar_bosque(self):
        arbol_superheroes = ArbolMCU()
        arbol_villanos = ArbolMCU()

        def in_order(nodo):
            if nodo is not None:
                in_order(nodo.izquierdo)
                if nodo.es_heroe:
                    arbol_superheroes.insertar(nodo.nombre, True)
                else:
                    arbol_villanos.insertar(nodo.nombre, False)
                in_order(nodo.derecho)

        in_order(self.raiz)
        return arbol_superheroes, arbol_villanos

    def contar_nodos(self):
        contador = 0
        
        def in_order(nodo):
            nonlocal contador
            if nodo is not None:
                contador += 1
                in_order(nodo.izquierdo)
                in_order(nodo.derecho)
        
        in_order(self.raiz)
        return contador

    def barrido_alfabetico(self):
        nombres = []
        
        def in_order(nodo):
            if nodo is not None:
                in_order(nodo.izquierdo)
                nombres.append(nodo.nombre)
                in_order(nodo.derecho)

        in_order(self.raiz)
        return nombres

    def buscar_y_modificar(self, nombre_original, nuevo_nombre):
        def buscar(nodo):
            if nodo is None:
                return False
            if nombre_original.lower() in nodo.nombre.lower():
                nodo.nombre = nuevo_nombre
                return True
            return buscar(nodo.izquierdo) or buscar(nodo.derecho)

        encontrado = buscar(self.raiz)
        return encontrado

arbol_mcu = ArbolMCU()

arbol_mcu.insertar("Iron Man", True)
arbol_mcu.insertar("Thanos", False)
arbol_mcu.insertar("Hulk", True)
arbol_mcu.insertar("Loki", False)
arbol_mcu.insertar("Captain America", True)
arbol_mcu.insertar("Ultron", False)
arbol_mcu.insertar("Captain Marvel", True)  
arbol_mcu.insertar("Doctor Strange", True)  

superheroes_con_c = arbol_mcu.listar_superheroes_con_c()
print("Superhéroes que empiezan con 'C':", superheroes_con_c)

total_superheroes = arbol_mcu.contar_superheroes()
print("Total de superhéroes en el árbol:", total_superheroes)

superheroes_descendentes = arbol_mcu.listar_superheroes_descendente()
print("Superhéroes ordenados de manera descendente:", superheroes_descendentes)

arbol_superheroes, arbol_villanos = arbol_mcu.generar_bosque()

nodos_superheroes = arbol_superheroes.contar_nodos()
print("Total de nodos en el árbol de superhéroes:", nodos_superheroes)

nodos_villanos = arbol_villanos.contar_nodos()
print("Total de nodos en el árbol de villanos:", nodos_villanos)

barrido_superheroes = arbol_superheroes.barrido_alfabetico()
barrido_villanos = arbol_villanos.barrido_alfabetico()

print("Barrido alfabético de superhéroes:", barrido_superheroes)
print("Barrido alfabético de villanos:", barrido_villanos)
    
barrido_superheroes_actualizado = arbol_superheroes.barrido_alfabetico()
print("Barrido alfabético de superhéroes después de la modificación:", barrido_superheroes_actualizado)
