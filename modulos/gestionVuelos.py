#IMPORTACIONES
from .data import destinos ,vuelos, aviones
from .validaciones import validaciones, modificiar_archivo, cargar_json
import calendar , random , json
from functools import reduce



#HORARIOS POSBILES PARA GENERAR VUELOS
horarios = [ "8.30 AM" , "12.30 AM", "20.30 PM", "23.30 PM"]

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

        if nroVuelo < 1000 or nroVuelo> 9999:
            print("El número de vuelo debe tener 4 dígitos")
            continue

        return(nroVuelo)

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
            print(f"{count}. {lista[i]}\n")
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
            
def aviones_por_destino(tipoVuelo):
    
    """Funcion que asigna los aviones posibles de uso segun su tipo de vuelo"""

    #AVIONES SEPARADOS POR TIPO DE VUELO (NACIONALES - INTERNACIONALES)

    avionesPosibles = []

    for i in range(len(aviones)):

       if aviones[i]["tipoUso"] == tipoVuelo:

            avionesPosibles.append(aviones[i])
    
    return avionesPosibles

def asignacion_avion(tipoVuelo, dia, mes, horario):

    "Funcion que asigna el avion segun disponibilidad y teniendo en cuenta el destino "

   #Listas de aviones para ese destino
    aviones_posibles = aviones_por_destino(tipoVuelo)
    
    #Verifica cual de los aviones de la lista no esta en uso en las condiciones que puso el administrador.
    for avion in aviones_posibles:
        
        ocupado = False

        #Accedemos a los datos del vuelo por clave.
        
        for vuelo in vuelos:

            if (
                vuelo["avion"] == avion and
                vuelo["fecha"]["dia"] == dia and
                vuelo["fecha"]["mes"] == mes and
                vuelo["horario"] == horario):
                
                ocupado = True
        
        if not ocupado:
            return avion
    
    return None

#Implementacion de reduce
def contar_vuelos_por_mes():

    """ Funcion encargada de contar los vuelos"""
    while True:
        # ---- MES ----
        entrada = input("\nIngrese el mes (1-12): ").strip()

        if not entrada or not entrada.isdigit():
            print("Debe ingresar un número.")
            continue

        mes = int(entrada)

        if mes < 1 or mes > 12:
            print("Mes inválido.")
            continue

        break
    vuelos_del_mes = list(filter(lambda vuelo: vuelo[4] == mes, vuelos))
    
    total = reduce(lambda acumulado, vuelo: acumulado + 1, vuelos_del_mes, 0)
    
    print("\n"
        f"Vuelos programados en el mes {mes}: {total}\n")

#Funciones para ADMINISTRADOR 

#Funcion para crear vuelos.

def crearVuelo():

    """Funcion que le permite al administrador crear vuelos y guardarlos en la base de datos (vuelos) """
    
    while True: 

        presentacion_programacion_vuelos()

        origen,destino= seleccion_OrigenDestino()

        tipoVuelo = tipo_vuelo(origen,destino)

        mes,dia = Asignacion_FechaVuelo()

        horario = seleccion_horario()

        avion = asignacion_avion(tipoVuelo, dia, mes, horario)

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
    
    vuelo = {
            "origen": origen,
            "destino": destino,

            "fecha": {
                "dia": dia,
                "mes": mes,
                "anio": 2026
            },
            "avion": avion
    }

    cargar_json("vuelos.json",idVuelo,vuelo)

   
        
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


#Funcion para modificar un vuelo 
def modificarVuelo():

    """Funcion que permite al administrador modificar Fecha/Hora de un vuelo """
    idVuelo= validar_nroVuelo()
    with open ("vuelos.json","r",encoding="utf-8") as archivo:
        vuelos = json.load(archivo)
    while idVuelo not in vuelos:
        print("El vuelo ingresado no existe")
    vuelo = vuelos[idVuelo]
    opciones=[1,2] #opciones de ingreso del usuario

    print("Ingrese el numero correspondiente al dato a modificar:\n" f"1. Fecha\n" f"2. Hora\n")
    
    datoAmodificar= validaciones(opciones)

    while datoAmodificar is False:
        print("Ingrese el numero correspondiente al dato a modificar:\n" f"1. Fecha\n" f"2. Hora\n")
        datoAmodificar= validaciones(opciones)

    if datoAmodificar==1:
        #Invocamos funcion para pedir nueva fecha en que se quiere generar el vuelo.
        mes,dia=Asignacion_FechaVuelo()  

        vuelo["fecha"]["mes"]= mes
        vuelo["fecha"]["dia"] = dia

        print("NUMERO DE VUELO:", idVuelo)
        print("\n--- RESUMEN DE VUELO MODIFICADO ---\n")
        print("ORIGEN:", origen)
        print("DESTINO:", destino )
        print("FECHA:", dia,"/", mes,"/",2026)
        

        print("Dia del vuelo se ha modificado con exito")

    else: #CASO DE QUERER MODIFICAR EL HORARIO
        tipoVuelo= tipo_vuelo(origen,vuelo)
        horario=seleccion_horario(tipoVuelo)
        dia= vuelo[-4]
        mes=vuelo[-3]
        #VALIDAR EL AVION QUE ESTE DISPONIBLE A ESE HORARIO 
        avion = asignacion_avion(origen, destino, dia, mes, horario)

        if  avion == None:
            print("Vuelo no pudo ser modificado")
            print("Todos los aviones estan en uso para las condiciones ingresadas.")
        else:
            vuelo[5]= horario
            vuelo[6]= avion

            print("\n--- RESUMEN DE VUELO MODIFICADO ---\n")
            print("NUMERO DE VUELO:", idVuelo)
            print("ORIGEN:", origen)
            print("DESTINO:", destino )
            print("FECHA:", dia,"/", mes,"/",2026)
            print("HORARIO", horario)
           

            print("Horario del vuelo se modifico con exito")

#Funcion para eliminar un vuelo

def eliminarVuelo():
    while True:
        nroVuelo = validar_nroVuelo()
        encontrado = False

        for v in vuelos:
            if v[0] == nroVuelo:
                vuelos.remove(v)
                print("Vuelo eliminado correctamente.")
                encontrado = True
                break
        
        if encontrado:
            break
        else:
            print("No existe ese vuelo.")
            return