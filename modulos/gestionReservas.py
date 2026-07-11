from .gestionAsientos import  reservar_asiento, liberar_asiento
from .consultas import sumarMillas, canjear_millas, restarMillas
from .gestionAsientos import cargar_matrices_aviones, reservar_asiento, liberar_asiento, guardar_aviones, mostrar_matriz_avion
from .gestionVuelos import cargar_vuelos,seleccion_OrigenDestino

# ─────────────────────────────────────────────
# AVIONES (PERSISTENCIA)
# ─────────────────────────────────────────────

aviones = cargar_matrices_aviones()
vuelos = cargar_vuelos()


# ─────────────────────────────────────────────
# RESERVAS
# ─────────────────────────────────────────────

def cargar_reservas():
    reservas = {}

    try:
        with open("data/reservas.txt", "r", encoding="utf-8") as f:
            for linea in f:
                if not linea.strip():
                    continue

                partes = linea.strip().split(";")

                reservas[partes[0]] = {
                    "id_vuelo": partes[1],
                    "nombre": partes[2],
                    "dni": partes[3],
                    "fila": int(partes[4]),
                    "columna": int(partes[5]),
                    "dia": partes[6],
                    "mes": partes[7],
                    "equipaje": partes[8],
                    "avion": partes[9],
                    "tipo": partes[10]
                }
    except FileNotFoundError:
        return {}

    return reservas


def guardar_reservas(reservas):
    with open("data/reservas.txt", "w", encoding="utf-8") as f:
        for id_reserva, r in reservas.items():
            f.write(";".join([
                str(id_reserva),
                str(r["id_vuelo"]),
                r["nombre"],
                r["dni"],
                str(r["fila"]),
                str(r["columna"]),
                str(r["dia"]),
                str(r["mes"]),
                r["equipaje"],
                str(r["avion"]),
                str(r["tipo"])
            ]) + "\n")


def cargar_contador():
    try:
        with open("data/contador.txt", "r", encoding="utf-8") as f:
            _, valor = f.readline().strip().split("=")
            return int(valor)
    except:
        return 1010


def guardar_contador(valor):
    with open("data/contador.txt", "w", encoding="utf-8") as f:
        f.write(f"contador_reserva={valor}")


# ─────────────────────────────────────────────
# ESTADO EN MEMORIA
# ─────────────────────────────────────────────

reservas = cargar_reservas()

destinos = [
    "BUENOS AIRES, ARGENTINA",
    "MENDOZA, ARGENTINA",
    "SANTA CRUZ, ARGENTINA",
    "MADRID, ESPAÑA",
    "PEKÍN, CHINA",
    "ROMA, ITALIA",
    "LYON, FRANCIA",
    "BOGOTA, COLOMBIA",
    "CARACAS, VENEZUELA"
]



#---------------------------------
# FUNCIONES PARA MODULARIZAR
#--------------------------------

#FUNCIONES
def seleccionar_asiento(matriz):

    mostrar_matriz_avion(matriz)

    while True:
        try:
            entrada = input("Fila,Columna: ")
            f, c = entrada.split(",")

            fila = int(f)
            columna = int(c)

            if fila < 1 or fila > len(matriz):
                print("Fila fuera de rango.")
                continue

            if columna < 1 or columna > len(matriz[0]):
                print("Columna fuera de rango.")
                continue

            if matriz[fila-1][columna-1] == "R":
                print("Asiento ocupado.")
                continue

            if matriz[fila-1][columna-1] == "D":
                print("Asiento seleccionado correctamente.")
                return fila, columna

        except:
            print("Formato inválido. Ejemplo: 5,3")


def seleccionar_equipaje():

    print("\nEquipaje:")
    print("1 - Sin equipaje")
    print("2 - Equipaje de mano $10.000")
    print("3 - Equipaje de bodega $20.000")

    op = input("Opción: ")

    equipaje = {
        "1": "Sin equipaje",
        "2": "Equipaje de mano",
        "3": "Equipaje de bodega"
    }.get(op, "Sin equipaje")

    return equipaje

def calcular_precio(ruta_elegida, vuelos_mes, equipaje):

    precio = 0

    for id_vuelo in ruta_elegida:

        vuelo = vuelos_mes[id_vuelo]

        if vuelo["tipo"] == "nacional":
            precio += 70000
        else:
            precio += 140000

    if equipaje == "Equipaje de mano":
        precio += 10000

    elif equipaje == "Equipaje de bodega":
        precio += 20000

    return precio

def aplicar_millas(precio, dni_pasajero):

    while True:

        usar = input("¿Desea usar sus millas? (s/n): ").lower()

        if usar in ["s","n"]:
            break

        print("Ingrese únicamente s o n.")

    if usar == "s":

        descuento = canjear_millas(dni_pasajero)

        precio -= descuento

        if precio < 0:
            precio = 0

    return precio

def confirmar_compra(nombre, ruta_elegida, equipaje, precio, vuelos_mes):

    print("\n" + "=" * 45)
    print("          RESUMEN DE LA RESERVA")
    print("=" * 45)

    print(f"\nPasajero: {nombre}")

    print("\nRecorrido:")

    for i, id_vuelo in enumerate(ruta_elegida):

        vuelo = vuelos_mes[id_vuelo]

        print(f"\nVuelo {id_vuelo}")
        print(f"  Origen : {vuelo['origen']}")
        print(f"  Destino: {vuelo['destino']}")
        print(f"  Fecha  : {vuelo['dia']}/{vuelo['mes']}/{vuelo['anio']}")
        print(f"  Hora   : {vuelo['hora']}")
        print(f"  Tipo   : {vuelo['tipo'].capitalize()}")

        if i < len(ruta_elegida) - 1:
            print("           ↓ CONEXIÓN ↓")

    print(f"\nEquipaje: {equipaje}")

    print(f"\nTotal a pagar: ${precio:,}".replace(",", "."))

    print("=" * 45)

    while True:

        confirmar = input("\n¿Confirmar reserva? (s/n): ").lower()

        if confirmar in ["s", "n"]:
            return confirmar == "s"

        print("Ingrese únicamente s o n.")
        
def realizar_pago(precio):

    print("\nMétodos de pago")
    print("1 - Dinero en cuenta")
    print("2 - QR Mercado Pago")

    metodo = input("Seleccione método: ")

    if metodo == "1":

        saldo = float(input("Ingrese saldo disponible: "))

        if saldo < precio:
            print("Saldo insuficiente.")
            return False

        print("Pago realizado correctamente.")
        return True

    elif metodo == "2":

        print("\n--- QR DE PAGO ---")

        print("""
        ███████████████████████████
        ██ ▄▄▄▄▄ █▀▀ ▄ ▀█ ▄▄▄▄▄ ███
        ██ █   █ █▄▀▄█▀▄█ █   █ ███
        ██ █▄▄▄█ █ ▀ █ ▄█ █▄▄▄█ ███
        ██▄▄▄▄▄▄▄█ ▀ ▀ █▄█▄▄▄▄▄▄▄██
        ██ ▄▀▄ ▄▄ ▀█▄▀ ▀ ▄▄▀▄▀▄ ███
        ██▀ ▄▄▀▄▄▄█▀▀▀▄█▄▀█ ▄ ▀████
        ██ ▄▄▄▄▄ █▀█ ▄ ▄▀▀▀▄█▄ ████
        ██ █   █ █▄▀█▀▄▄█ ▄▄ ▄█████
        ██ █▄▄▄█ █ ▄█ ▄▀ ▄█▀▄▀█████
        ██▄▄▄▄▄▄▄█▄██▄▄█▄▄█▄▄▄█████
        ███████████████████████████
        """)

        input("Escanee el QR y presione ENTER...")

        print("Pago acreditado.")

        return True

    print("Método inválido.")

    return False

def guardar_reserva(contador, id_vuelo, nombre, dni, fila, columna, equipaje, vuelo, id_avion, tipo):

    reservas = cargar_reservas()

    reservas[str(contador)] = {

        "id_vuelo": id_vuelo,
        "nombre": nombre,
        "dni": dni,
        "fila": fila,
        "columna": columna,
        "dia": vuelo["dia"],
        "mes": vuelo["mes"],
        "anio": vuelo["anio"],
        "equipaje": equipaje,
        "avion": id_avion,
        "tipo": tipo
    }

    guardar_reservas(reservas)

    guardar_contador(contador+1)




def cargar_vuelos():
    vuelos = {}

    with open("data/vuelos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea:
                continue

            datos = linea.split(";")

            id_vuelo = datos[0].strip()

            vuelos[id_vuelo] = {
                "tipo": datos[1].strip(),
                "origen": datos[2].strip(),
                "destino": datos[3].strip(),
                "dia": datos[4].strip(),
                "mes": datos[5].strip(),
                "anio": datos[6].strip(),
                "hora": datos[7].strip(),
                "avion": datos[8].strip()
            }

    return vuelos

def buscar_ruta(origen_actual, destino_final, vuelos, ruta, visitados, ultimo_vuelo=None):

    # Caso base: llegamos al destino
    if origen_actual == destino_final:
        return ruta

    # Recorremos todos los vuelos del diccionario
    for id_vuelo, vuelo in vuelos.items():

        if ultimo_vuelo is not None:
            if int(vuelo["dia"]) < int(ultimo_vuelo["dia"]):
                continue

        # El vuelo tiene que salir desde donde estamos
        if vuelo["origen"] == origen_actual:

            # Vemos si el destino es un lugar en el que ya visitado (asi no ir para atras)
            if vuelo["destino"] in visitados:
                continue

            # Si no lo es guardamos vuelo
            ruta.append(id_vuelo)

            # Marcamos el aeropuerto visitado
            visitados.append(vuelo["destino"])


            # Seguimos buscando desde el nuevo aeropuerto
            resultado = buscar_ruta(
                vuelo["destino"],
                destino_final,
                vuelos,
                ruta,
                visitados, vuelo
            )

            # Encontramos una ruta válida
            if resultado is not None:
                return resultado

            # Este camino no funcionó, volvemos atrás
            ruta.pop()
            visitados.pop()

    # No existe ruta
    return None

def filtrar_vuelos_por_mes(mes):

    vuelos_mes = {}

    for id_vuelo, vuelo in vuelos.items():

        if vuelo["mes"] == str(mes):
            vuelos_mes[id_vuelo] = vuelo

    return vuelos_mes

# ─────────────────────────────────────────────
# CREAR RESERVA
# ─────────────────────────────────────────────


def crear_reserva(dni_pasajero, pasajero):

    global reservas, aviones

    print("\n--- NUEVA RESERVA ---")

    nombre = pasajero[1]

    while True:

        id_Vdirectos = []

        # ---- SELECCION ORIGEN - DESTINO ----
        origen, destino = seleccion_OrigenDestino()

        # ---- MES ----
        while True:

            entrada = input("\nIngrese el mes del viaje (1-12): ").strip()

            if not entrada.isdigit():
                print("Debe ingresar un número.")
                continue

            mes = int(entrada)

            if mes < 1 or mes > 12:
                print("Mes inválido.")
                continue

            if mes <= 6:
                print("No puede ser un mes ya pasado")
                continue

            break

        # ---- FILTRAR VUELOS DEL MES ----
        vuelos_mes = filtrar_vuelos_por_mes(mes)

        # ---- BUSCAR VUELOS DIRECTOS ----
        for id_vuelo, vuelo in vuelos_mes.items():

            if vuelo["origen"] == origen and vuelo["destino"] == destino:
                id_Vdirectos.append(id_vuelo)

        # ---- NO HAY DIRECTOS -> BUSCAR CONEXIÓN ----
        if len(id_Vdirectos) == 0:

            ruta = []
            visitados = [origen]

            conexion = buscar_ruta(
                origen,
                destino,
                vuelos_mes,
                ruta,
                visitados
            )

            if conexion is None:

                input("\nNo existe ninguna ruta disponible. Presione enter para continuar:")
                continue

            print("\nSe encontró la siguiente conexión:\n")

            for i, id_vuelo in enumerate(conexion):

                vuelo = vuelos_mes[id_vuelo]

                print(
                    f"Vuelo {id_vuelo} | "
                    f"{vuelo['origen']} → {vuelo['destino']} | "
                    f"{vuelo['dia']}/{vuelo['mes']} - {vuelo['hora']}"
                )

                if i < len(conexion)-1:
                    print("        ↓ CONEXIÓN ↓")

            while True:

                op = input("\n¿Aceptar esta conexión? (s/n): ").lower()

                if op == "s":
                    ruta_elegida = conexion
                    break

                elif op == "n":
                    break

                print("Opción inválida.")

            if op == "s":
                break

            continue

        # ---- HAY VUELOS DIRECTOS ----

        print("\nVuelos disponibles:\n")

        for i, id_vuelo in enumerate(id_Vdirectos):

            vuelo = vuelos_mes[id_vuelo]

            print(
                f"{i} - "
                f"Vuelo {id_vuelo} | "
                f"{vuelo['dia']}/{vuelo['mes']} | "
                f"{vuelo['hora']}"
            )

        while True:

            opcion = input("Seleccione vuelo: ")

            if opcion.isdigit() and int(opcion) in range(len(id_Vdirectos)):

                ruta_elegida = [id_Vdirectos[int(opcion)]]
                break

        break

    # -----------------------------------------
    # SELECCION DE ASIENTO, EQUIPAJE Y COMPRA 
    # -----------------------------------------

     # ---- RESERVAR CADA TRAMO ----

    for id_vuelo in ruta_elegida:

        vuelo = vuelos_mes[id_vuelo]

        id_avion = vuelo["avion"]

        matriz = aviones[id_avion]

        print(f"\nSeleccione asiento para el vuelo {id_vuelo}")
        print(f"{vuelo['origen']} → {vuelo['destino']}")

        fila, columna = seleccionar_asiento(matriz)

        reservar_asiento(matriz, fila, columna)

        aviones[id_avion] = matriz

        
        equipaje = seleccionar_equipaje()

        contador = cargar_contador()

        guardar_reserva(
            contador,
            id_vuelo,
            nombre,
            dni_pasajero,
            fila,
            columna,
            equipaje,
            vuelo,
            id_avion,
            vuelo["tipo"]
        )

        guardar_contador(contador + 1)

        sumarMillas(dni_pasajero, vuelo)

    guardar_aviones(aviones)

    precio = calcular_precio(
        ruta_elegida,
        vuelos_mes,
        equipaje
    )
    
    print(f"\nSubtotal del viaje: ${precio:,}".replace(",", "."))

    precio = aplicar_millas(precio, dni_pasajero)

    if not confirmar_compra(
        nombre,
        ruta_elegida,
        equipaje,
        precio,
        vuelos_mes
    ):
        print("Reserva cancelada.")
        return

    if not realizar_pago(precio):
        return

   
    print("\nReserva creada correctamente.")



# ─────────────────────────────────────────────
# CANCELAR
# ─────────────────────────────────────────────

def cancelar_reserva(dni_pasajero, pasajero):
    global reservas, aviones

    numero = input("Número reserva: ")

    reserva = reservas.get(numero)

    if not reserva:
        print("No existe")
        return

    if reserva["dni"] != dni_pasajero:
        print("No es tuya")
        return

    id_avion = reserva["avion"]
    matriz = aviones[id_avion]

    liberar_asiento(matriz, reserva["fila"], reserva["columna"])

    aviones[id_avion] = matriz
    guardar_aviones(aviones)

    del reservas[numero]
    guardar_reservas(reservas)

    restarMillas(dni_pasajero, reserva["tipo"])

    print("Cancelada")
