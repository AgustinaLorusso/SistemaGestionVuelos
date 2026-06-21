import json
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

def modificiar_archivo(nombre_archivo, id, clave, valor):
    #primero leer el archivo
    with open(nombre_archivo,"r", encoding= "utf-8") as archivo:
        nom_archivo = json.load(archivo) #lee desde un archivo
    nom_archivo[id][clave]= valor
    with open(nombre_archivo,"w", encoding= "utf-8") as archivo:
        json.dump(nom_archivo,archivo,indent=4)

def cargar_json(nombre_archivo, id , datos):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        nom_archivo = json.load(archivo)
    nom_archivo[id] = datos #estan entre llaves.
    with open(nombre_archivo,"w", encoding= "utf-8") as archivo:
        json.dump(nom_archivo,archivo,indent=4)

    





    