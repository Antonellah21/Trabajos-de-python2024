# sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;
mochila = ["suministros", "comunicador", "botella_de_agua", "sable de luz"]


def usar_la_fuerza(mochila, objeto_quitado=0):
    if len(mochila) == 0:
        return print("el objeto no se encontro")
    objeto = mochila.pop(0)
    if objeto == "sable de luz":
        return print(f"para encontar el sable de luz tuve que quitar {objeto_quitado} objetos")
    else:
        print(f"se encontro el objeto {objeto} en la mochila")
        objeto_quitado += 1
        return usar_la_fuerza(mochila, objeto_quitado)


print(usar_la_fuerza(mochila))
