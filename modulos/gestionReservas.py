from .gestionVuelos import vuelos
from .gestionAsientos import mostrar_matriz, reservar_asiento, matrices_aviones
from .data import reservas, contador_reserva, destinos
from .consultas import sumarMillas, canjear_millas, restarMillas

def crear_reserva(pasajero):
    print("\n--- NUEVA RESERVA ---")

    # 1. BUSCAR PASAJERO
    nombre = pasajero [0]
    dni = pasajero[1]
    email = pasajero[2]

    #SELECCIÓN DE VUELO
    # 1. Elegir origen desde lista cerrada
    print("\nSeleccione origen:\n")
    for i in range(len(destinos)):
        print(i, "-", destinos[i])

    while True:
        opcion = input("\nSeleccione origen: ").strip()
        if opcion.isdigit() and int(opcion) in range(len(destinos)):
            opcion = int(opcion)
            break
        print("Opción inválida, ingrese un número del 0 al", len(destinos) - 1)

    origen = destinos[opcion]               


    if "ARGENTINA" in origen:
        pais_origen = "ARGENTINA"
    elif "ESPAÑA" in origen:
        pais_origen = "ESPAÑA"
    elif "CHINA" in origen:
        pais_origen = "CHINA"
            
    #Tipo de vuelo
    print("\nTipos de vuelo:\n")
    print("1. Vuelos con destino nacional")
    print("2. Vuelos con destino internacional\n")

    tipo = input("Seleccione una opción: ")

    while tipo not in ["1", "2"]:
        print("Opción inválida")
        tipo = input("Seleccione: ")
        
    print("\nVuelos disponibles:\n")

    #implementación de FILTER
    pais_origen = origen.split(",")[1]
    vuelos_disponibles = list(filter(
    lambda vuelo: vuelo[1] == origen and (
        (tipo == "1" and vuelo[2].split(",")[1] == pais_origen and vuelo[2] != origen) or
        (tipo == "2" and vuelo[2].split(",")[1] != pais_origen)
    ),
    vuelos
    ))
                    
    if len(vuelos_disponibles) == 0:
       print("No hay vuelos disponibles para esa selección.")
       return
   
    #implementación de MAP()
    def mostrar_vuelo(v):
        return f"{v[0]} | {v[1]} → {v[2]} | {v[3]}/{v[4]} | {v[5]} hs"

    vuelos_mostrables = list(map(mostrar_vuelo, vuelos_disponibles))

    for i in range(len(vuelos_mostrables)):
        print(i, "-", vuelos_mostrables[i])

    while True:
        opcion = input("\nSeleccione vuelo: ").strip()
        if opcion.isdigit() and int(opcion) in range(len(vuelos_disponibles)):
            opcion = int(opcion)
            break
        print("Opción inválida, ingrese un número del 0 al", len(vuelos_disponibles) - 1)

    vuelo_elegido = vuelos_disponibles[opcion] 

    for reserva in reservas:
        if reserva[1] == vuelo_elegido[0] and reserva[3] == dni:
            print("\nYa tenés una reserva para este vuelo.")
            input("Presione enter para continuar...")
            return
    
    # 5. ELEGIR ASIENTO
    matriz = matrices_aviones[vuelo_elegido[6]]
    mostrar_matriz(matriz)

    while True:
        entrada = input("\nSeleccione fila y columna (ej: 3,5): ")
        partes = entrada.split(",")

        if len(partes) != 2:
            print("Error: debe ingresar dos valores separados por coma (ej: 3,5)")
            continue

        try:
            fila = int(partes[0].strip())
            columna = int(partes[1].strip())
        except ValueError:
            print("Error: ambos valores deben ser números")
            continue

        if fila < 1 or columna < 1 or fila > 27 or columna > 7:
            print("Error: asiento fuera de rango. Ingrese otro.")
            continue

        if reservar_asiento(matriz, fila, columna):
            break


    # 6. ELEGIR EQUIPAJE
    tipo_equipaje = None

    while tipo_equipaje is None:
        print("\nSeleccione tipo de equipaje:")
        print("1. Sin equipaje")
        print("2. Equipaje de mano: $10.000")
        print("3. Equipaje bodega: $20.000")

        opcion = input("\nOpción: ")

        if opcion == "1":
            tipo_equipaje = "Sin equipaje"
        elif opcion == "2":
            tipo_equipaje = "Equipaje de mano"
        elif opcion == "3":
            tipo_equipaje = "Equipaje bodega"
        else:
            print("Opción inválida, intente nuevamente.")

    # 7. CALCULAR PRECIO
    recargos = {
        "Sin equipaje": 0,
        "Equipaje de mano": 10000,
        "Equipaje bodega": 20000
    }

    #utilización de función LAMBDA 

    calcular_total = lambda base, equipaje: base + recargos[equipaje] 

    if tipo == "1":
            precio_pasaje = 70000
    else:
        precio_pasaje = 140000

    precio_total = calcular_total(precio_pasaje, tipo_equipaje)
    
    while True:
        usar_millas = input("\n¿Desea usar millas? (s/n): ").lower()

        if usar_millas == "s":
            descuento = canjear_millas(pasajero)
            precio_total -= descuento
            break

        elif usar_millas == "n":
            break

        else:
            print("Entrada inválida, ingrese 's' o 'n'")

    if precio_total < 0:
        precio_total = 0
        
    # 8. MOSTRAR RESUMEN
    print("\n--- RESUMEN ---")
    print("Pasajero:", nombre)
    print("Vuelo:", vuelo_elegido[1], "→", vuelo_elegido[2])
    print("Asiento:", fila, "-", columna)
    print("Fecha:", vuelo_elegido[3], "/", vuelo_elegido[4])
    print("Hora:", vuelo_elegido[5])
    print("Equipaje:", tipo_equipaje)
    print("Total:", precio_total)


    while True:
        confirmar = input("\n¿Confirmar reserva? (s/n): ").lower()

        if confirmar == "s":
            break

        elif confirmar == "n":
            print("Reserva cancelada.")
            return

        else:
            print("Entrada inválida, ingrese 's' o 'n'")

    # 9. GUARDAR RESERVA
    id_reserva = contador_reserva[0]
    contador_reserva[0] += 1

    nueva_reserva = [
        id_reserva,
        vuelo_elegido[0],
        nombre,
        dni,
        fila,
        columna,
        vuelo_elegido[3],
        vuelo_elegido[4],
        tipo_equipaje,
        vuelo_elegido[6], 
        tipo  
    ]


    reservas.append(nueva_reserva)
    
    sumarMillas(pasajero, vuelo_elegido)

    print("Reserva creada correctamente. Nº:", id_reserva)
    input("Presione enter para continuar...")


# ─────────────────────────────────────────────
# CANCELAR RESERVA
# ─────────────────────────────────────────────
def liberar_asiento(matriz, fila, columna):
    fila -= 1
    columna -= 1

    if matriz[fila][columna] == "R":
        matriz[fila][columna] = "D"
        return True

    return False

def cancelar_reserva(pasajero):

    while True:
        numero_reserva = input("\nIngrese número de reserva a cancelar (4 dígitos): ")

        if not numero_reserva.isdigit():
            print("Error: debe ingresar solo números.\n")
            continue

        if len(numero_reserva) != 4:
            print("Error: el número de reserva debe tener 4 dígitos.\n")
            continue

        numero_reserva = int(numero_reserva)
        break

    reserva_encontrada = None

    for reserva in reservas:
        if reserva[0] == numero_reserva:
            reserva_encontrada = reserva
            break

    if reserva_encontrada is None:
        print("\nNo se encontró la reserva.")
        return
    
    if reserva_encontrada[3] != pasajero[1]:
        print("\nNo podés cancelar una reserva que no te pertenece.")
        return

    reservas.remove(reserva_encontrada)
    print("\nReserva cancelada correctamente.")
    
    # Liberar asiento
    avion = reserva_encontrada[9]

    if isinstance(avion, list):
        avion = avion[0]

    matriz = matrices_aviones[avion]
    fila = reserva_encontrada[4]
    columna = reserva_encontrada[5]

    liberar_asiento(matriz, fila, columna)
    
    #Restar Millas
    vuelo = reserva_encontrada[10]
    restarMillas(pasajero, vuelo)