from .validaciones import validaciones
import calendar , random
from .fileManager import leer_archivo
from .gestionAsientos import crear_matriz_aleatoria
#DESTINOS 
destinos = ("BUENOS AIRES, ARGENTINA" ,"SANTA CRUZ, ARGENTINA", "MENDOZA, ARGENTINA", "MADRID, ESPAÑA","PEKÍN, CHINA", "ROMA, ITALIA","LYON, FRANCIA", "CARACAS, VENEZUELA","BOGOTA, COLOMBIA")

#HORARIOS POSBILES PARA GENERAR VUELOS
horarios = [ "8:30" , "12:30 ", "20:30 ", "23:30"]

# FUNCIONES DE VALIDACION 

#Validacion para numero de vuelo
def validar_nroVuelo():
    
    """Funcion para validar que numero de vuelo exista"""

    while True:
        nroVuelo = input("\nIngrese el numero de vuelo: ").strip()

        if not nroVuelo:
            print("No puede estar vacío")
            continue

        try:
            nroVuelo = int(nroVuelo)
        except ValueError:
            print("Debe ser un número entero (sin puntos ni letras)")
            continue

        if nroVuelo < 1000 or nroVuelo > 9999:
            print("El número de vuelo debe tener 4 dígitos")
            continue

        return nroVuelo

#Funciones que se invocan en las funciones principales de administrador  (CREAR, MODIFICAR, ELIMINAR VUELOS)

def presentacion_programacion_vuelos():

    "Funcion que presenta la plataforma de programacion de vuelos"

    print("---------SISTEMA DE PROGRAMACION DE VUELOS---------------\n")
    print("El sistema te guiará automáticamente mostrando solo opciones válidas según las reglas operativas para eficiencia logistica\n")

    print("• Vuelos internacionales y Cabotaje:")
    print("Hasta dos vuelos de ida y dos de vuelta por dia en distintos horarios determinados.\n")

    print("• Domingos: no disponible programar vuelos. Aviones en MANTENIMIENTO\n ")

def mostrar_opciones(lista):
    """Funcion para visualizar opciones para un usuario"""
    count=1
    opciones = []
    for i in range(len(lista)):
            opciones.append(count)
            print(f"{count}. {lista[i]}")
            count = count + 1
    return (opciones)
    
def seleccion_OrigenDestino():

    """Funcion que asigna pide al administrador el origen y destino del vuelo"""
    listaDestinos = list(destinos)

    #MUESTRA DE OPCIONES DE ORIGEN 
    print("------- NUEVO VUELO --------")
    print("\n------SELECCION DE ORIGEN----\n\n")

    #VALIDACION DE DATO
    opciones = mostrar_opciones(listaDestinos)  #Opciones del usuario para poder validar
    eleccion = validaciones(opciones)
    while eleccion is False:
        print("\n")
        print("\n------SELECCION DE ORIGEN----\n\n")
        opciones = mostrar_opciones(listaDestinos)
        eleccion = validaciones(opciones)

    #GUARDA ORIGEN   
    origen = listaDestinos[eleccion - 1]
    print(origen)

    #MUESTRA DESTINOS POSIBLES  
    print("\n------SELECCION DE DESTINO----\n\n")
    listaDestinos.pop(eleccion-1) #Elimina de las opciones el origen
    opciones = mostrar_opciones(listaDestinos)
    eleccion  = validaciones(opciones)

    while eleccion is False:
        print("\n------SELECCION DE DESTINO----\n\n")
        print("\n")
        opciones = mostrar_opciones(listaDestinos)
        eleccion = validaciones(opciones)

    #GUARDA DESTINO
    destino = listaDestinos[eleccion - 1]

    return(origen,destino)

def seleccion_horario():

    print("\n------SELECCION DE HORARIO----\n\n")
    opciones = mostrar_opciones(horarios)
    eleccion = validaciones(opciones)
    while eleccion is False:
        print("\n------SELECCION DE HORARIO----\n\n")
        opciones = mostrar_opciones(horarios)
        eleccion = validaciones(opciones)
    horario = horarios[eleccion -1]

    return(horario)

def tipo_vuelo(origen,destino):
 
    """Funcion que asigna que tipo de vuelo es el que se esta programando en base a su orgien y destino"""

    internacionales = ["MADRID, ESPAÑA", "PEKÍN, CHINA", "ROMA, ITALIA","LYON, FRANCIA", "CARACAS, VENEZUELA","BOGOTA, COLOMBIA"]

    if (destino or origen) in internacionales:
        tipoVuelo = " internacional"
    else:
        tipoVuelo = "nacional"
  
    return tipoVuelo

def Asignacion_FechaVuelo():

    """Funcion que pide fecha en la que se quiere programar el vuelo y valida si es posible segun las condiciones planteadas"""

    while True:
        # ---- MES ----
        entrada = input("\nIngrese el mes del viaje (1-12): ").strip()

        if not entrada or not entrada.isdigit():
            print("Debe ingresar un número.")
            continue

        mes = int(entrada)

        if mes < 1 or mes > 12:
            print("Mes inválido.")
            continue

        break

    while True:

        # ---- DÍA ----
        print("\n")
        print(calendar.month(2026, mes)) #Muestra calendario 

        entrada = input("Ingrese el día del viaje: ").strip()

        if not entrada or not entrada.isdigit():
            print("Debe ingresar un número")
            continue

        dia = int(entrada)

        # validar cantidad real de días del mes
        _, dias_en_mes = calendar.monthrange(2026, mes)

        if dia < 1 or dia > dias_en_mes:
            print("Día inválido para ese mes.")
            continue

        # ---- DOMINGO ---- #Verifica que dia seleccionado no es domingo.
        dia_semana = calendar.weekday(2026, mes, dia)

        if dia_semana == 6:
            print("No se puede programar un vuelo en domingo.")
            print("El avión está en mantenimiento.")
            continue
        break 
        
    print(f"Fecha válida seleccionada: {dia}/{mes}/2026\n")
    return (mes,dia)
            

def asignacion_avion(dia, mes, horario):

    """Asigna el primer avión disponible"""

    vuelos = leer_archivo("Gestion_Vuelos/data/vuelos.txt")

    for numero in range(1, 17):

        avion = f"av{numero}"
        ocupado = False

        for vuelo in vuelos:

            if (
                vuelo[8] == avion and      # avión
                int(vuelo[4]) == dia and   # día
                int(vuelo[5]) == mes and   # mes
                vuelo[7] == horario        # horario
            ):
                ocupado = True
                break

        if not ocupado:
            return avion

    return None


def contar_vuelos_por_mes():

    vuelos = leer_archivo("data/vuelos.txt")

    while True:
        entrada = input("\nIngrese el mes (1-12): ").strip()

        if not entrada.isdigit():
            print("Debe ingresar un número.")
            continue

        mes = int(entrada)

        if mes < 1 or mes > 12:
            print("Mes inválido.")
            continue

        break

    total = sum(1 for vuelo in vuelos if int(vuelo[5]) == mes)

    print(f"\nVuelos programados en el mes {mes}: {total}\n")



#Funciones para ADMINISTRADOR 

#Funcion para crear vuelos.


def crearVuelo():

    """Funcion que le permite al administrador crear vuelos y guardarlos en la base de datos (vuelos) """
    
    vuelos= leer_archivo("Gestion_Vuelos/data/vuelos.txt")
    
    while True: 

        presentacion_programacion_vuelos()

        origen,destino= seleccion_OrigenDestino()

        tipoVuelo = tipo_vuelo(origen,destino)

        mes,dia = Asignacion_FechaVuelo()

        horario = seleccion_horario()

        avion = asignacion_avion(dia, mes, horario)

        if  avion == None:
         print("Vuelo no pudo ser guardado, todos los aviones estan ocupados para condiciones ingresadas")
         continue

        break
    
    #Asignacion de nro de identificacion del vuelo.
    idVuelo= random.randint(1000, 9999)

    #Para que el ID del vuelo sea unico verificamos en la lista VUELOS que ese ID no este utilizado.

    for vuelo in vuelos:
        #Miramos si esta sino volvemos a generar otro hasta que no se repita.
        while idVuelo in vuelo:
            idVuelo= random.randint(1000, 9999)

    with open("data/aviones.txt", "a", encoding="utf-8") as archivo:

        nro_avion = random.randint(1, 999)
        avion = f"av{nro_avion}"

        asientos = crear_matriz_aleatoria()

        # Convierte la matriz a una lista plana
        asientos_planos = [asiento for fila in asientos for asiento in fila]

        # Une todo con comas
        asientos_txt = ",".join(asientos_planos)

        archivo.write(f"{avion};{asientos_txt}\n")

    with open("data/vuelos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
        f"\n{idVuelo};{tipoVuelo};{origen};{destino};{dia};{mes};2026;{horario};{avion}"
        )

        
    # MOSTRAR RESUMEN

    print("\n-------- RESUMEN --------\n")
    print("NUMERO DE VUELO:", idVuelo)
    print("ORIGEN:", origen)
    print("DESTINO:", destino )
    print("FECHA:", dia,"/", mes,"/",2026)
    print("HORARIO:", horario)
    print("AVION ASIGNADO:", avion)
    print("\n--------------------------\n")

    print("¡El vuelo se guardo exitosamente!")


#Funcion para eliminar un vuelo

def eliminarVuelo():
   
    # Cargar vuelos en lista
    vuelos = leer_archivo("data/vuelos.txt")


    # Buscar y eliminar
    while True:
        nroVuelo = str(validar_nroVuelo())
        encontrado = False

        for v in vuelos:
            if v[0] == nroVuelo:
                print("Vuelo encontrado:")
                print("Origen:", v[1])
                print("Destino:", v[2])

                confirmacion = input("¿Eliminar vuelo? (s/n): ").lower()

                if confirmacion != "s":
                    print("Operación cancelada.")
                    return

                vuelos.remove(v)
                encontrado = True
                print("Vuelo eliminado correctamente.")
                break

        if encontrado:
            break
        else:
            print("No existe ese vuelo.")
            return

   # Reescribir archivo TXT
    with open("data/vuelos.txt", "w", encoding="utf-8") as archivo:
        for v in vuelos:
            archivo.write(";".join(map(str, v)) + "\n")

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