import random

def crear_matriz():
    """Función para crear una matriz de asientos con valores aleatorios "D" (disponible) y "R" (reservado)"""
    matriz = []
    for i in range(27):
        fila = []
        for j in range(7):
            if random.randint(0, 1) == 0:
                fila.append("D")
            else:
                fila.append("R")
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    """Función para mostrar la matriz de asientos de manera legible."""
    print("\n      1  2  3  4  5  6  7")

    for i in range(27):
        print(f"{i + 1:3}   ", end="")

        for j in range(7):
            print(f"{matriz[i][j]:2}", end=" ")

        print()


def reservar_asiento(matriz, fila, columna):
    """Función para reservar un asiento específico en la matriz."""

    if fila < 1 or columna < 1:
        print("La fila y columna deben ser mayores a 0.")
        return False

    fila -= 1
    columna -= 1

    if fila >= 27 or columna >= 7:
        print("La fila o columna ingresada no existe.")
        return False

    if matriz[fila][columna] == "D":
        matriz[fila][columna] = "R"
        print("El asiento ha sido reservado correctamente.")
        return True
    
    if matriz[fila][columna] == "R":
        print("El asiento se encuentra ocupado, elija otro.")

    return False


def pedir_asiento(matriz):
    """Pide al usuario un asiento válido hasta que se reserve correctamente"""

    while True:
        try:
            fila = int(input("Ingrese fila: "))
            columna = int(input("Ingrese columna: "))
        except ValueError:
            print("Error: debe ingresar números")
            continue

        if fila < 1 or columna < 1 or fila > 27 or columna > 7:
            print("Error: asiento fuera de rango. Ingrese otro.")
            continue

        if reservar_asiento(matriz, fila, columna):
            return fila, columna

        print("Asiento ocupado, elija otro.")


#se crea una matriz por avión
matrices_aviones = {
    "av1": crear_matriz(),
    "av2": crear_matriz(),
    "av3": crear_matriz(),
    "av4": crear_matriz(),
    "av5": crear_matriz(),
    "av6": crear_matriz()
}