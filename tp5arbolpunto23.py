class Nodo:
    def __init__(self, criatura, derrotado_por=None, descripcion=None, capturada=None):
        self.criatura = criatura
        self.derrotado_por = derrotado_por
        self.descripcion = descripcion
        self.hijos = []
        self.capturada = capturada  

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, criatura, derrotado_por=None, descripcion=None, capturada=None):
        nuevo_nodo = Nodo(criatura, derrotado_por, descripcion, capturada)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._agregar_recursivo(self.raiz, nuevo_nodo)

    def _agregar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.criatura < nodo_actual.criatura:
            if nodo_actual.hijos:
                self._agregar_recursivo(nodo_actual.hijos[0], nuevo_nodo)
            else:
                nodo_actual.hijos.append(nuevo_nodo)
        else:
            if len(nodo_actual.hijos) < 2:
                nodo_actual.hijos.append(nuevo_nodo)
            else:
                self._agregar_recursivo(nodo_actual.hijos[1], nuevo_nodo)

    def listado_inorden(self, nodo):
        if nodo:
            if nodo.hijos:
                self.listado_inorden(nodo.hijos[0])
            print(f"{nodo.criatura} - Derrotado por: {nodo.derrotado_por}, Descripción: {nodo.descripcion}, Capturada: {nodo.capturada}")
            if len(nodo.hijos) > 1:
                self.listado_inorden(nodo.hijos[1])

    def mostrar_informacion(self, criatura):
        nodo = self.buscar_criatura(self.raiz, criatura)
        if nodo:
            print(f"Nombre: {nodo.criatura}, Derrotado por: {nodo.derrotado_por}, Descripción: {nodo.descripcion}, Capturada: {nodo.capturada}")
        else:
            print("Criatura no encontrada.")

    def buscar_criatura(self, nodo, criatura):
        if nodo is None:
            return None
        if nodo.criatura == criatura:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self.buscar_criatura(hijo, criatura)
            if encontrado:
                return encontrado
        return None

    def heroes_mas_capturas(self):
        conteo = {}
        self._contar_capturas(self.raiz, conteo)
        return sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

    def _contar_capturas(self, nodo, conteo):
        if nodo:
            if nodo.derrotado_por:
                conteo[nodo.derrotado_por] = conteo.get(nodo.derrotado_por, 0) + 1
            for hijo in nodo.hijos:
                self._contar_capturas(hijo, conteo)

    def buscar_por_coincidencia(self, termino):
        coincidencias = []
        self._buscar_coincidencia(self.raiz, termino, coincidencias)
        return coincidencias

    def _buscar_coincidencia(self, nodo, termino, coincidencias):
        if nodo:
            if termino.lower() in nodo.criatura.lower():
                coincidencias.append(nodo.criatura)
            for hijo in nodo.hijos:
                self._buscar_coincidencia(hijo, termino, coincidencias)

    def eliminar_criatura(self, criatura):
        self.raiz = self._eliminar(self.raiz, criatura)

    def _eliminar(self, nodo, criatura):
        if nodo is None:
            return None
        if nodo.criatura == criatura:
            return None  

        nodo.hijos = [self._eliminar(hijo, criatura) for hijo in nodo.hijos]
        return nodo

    def listar_criaturas_derrotadas_por_heracles(self):
        criaturas = []
        self._listar_criaturas_por_heracles(self.raiz, criaturas)
        return criaturas

    def _listar_criaturas_por_heracles(self, nodo, criaturas):
        if nodo:
            if nodo.derrotado_por == "Heracles":
                criaturas.append(nodo.criatura)
            for hijo in nodo.hijos:
                self._listar_criaturas_por_heracles(hijo, criaturas)

    def listar_criaturas_no_derrotadas(self):
        criaturas = []
        self._listar_no_derrotadas(self.raiz, criaturas)
        return criaturas

    def _listar_no_derrotadas(self, nodo, criaturas):
        if nodo:
            if nodo.derrotado_por is None:
                criaturas.append(nodo.criatura)
            for hijo in nodo.hijos:
                self._listar_no_derrotadas(hijo, criaturas)

    def modificar_capturas_heracles(self):
        criaturas_a_modificar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
        for criatura in criaturas_a_modificar:
            nodo = self.buscar_criatura(self.raiz, criatura)
            if nodo:
                nodo.capturada = "Heracles"

    def modificar_aves_estinfalo(self):
        nodo = self.buscar_criatura(self.raiz, "Aves del Estínfalo")
        if nodo:
            nodo.derrotado_por = "Heracles"

    def renombrar_ladon(self):
        nodo = self.buscar_criatura(self.raiz, "Ladón")
        if nodo:
            nodo.criatura = "Dragón Ladón"

    def listado_por_nivel(self):
        niveles = {}
        self._listar_por_nivel(self.raiz, 0, niveles)
        for nivel, criaturas in niveles.items():
            print(f"Nivel {nivel}: {', '.join(criaturas)}")

    def _listar_por_nivel(self, nodo, nivel, niveles):
        if nodo:
            if nivel not in niveles:
                niveles[nivel] = []
            niveles[nivel].append(nodo.criatura)
            for hijo in nodo.hijos:
                self._listar_por_nivel(hijo, nivel + 1, niveles)

arbol = Arbol()
arbol.agregar("Ceto", descripcion="Diosa primordial del mar y madre de monstruos marinos.")
arbol.agregar("Tifón", "Zeus", "Monstruo gigante, considerado el más poderoso.")
arbol.agregar("Equidna", "Argos Panoptes", "Madre de todos los monstruos.")
arbol.agregar("Dino", descripcion="Monstruo marino que se considera parte de las leyendas de Ceto.")
arbol.agregar("Pefredo", descripcion="Criatura marina, madre de monstruos.")
arbol.agregar("Enio", descripcion="Diosa de la guerra y la destrucción, asociada con el caos.")
arbol.agregar("Escila", descripcion="Monstruo marino con múltiples cabezas, habitante de las rocas.")
arbol.agregar("Caribdis", descripcion="Monstruo marino que devora el mar y lo escupe de nuevo.")
arbol.agregar("Euríale", descripcion="Una de las Gorgonas, hermana de Medusa, conocida por su cabello de serpientes.")
arbol.agregar("Esteno", descripcion="Otra de las Gorgonas, también hermana de Medusa.")
arbol.agregar("Medusa", "Perseo", "Gorgona cuya mirada convierte a los hombres en piedra.")
arbol.agregar("Ladón", "Heracles", "Dragón que custodiaba las manzanas doradas en el Jardín de las Hespérides.")
arbol.agregar("Águila del Cáucaso", descripcion="Gigante que devoraba el hígado de Prometeo.")
arbol.agregar("Aves del Estínfalo", descripcion="Aves con plumaje metálico que atacaban a los humanos.")
arbol.agregar("Quimera", "Belerofonte", "Criatura con partes de león, cabra y serpiente.")
arbol.agregar("Hidra de Lerna", "Heracles", "Serpiente de múltiples cabezas, regeneraba sus cabezas cuando eran cortadas.")
arbol.agregar("León de Nemea", "Heracles", "León invulnerable que aterrorizaba la región de Nemea.")
arbol.agregar("Cerbero", descripcion="Perro de tres cabezas que guardaba la entrada al inframundo.")
arbol.agregar("Toro de Creta", "Teseo", "Toro sagrado que devastaba Creta.")
arbol.agregar("Jabalí de Calidón", "Atalanta", "Jabalí gigante que fue cazado por un grupo de héroes.")
arbol.agregar("Cerda de Cromión", "Teseo", "Monstruo que aterrorizaba a los viajeros.")
arbol.agregar("Ortro", "Heracles", "Perro de dos cabezas que guardaba el ganado de Gerión.")
arbol.agregar("Jabalí de Erimanto", descripcion="Jabalí gigantesco que fue capturado por Heracles.")
arbol.agregar("Cierva de Cerinea", descripcion="Cierva dorada que era muy veloz.")
arbol.agregar("Harpías", descripcion="Criaturas aladas que robaban y atormentaban a los humanos.")
arbol.agregar("Talos", "Medea", "Autómata de bronce que protegía a Creta.")
arbol.agregar("Pitón", "Apolo", "Serpiente que guardaba el oráculo de Delfos.")
arbol.agregar("Esfinge", "Edipo", "Criatura con cuerpo de león y cabeza de mujer, famosa por su acertijo.")
arbol.agregar("Basilisco", descripcion="Criatura legendaria que mata con la mirada.")
arbol.agregar("Sirenas", descripcion="Criaturas marinas que atraían a los marineros con su canto.")

arbol.modificar_capturas_heracles()

arbol.modificar_aves_estinfalo()

arbol.renombrar_ladon()

print("Listado inorden de criaturas y quienes las derrotaron:")
arbol.listado_inorden(arbol.raiz)

print("\nInformación de la criatura Talos:")
arbol.mostrar_informacion("Talos")

print("\nLos 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
heroes_mas_capturas = arbol.heroes_mas_capturas()
for heroe, cantidad in heroes_mas_capturas:
    print(f"{heroe}: {cantidad} criaturas derrotadas")

termino = "Cer"
print(f"\nBúsqueda por coincidencia para '{termino}':")
coincidencias = arbol.buscar_por_coincidencia(termino)
for criatura in coincidencias:
    print(criatura)

print("\nCriaturas derrotadas por Heracles:")
criaturas_derrotadas_por_heracles = arbol.listar_criaturas_derrotadas_por_heracles()
for criatura in criaturas_derrotadas_por_heracles:
    print(criatura)
    
print("\nCriaturas no derrotadas:")
criaturas_no_derrotadas = arbol.listar_criaturas_no_derrotadas()
for criatura in criaturas_no_derrotadas:
    print(criatura)

arbol.eliminar_criatura("Basilisco")
arbol.eliminar_criatura("Sirenas")

print("\nEstado del árbol después de las eliminaciones:")
arbol.listado_inorden(arbol.raiz)

print("\nListado por nivel del árbol:")
arbol.listado_por_nivel()
