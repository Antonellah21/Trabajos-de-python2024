from collections import deque

cola_prioridad_alta = deque()
cola_prioridad_media = deque()
cola_prioridad_baja = deque()
bitacora = []

def agregar_pedido(nombre_general, planeta, descripcion):
    pedido = {
        "nombre_general": nombre_general,
        "planeta": planeta,
        "descripcion": descripcion
    }

    if nombre_general == "Gran Inquisidor" or planeta == "Lothal" or "Hera Syndulla" in descripcion:
        cola_prioridad_alta.append(pedido)
    elif nombre_general == "Agente Kallus" or "Destructor Estelar" in descripcion or "AT-AT" in descripcion:
        cola_prioridad_media.append(pedido)
    else:
        cola_prioridad_baja.append(pedido)

def atender_pedido():
    if cola_prioridad_alta:
        pedido_atendido = cola_prioridad_alta.popleft()
    elif cola_prioridad_media:
        pedido_atendido = cola_prioridad_media.popleft()
    elif cola_prioridad_baja:
        pedido_atendido = cola_prioridad_baja.popleft()
    else:
        print("No hay más pedidos para atender.")
        return

    bitacora.append(pedido_atendido)
    print(f"Pedido atendido: {pedido_atendido}")

def mostrar_estado():
    print("\n--- Estado de las colas ---")
    print(f"Cola de prioridad alta: {list(cola_prioridad_alta)}")
    print(f"Cola de prioridad media: {list(cola_prioridad_media)}")
    print(f"Cola de prioridad baja: {list(cola_prioridad_baja)}")
    print(f"Bitácora: {bitacora}\n")

agregar_pedido("Gran Inquisidor", "Coruscant", "Ataque de flota rebelde")
agregar_pedido("Agente Kallus", "Mustafar", "Movimientos de un Destructor Estelar")
agregar_pedido("General Veers", "Endor", "Necesidad de más AT-ATs")
agregar_pedido("General Hux", "Lothal", "Reportes de actividad de Hera Syndulla")
agregar_pedido("Capitán Phasma", "Jakku", "Reforzamiento de tropas")

mostrar_estado()
atender_pedido()  
atender_pedido()  
atender_pedido()  
mostrar_estado()
agregar_pedido("General Pryde", "Kessel", "Requiere refuerzos")
mostrar_estado()