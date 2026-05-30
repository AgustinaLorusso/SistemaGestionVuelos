from .data import reservas, pasajeros, vuelos #Importa la lista global de reservas desde otro módulo
import re

#FUNCIONES CLIENTE

def MisReservas(dni):
      
    """Función que permite visualizar las reservas de un usuario a partir de su DNI"""
    
    reservasUsuario = list(filter(lambda r: r[3] == dni, reservas))
    
    if len(reservasUsuario) == 0:  #Verifica si no se encontró ninguna reserva
        print("\nNo se encontraron reservas.")  #Informa que no hay resultados
    else:  #Si sí hay reservas encontradas
         for r in reservasUsuario:
            print("\nReserva N°:", r[0])
            print("Vuelo:", r[1])
            print("Pasajero:", r[2])
            print("DNI:", r[3])
            print("Fila:", r[4], "Columna:", r[5])
            print("Día/Mes:", r[6], "/", r[7])
            print("Equipaje:", r[8])
            print("Avión:", r[9])
            print("------------------------")
        
def sumarMillas(pasajero, vuelo): 
    
    """Función para sumar millas obtenidas a partir de la confirmación de un vuelo, como parámetros tiene al pasajero y el tipo de vuelo que se confirmó, dado que si es nacional no suma lo mismo que si fuese internacional."""
    
    if vuelo[1].split(",")[1] == vuelo[2].split(",")[1]: #Determina si el vuelo es nacional o internacional
        millas = 100  #Nacional
    else:
        millas = 500  #Internacional

    
    pasajero[4] += millas #Suma al acumulador del pasajero

    
    print("\nSe sumaron", millas, "millas.\n") #Muestra cuántas millas se agregaron
    
def restarMillas(pasajero, vuelo):
    
    """Resta las millas previamente otorgadas por un vuelo cancelado"""

    if vuelo == "1":
        millas = 100   # Nacional
    else:
        millas = 500   # Internacional

    pasajero[4] -= millas

    # Evitar negativos
    if pasajero[4] < 0:
        pasajero[4] = 0

    print("\nSe restaron", millas, "millas por cancelación.")
    input("\nPresione enter para continuar...")
    
def verMillas(pasajero): 
    
    """Función para ver las millas de un pasajero, a partir del parámetro pasajero"""
    
    print("\nMillas acumuladas:", pasajero[4]) #Imprime el total de millas
    input("\nPresione enter para continuar...")

def canjear_millas(pasajero):
    
    print("\n--- CANJE DE MILLAS ---")
    print("\nMillas disponibles:", pasajero[4])

    print("\nOpciones:")
    print("1. $10.000 (100 millas)")
    print("2. $30.000 (250 millas)")
    print("3. $70.000 (500 millas)\n")

    while True:
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            costo = 100
            descuento = 10000
            break
        elif opcion == "2":
            costo = 250
            descuento = 30000
            break
        elif opcion == "3":
            costo = 500
            descuento = 70000
            break
        else:
            print("Opción inválida, intente nuevamente")

    if pasajero[4] < costo:
        print("\nNo tenés suficientes millas.")
        input ("\nPresione enter para continuar...")
        return 0

    pasajero[4] -= costo

    print("\nCanje realizado. Millas restantes:", pasajero[4])

    return descuento

def verDatos(pasajero):
    
    """Función para ver los datos de un pasajero, a partir del parámetro pasajero"""
    
    print("\n--- DATOS DEL PASAJERO ---")
    print("Nombre:", pasajero[0])#Muestra nombre
    print("DNI:", pasajero[1])#Muestra DNI
    print("Email:", pasajero[2])#Muestra email
    print("Millas:", pasajero[4])#Muestra millas acumuladas
    input("\nPresione enter para continuar...")
    
    
##FUNCIONES ADMINISTRADOR
    
def visualizarReservas(): 
    
    """Función para visualizar todas las reservas de la aerolínea"""
    
    print("Datos de las reservas: ")
    for reserva in reservas: #Bucle que recorre la lista reservas
        print("\nReserva N°:", reserva[0])
        print("Vuelo:", reserva[1])
        print("Pasajero:", reserva[2])
        print("DNI:", reserva[3])
        print("Fila:", reserva[4], "Columna:", reserva[5])
        print("Día/Mes:", reserva[6], "/", reserva[7])
        print("Equipaje:", reserva[8])
        print("Avión:", reserva[9])
        print("------------------------")

def visualizarVuelos(): 
    
    """Función para visualizar los vuelos existentes en la aerolínea"""
    
    print("Datos de los vuelos: ")
    for vuelo in vuelos: #Bucle que recorre la lista vuelos
        print("Vuelo #", vuelo[0])
        print("Origen: ", vuelo[1])
        print("Destino:", vuelo[2])
        print("Día/Mes:", vuelo[3], "/", vuelo[4])
        print("Horario: ", vuelo[5])
        print("Avión: ", vuelo[6])
        print ("------------------------\n")
        print("\n")

def pasajerosPorID():
    
    """Función para visualizar la información de un pasajero a partir de su ID"""
    
    while True:
        dni = input("\nIngrese el DNI (todo junto y sin puntos): ").strip()

        if not re.match(r'^\d{7,9}$', dni):
            print("Error: el DNI debe tener entre 7 y 9 dígitos numéricos.")
            continue

        if len(dni) not in [7, 8, 9]:
            print("Error: el DNI debe tener entre 7 y 9 dígitos.")
            continue
        
        break
    
    for pasajero in pasajeros: #Bucle que recorre la lista pasajeros
        if pasajero[1] == dni: #Verifica si existe algún dni en algún pasajero que coincida con el dni ingresado
            print("Pasajero: ", pasajero[0])
            print("DNI: ", pasajero[1])
            print("Email: ", pasajero[2])
            print("Pasajero: ", pasajero[4])
            return
    
    print("\nNo se encontró un pasajero con ese DNI.\n")#Sino imprime que no se encontró

def pasajerosPorVuelo(): 
    """Función para visualizar los pasajeros de un vuelo"""
    
    while True:
        nro_vuelo = input("\nIngrese el número de vuelo: ").strip()
        
        if nro_vuelo == "":
            print("No podés dejar el campo vacío.")
            continue
        
        if not nro_vuelo.isdigit():
            print("Debe contener solo números.")
            continue
        
        if len(nro_vuelo) != 4:
            print("Debe tener exactamente 4 dígitos.")
            continue
        
        existe = False
        
        for vuelo in vuelos:
            if str(vuelo[0]) == nro_vuelo:
                existe = True
                break
        
        if existe:
            break  
        
        opcion = input("Número de vuelo inválido. ¿Desea continuar? (s/n): ").lower()
        
        while opcion != "s" and opcion != "n":
            opcion = input("Opción inválida. ¿Desea continuar? (s/n): ").lower()
        
        if opcion == "n":
            return

   
    encontrado = False
    
    for reserva in reservas:
        if str(reserva[1]) == nro_vuelo:
            print(f"\nNúmero de reserva: {reserva[0]}, Pasajero: {reserva[2]}, DNI: {reserva[3]}")
            encontrado = True
    
    if not encontrado:
        print("No hay pasajeros para ese vuelo.")