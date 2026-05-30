
from modulos.menu import bienvenida, administrador, usuario, login_administrador
from modulos.gestionPasajeros import login_cliente , registrar_pasajero

#PROGRAMA PRINCIPAL

while True:
    seleccion = bienvenida()

    if seleccion == 1: #Despliegue de opciones de administrador.
        login_administrador() #Inicio de sesion como administrador.
        administrador()

    elif seleccion == 2:  #Despliegue de opciones de cliente.
        pasajero = login_cliente() #Inicio de sesion como cliente.
        usuario(pasajero)
    
    elif seleccion == 3: #Opcion para registrar un nuevo usuario en el sistema.
        registrar_pasajero()

    elif seleccion == 4: # Opcion para salir del programa.
        print("¡Gracias por confiar en Aerolíneas AIR ARGES!")
        print("Saliendo...")
        break