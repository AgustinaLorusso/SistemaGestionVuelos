from modulos.fileManager import leer_archivo, escribir_archivo
import re

# --- FUNCIONES DE APOYO INTERNAS ---
def obtener_lista_pasajeros():
    return leer_archivo("data/pasajeros.txt")

def guardar_lista_pasajeros(lista):
    escribir_archivo("data/pasajeros.txt", lista)

# --- FUNCIONES CLIENTE ---

def MisReservas(dni):
    """Visualiza las reservas de un usuario filtrando directamente del archivo"""
    todas_las_reservas = leer_archivo("data/reservas.txt")
    reservasUsuario = [r for r in todas_las_reservas if r[3] == dni]
    
    if not reservasUsuario:
        print("\nNo se encontraron reservas.")
    else:
        for r in reservasUsuario:
            print(f"\nReserva N°: {r[0]} | Vuelo: {r[1]} | Pasajero: {r[2]} | DNI: {r[3]}")
            print(f"Fila: {r[4]} | Columna: {r[5]} | Día/Mes: {r[6]}/{r[7]}")
            print(f"Equipaje: {r[8]} | Avión: {r[9]}")
            print("------------------------")

def sumarMillas(dni_pasajero, vuelo):
    pasajeros = obtener_lista_pasajeros()

    origen = vuelo["origen"]
    destino = vuelo["destino"]

    pais_origen = origen.split(",")[1].strip()
    pais_destino = destino.split(",")[1].strip()

    es_nacional = pais_origen == pais_destino

    millas_a_sumar = 100 if es_nacional else 500

    encontrado = False

    for p in pasajeros:
        if str(p[2]) == str(dni_pasajero):
            p[5] = str(int(p[5]) + millas_a_sumar)
            encontrado = True
            break

    if encontrado:
        guardar_lista_pasajeros(pasajeros)
        print(f"\nSe sumaron {millas_a_sumar} millas.")
        
def restarMillas(dni_pasajero, tipo_vuelo):
    """Resta millas y persiste"""
    pasajeros = obtener_lista_pasajeros()
    millas_a_restar = 100 if tipo_vuelo == "1" else 500

    for p in pasajeros:
        if p[2] == dni_pasajero:
            actuales = int(p[5]) - millas_a_restar
            p[5] = str(max(0, actuales)) 
            break
            
    guardar_lista_pasajeros(pasajeros)
    print("\nSe restaron millas por cancelación y se guardaron los cambios.")

def canjear_millas(dni_pasajero):
    """Gestiona el canje de millas: Verifica, descuenta del archivo y retorna el valor monetario"""
    pasajeros = obtener_lista_pasajeros()
    pasajero = next((p for p in pasajeros if p[2] == dni_pasajero), None)
    
    if not pasajero:
        return 0

    millas_actuales = int(pasajero[5])
    print(f"\n--- CANJE DE MILLAS ---")
    print(f"Millas disponibles: {millas_actuales}")
    print("Opciones:")
    print("1. $10.000 (100 millas)") 
    print("2. $30.000 (250 millas)") 
    print("3. $70.000 (500 millas)")

    opciones = {"1": (100, 10000), "2": (250, 30000), "3": (500, 70000)}
    opc = input("Seleccione opción: ")
    
    if opc in opciones:
        costo, desc = opciones[opc]
        if millas_actuales >= costo:
            pasajero[5] = str(millas_actuales - costo)
            guardar_lista_pasajeros(pasajeros)
            print(f"Canje exitoso. Millas restantes: {pasajero[5]}")
            return desc
    
    print("\nNo tenés suficientes millas o opción inválida.")
    return 0

def verMillas(dni):
    pasajeros = obtener_lista_pasajeros()

    pasajero = next((p for p in pasajeros if str(p[2]) == str(dni)), None)

    print("\nMillas acumuladas:", pasajero[5])
    input("\nPresione enter para continuar...")
    
def verDatos(pasajero):
    dni = pasajero[2]
    """Función para ver los datos de un pasajero, a partir del parámetro pasajero"""
    pasajeros = obtener_lista_pasajeros()

    pasajero = next((p for p in pasajeros if str(p[2]) == str(dni)), None)
    
    print("\n--- DATOS DEL PASAJERO ---")
    print("Nombre:", pasajero[1])#Muestra nombre
    print("DNI:", pasajero[2])#Muestra DNI
    print("Email:", pasajero[3])#Muestra email
    print("Millas:", pasajero[5])#Muestra millas acumuladas
    input("\nPresione enter para continuar...")
    
def visualizarVuelos():
   with open("data/vuelos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:

        linea = linea.strip()

        if not linea:
            continue

        datos = linea.split(";")

        if len(datos) != 9:
            print("Línea inválida:", linea)
            continue

        print("Vuelo #", datos[0])
        print("Tipo:", datos[1])
        print("Origen:", datos[2])
        print("Destino:", datos[3])
        print("Fecha:", f"{datos[4]}/{datos[5]}/{datos[6]}")
        print("Horario:", datos[7])
        print("Avión:", datos[8])
        print("------------------------")
        
            
def pasajerosPorVuelo():
    """Función para visualizar los pasajeros de un vuelo"""

    while True:
        nro_vuelo = input("Ingrese el número de vuelo: ").strip()

        if nro_vuelo == "":
            print("No podés dejar el campo vacío.")
            continue

        if not nro_vuelo.isdigit():
            print("Debe contener solo números.")
            continue

        if len(nro_vuelo) != 4:
            print("Debe tener exactamente 4 dígitos.")
            continue

        # Validar existencia del vuelo en vuelos.txt
        existe = False

        with open("data/vuelos.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(";")  # <-- corregido
                if datos[0] == nro_vuelo:
                    existe = True
                    break

        if existe:
            break

        opcion = input("Número de vuelo inválido. ¿Desea continuar? (s/n): ").lower()

        while opcion not in ("s", "n"):
            opcion = input("Opción inválida. ¿Desea continuar? (s/n): ").lower()

        if opcion == "n":
            return

    encontrado = False

    with open("data/reservas.txt", "r", encoding="utf-8") as f:
        for linea in f:
            reserva = linea.strip().split(";")  # <-- corregido

            if reserva[1] == nro_vuelo:
                print(
                    f"Número de reserva: {reserva[0]} | "
                    f"Pasajero: {reserva[2]} | "
                    f"DNI: {reserva[3]}"
                )
                encontrado = True

    if not encontrado:
        print("No hay pasajeros para ese vuelo.")

# --- FUNCIONES ADMINISTRADOR ---

def visualizarReservas(): 
    reservas = leer_archivo("data/reservas.txt")
    print("Datos de las reservas: ")
    for r in reservas:
        print(f"\nReserva N°: {r[0]} | Vuelo: {r[1]} | Pasajero: {r[2]} | DNI: {r[3]}")
        print("------------------------")

def pasajerosPorID():
    dni = input("\nIngrese DNI: ").strip()
    pasajeros = obtener_lista_pasajeros()

    for p in pasajeros:
        if p[1].strip() == dni:          # Formato: usuario;DNI;nombre...
            print(f"Pasajero: {p[2]} | Email: {p[3]} | Millas: {p[5]}")
            return

        elif p[2].strip() == dni:        # Formato: usuario;nombre;DNI...
            print(f"Pasajero: {p[1]} | Email: {p[3]} | Millas: {p[5]}")
            return

    print("\nNo se encontró ese DNI.")


def pasajero_mayor_millas(pasajeros, i=0, mayor=None):
    if i == len(pasajeros):
        return mayor

    if mayor is None or int(pasajeros[i][5]) > int(mayor[5]):
        mayor = pasajeros[i]

    return pasajero_mayor_millas(pasajeros, i+1, mayor)