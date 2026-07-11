# Importaciones

from .gestionAsientos import *
from .gestionReservas import crear_reserva, cancelar_reserva
from .gestionPasajeros import buscar_reserva_por_numero
from .consultas import *
from .gestionVuelos import *
from .data import administradores
import re

# Funciones relacionadas con el menu de los distintos usuarios del sistema.


def bienvenida():
    """Funcion de bienvenida al programa principal"""

    print("SISTEMA DE GESTIÓN DE AEROLÍNEA")
    print("----------AIR ARGES------------")
    print("\nSeleccione una opción:\n")
    print("1. Iniciar sesión como Administrador")
    print("2. Iniciar sesión como Cliente")
    print("3. Crear cuenta")
    print("4. Salir")
    opciones = [1, 2, 3, 4]

    # VALIDACION CON LA IMPORTADA DE GESTION DE VUELOS ( VALIDACION segun opciones )
    seleccion = validaciones(opciones)
    while seleccion is False:
        seleccion = validaciones(opciones)

    return seleccion


def menu_administrador():
    """Funcion que muestra el menu de opciones del administrador"""

    print("\n-----MENÚ ADMINISTRADOR----\n")
    print("1. Programar vuelo")
    print("2. Eliminar un vuelo existente")
    print("3. Consultas de administrador")
    print("4. Cerrar sesión\n")

    opciones = [1, 2, 3, 4]

    # VALIDACION CON LA IMPORTADA DE GESTION DE VUELOS ( VALIDACION segun opciones )
    seleccion = validaciones(opciones)
    while seleccion is False:
        seleccion = validaciones(opciones)

    return seleccion


def menu_Consultas_Administrador():
    """Función para consultas del administrador"""

    print("\n--------MENÚ CONSULTAS-----------\n")
    print("1. Ver Reservas existentes de clientes")
    print("2. Ver Vuelos existentes")
    print("3. Buscar pasajero por ID")
    print("4. Ver pasajeros por vuelo")
    print("5. Ver cantidad de vuelos por mes")
    print("6. Volver al menú anterior")

    opciones = [1, 2, 3, 4, 5, 6]

    # VALIDACION CON LA IMPORTADA DE GESTION DE VUELOS ( VALIDACION segun opciones )
    seleccion = validaciones(opciones)
    while seleccion is False:
        seleccion = validaciones(opciones)

    return seleccion


def login_administrador():
    """Funcion de log in para administradores"""

    # VALIDACIONES PARA EL INGRESO DEL MAIL
    while True:
        email = input("\nEmail: ").strip().lower()

        if not email:
            print("El email no puede estar vacío.")
            continue

        if " " in email:
            print("El email no puede contener espacios.")
            continue

        if re.match(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", email) is None:
            print("Formato de email inválido.")
            continue

        contraseña = input("Contraseña: ").strip()

        login_ok = False

        for administrador in administradores:
            if administrador["email"] == email and administrador["password"] == contraseña:
                print("\nLogin correcto.")
                login_ok = True
                break

        if login_ok:
            break  # sale del while

        print("Credenciales incorrectas.")


def administrador():
    """Gestiona las acciones disponibles para el administrador de la aerolínea, mostrando un menú de opciones y ejecutando la funcionalidad correspondiente según la selección del usuario."""

    sesion_activa = True  # SESION DENTRO DEL MENU PRINCIPAL DE ADMINISTRADOR
    sesion_activa2 = True  # SESION DENTRO DEL MENU DE CONSULTAS DEL ADMINISTRADOR

    while sesion_activa:

        seleccion = menu_administrador()  # MENU PRINCIPAL DE ADMINISTRADOR

        if seleccion == 1:
            crearVuelo()
            input("Presione enter para continuar...")

        elif seleccion == 2:
            eliminarVuelo()
            input("Presione enter para continuar...")

        elif seleccion == 3:

            while sesion_activa2:

                seleccion = (
                    menu_Consultas_Administrador()
                )  # MENU DE CONSULTAS DEL ADMINISTRADOR

                if seleccion == 1:
                    visualizarReservas()
                    input("Presione enter para continuar...")

                elif seleccion == 2:
                    visualizarVuelos()
                    input("Presione enter para continuar...")

                elif seleccion == 3:
                    pasajerosPorID()
                    input("Presione enter para continuar...")

                elif seleccion == 4:
                    pasajerosPorVuelo()
                    input("Presione enter para continuar...")

                elif seleccion == 5:
                    contar_vuelos_por_mes()
                    input("Presione enter para continuar...")

                elif seleccion == 6:
                    sesion_activa2 = False

        elif seleccion == 4:

            print("Sesión cerrada.\n")

            sesion_activa = False

    return False


def menuCliente():
    """Función para mostrar el menú a el cliente"""

    print("\nMENÚ CLIENTE\n")
    print("1. Crear reserva")
    print("2. Cancelar reserva")
    print("3. Consultas")
    print("4. Cerrar sesión")

    opcion = input(
        "\nSeleccione una opción: "
    )  # Input para que el usuario seleccione una opción

    while opcion not in [
        "1",
        "2",
        "3",
        "4",
    ]:  # Bucle para seguir ingresando la opción por si el usuario ingresa alguna opción que no esté en el menú
        print("Opción inválida. Intente nuevamente.\n")
        opcion = input("Seleccione una opción: ")

    return opcion


def menuConsultas():  # Función para consultas del usuario
    print("MENÚ CONSULTAS\n")
    print("1. Ver una reserva")
    print("2. Ver todas mis reservas")
    print("3. Ver millas")
    print("4. Ver datos personales")
    print("5. Volver al menú anterior")

    opcion = input(
        "\nSeleccione una opción: "
    )  # Input para que el usuario seleccione una opción

    while opcion not in [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]:  # Bucle para ingresar nuevamente la opción si el usuario ingresa un número que no está en las opciones
        print("Opción inválida. Intente nuevamente.\n")
        opcion = input("\nSeleccione una opción: ")

    return opcion  # Devuelve opción


def usuario(pasajero):  # Función del usuario
    sesion_activa = True  # Sesión activa actúa como flag para saber si el usuario quiere continuar en el menu del cliente o volver al menú principal de bienvenida
    sesion_activa2 = True  # Sesión activa actúa como flag para saber si el usuario quiere continuar en el menu de consultas o volver al menú de cliente
    dni = pasajero[1]  # Obtenemos dni de pasajero

    while sesion_activa == True:  # Bucle para continuar en menuCliente
        seleccion = menuCliente()
        sesion_activa2 = True  # Acá vuelvo a reiniciar la flag por si quiere generar una reserva y volver a menuConsultas, de lo contrario no le permitirá visualizar el menuConsultas

        if seleccion == "1":
            crear_reserva(pasajero)  # llamo función para crear reserva
        if seleccion == "2":
            cancelar_reserva(pasajero)  # llamo función para cancelar una reserva
        if seleccion == "3":
            while sesion_activa2 == True:  # Bucle para continuar en menuConsultas
                seleccion = menuConsultas()

                if seleccion == "1":
                    buscar_reserva_por_numero(
                        pasajero
                    )  # llamo función para consultar una reserva a partir de su ID
                if seleccion == "2":
                    MisReservas(
                        dni
                    )  # llamo función para visualizar todas las reservas del pasajero a partir de su dni
                    input("Presione enter para continuar...")
                if seleccion == "3":
                    verMillas(
                        pasajero
                    )  # llamo función para visualizar millas de un pasajero
                if seleccion == "4":
                    verDatos(
                        pasajero
                    )  # llamo función para ver todos los datos asociados a un pasajero
                if seleccion == "5":
                    sesion_activa2 = False  # cambio flag para volver al menú anterior
        if seleccion == "4":
            print("Cerrando sesión...")
            sesion_activa = False  # cambio flag para cerrar sesión

    return False
