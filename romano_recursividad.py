romano = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


def numero_romano_a_decimal(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]] >= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + numero_romano_a_decimal(numero_romano[1:])
        else:
            return -romano[numero_romano[0]] + numero_romano_a_decimal(numero_romano[1:])


print(numero_romano_a_decimal("mvx"))
