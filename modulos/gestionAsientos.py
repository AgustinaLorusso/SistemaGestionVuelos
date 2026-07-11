import random

# ─────────────────────────────
# MATRICES
# ─────────────────────────────


def crear_matriz_aleatoria():
    return [["R" if random.random() < 0.2 else "D" for _ in range(7)] for _ in range(27)]


def plana_a_matriz(lista_plana):
    return [lista_plana[i*7:(i+1)*7] for i in range(27)]


def matriz_a_plana(matriz):
    return [celda for fila in matriz for celda in fila]


def mostrar_columnas(total, columna=1):
    if columna > total:
        print()
        return

    print(columna, end=" ")
    mostrar_columnas(total, columna + 1) # recursividad


def mostrar_fila(fila, columna=0):
    if columna == len(fila):
        print()
        return

    print(fila[columna], end=" ")
    mostrar_fila(fila, columna + 1) # recursividad


def mostrar_matriz_avion(matriz, fila=0):
    if fila == 0:
        print("\n   ", end="")
        mostrar_columnas(len(matriz[0]))

    if fila == len(matriz):
        return

    print(f"{fila + 1:2} ", end="")
    mostrar_fila(matriz[fila])

    mostrar_matriz_avion(matriz, fila + 1)


def reservar_asiento(matriz, fila, columna):
    if 1 <= fila <= 27 and 1 <= columna <= 7:
        if matriz[fila-1][columna-1] == "D":
            matriz[fila-1][columna-1] = "R"
            return True
        print("Asiento ocupado.")
        return False
    print("Fuera de rango.")
    return False


# ─────────────────────────────
# PERSISTENCIA AVIONES TXT
# ─────────────────────────────

def cargar_matrices_aviones():
    aviones = {}

    columnas = 10  # ajustalo si tu avión tiene otro ancho

    with open("data/aviones.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea:
                continue

            partes = linea.split(";")

            id_avion = partes[0]
            asientos = partes[1].split(",")

            matriz = []

            for i in range(0, len(asientos), columnas):
                matriz.append(asientos[i:i + columnas])

            aviones[id_avion] = matriz

    return aviones


def guardar_aviones(aviones):
    with open("data/aviones.txt", "w", encoding="utf-8") as f:
        for id_avion, matriz in aviones.items():
            plano = matriz_a_plana(matriz)
            linea = id_avion + ";" + ",".join(plano)
            f.write(linea + "\n")


def liberar_asiento(matriz, fila, columna):
    if 1 <= fila <= 27 and 1 <= columna <= 7:
        if matriz[fila-1][columna-1] == "R":
            matriz[fila-1][columna-1] = "D"
            return True
    return False