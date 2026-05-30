#Validacion para selecciones del usuario
def validaciones(opciones):
    
    entrada = input("\nSeleccione una opción: ").strip()

    if not entrada:
        print("Debe ingresar un número.")
        return False

    try:
        entrada = int(entrada)
    except ValueError:
        print("Debe ser un número entero (sin puntos ni letras).")
        return False

    if entrada not in opciones:
        print("Opción no válida.")
        return False

    return entrada

def validar_sn():
    opcion = input("Ingrese si/no : ").lower().strip()

    while opcion not in ["si", "no"]:

        print("Error: elija una opción válida.")

        opcion = input("Ingrese si/no : ").lower().strip()
    
    return opcion 

    