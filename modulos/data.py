"""Bases de datos del programa"""
import json

# ---------
# RESERVAS 
# ---------


reservas = [
    {
        "id_reserva": 1000,
        "id_vuelo": 3491,
        "nombre": "Juan Perez",
        "dni": "12345678",
        "fila": 2,
        "columna": 3,
        "dia": 1,
        "mes": 1,
        "equipaje": "Sin equipaje",
        "avion": "av1",
        "tipo": "1"
    },
    {
        "id_reserva": 1001,
        "id_vuelo": 3495,
        "nombre": "Maria Gomez",
        "dni": "23456789",
        "fila": 5,
        "columna": 1,
        "dia": 15,
        "mes": 2,
        "equipaje": "Equipaje bodega",
        "avion": "av3",
        "tipo": "2"
    },
    {
        "id_reserva": 1002,
        "id_vuelo": 3493,
        "nombre": "Carlos Diaz",
        "dni": "34567890",
        "fila": 10,
        "columna": 4,
        "dia": 5,
        "mes": 1,
        "equipaje": "Equipaje de mano",
        "avion": "av2",
        "tipo": "1"
    },
    {
        "id_reserva": 1003,
        "id_vuelo": 3503,
        "nombre": "Ana Lopez",
        "dni": "45678901",
        "fila": 7,
        "columna": 2,
        "dia": 10,
        "mes": 2,
        "equipaje": "Equipaje bodega",
        "avion": "av4",
        "tipo": "2"
    },
    {
        "id_reserva": 1004,
        "id_vuelo": 3497,
        "nombre": "Lucia Fernandez",
        "dni": "56789012",
        "fila": 12,
        "columna": 6,
        "dia": 20,
        "mes": 2,
        "equipaje": "Sin equipaje",
        "avion": "av5",
        "tipo": "2"
    },
    {
        "id_reserva": 1005,
        "id_vuelo": 3492,
        "nombre": "Pedro Ramirez",
        "dni": "67890123",
        "fila": 3,
        "columna": 2,
        "dia": 1,
        "mes": 1,
        "equipaje": "Equipaje de mano",
        "avion": "av1",
        "tipo": "1"
    },
    {
        "id_reserva": 1006,
        "id_vuelo": 3505,
        "nombre": "Juan Perez",
        "dni": "12345678",
        "fila": 6,
        "columna": 4,
        "dia": 3,
        "mes": 2,
        "equipaje": "Sin equipaje",
        "avion": "av3",
        "tipo": "2"
    },
    {
        "id_reserva": 1007,
        "id_vuelo": 3501,
        "nombre": "Maria Gomez",
        "dni": "23456789",
        "fila": 8,
        "columna": 1,
        "dia": 25,
        "mes": 1,
        "equipaje": "Equipaje bodega",
        "avion": "av1",
        "tipo": "1"
    },
    {
        "id_reserva": 1008,
        "id_vuelo": 3498,
        "nombre": "Carlos Diaz",
        "dni": "34567890",
        "fila": 14,
        "columna": 5,
        "dia": 20,
        "mes": 2,
        "equipaje": "Equipaje de mano",
        "avion": "av5",
        "tipo": "2"
    },
    {
        "id_reserva": 1009,
        "id_vuelo": 3504,
        "nombre": "Ana Lopez",
        "dni": "45678901",
        "fila": 9,
        "columna": 3,
        "dia": 10,
        "mes": 2,
        "equipaje": "Sin equipaje",
        "avion": "av4",
        "tipo": "2"
    }

]

"""Contador de reservas funciona como un contador que genera el ID de la reserva"""

contador_reserva = [1010]

# ---------------
# ADMINISTRADORES
# ---------------

administradores =  [
    { "nombre": "Lucas Fernandez",
       "dni": 45678901,
       "email": "lucas.fernandez@gmail.com",
       "password":"lucas321"
    },
    { "nombre": "Sofia Martinez",
       "dni": 56789012,
       "email": "sofia.martinez@gmail.com",
       "password":"sofia654"
    },
    { "nombre": "Diego Alvarez",
       "dni": 67890123,
       "email": "diego.alvarez@gmail.com",
       "password":"diego987"
    }

 
]

# ------------
# PASAJEROS 
# ------------
pasajeros =  [

    { "nombre": "Juan Perez",
       "dni": 12345678,
       "email": "juan.perez@gmail.com",
       "password":"juan123", 
       "millas": 100},
    { "nombre": "Maria Gomez",
       "dni": 23456789,
       "email": "maria.gomez@gmail.com",
       "password":"maria456", 
       "millas": 300
    },
    { "nombre": "Carlos Diaz",
       "dni": 34567890,
       "email": "carlos.diaz@gmail.com",
       "password":"carlos789", 
       "millas": 600
    },
    {
        "nombre": "Ana Lopez",
       "dni": 45678901,
       "email": "ana.lopez@gmail.com",
       "password":"ana321", 
       "millas": 200
    },
    {
        "nombre": "Ana Lopez",
       "dni": 45678901,
       "email": "ana.lopez@gmail.com",
       "password":"ana321", 
       "millas": 200
    },
    {
        "nombre": "Lucia Fernandez",
       "dni": 56789012,
       "email": "lucia.fernandez@gmail.com",
       "password":"lucia654", 
       "millas": 0
    },
    {
        "nombre": "Pedro Ramirez",
       "dni": 67890123,
       "email": "pedro.ramirez@gmail.com",
       "password":"pedro987", 
       "millas": 100
    }
]

# -----------
# DESTINOS
# -----------
destinos = ("BUENOS AIRES, ARGENTINA" ,"SANTA CRUZ, ARGENTINA", "MENDOZA, ARGENTINA", "MADRID, ESPAÑA","PEKÍN, CHINA", "ROMA, ITALIA","LYON, FRANCIA", "CARACAS, VENEZUELA","BOGOTA, COLOMBIA")


#-------
#Vuelos
#-------
#Estructura => Vuelo = [nroVuelo, origen, destino, dia, mes, horario, Avion]

vuelos = [

    {
        "codigo": 1001,
        "tipo": "internacional",
        "origen": "MADRID, ESPAÑA",
        "destino": "PEKÍN, CHINA",
        "fecha": {
            "dia": 1,
            "mes": 6,
            "anio": 2026
        },
        "horario": "8:30",
        "avion": "av4"
    },

    {
        "codigo": 1002,
        "tipo": "internacional",
        "origen": "PEKÍN, CHINA",
        "destino": "MADRID, ESPAÑA",
        "fecha": {
            "dia": 1,
            "mes": 6,
            "anio": 2026
        },
        "horario": "16:30",
        "avion": "av5"
    },

    {
        "codigo": 1003,
        "tipo": "internacional",
        "origen": "ROMA, ITALIA",
        "destino": "LYON, FRANCIA",
        "fecha": {
            "dia": 2,
            "mes": 6,
            "anio": 2026
        },
        "horario": "12:30",
        "avion": "av6"
    },

    {
        "codigo": 1004,
        "tipo": "internacional",
        "origen": "LYON, FRANCIA",
        "destino": "ROMA, ITALIA",
        "fecha": {
            "dia": 2,
            "mes": 6,
            "anio": 2026
        },
        "horario": "20:30",
        "avion": "av7"
    },

    {
        "codigo": 1005,
        "tipo": "nacional",
        "origen": "MENDOZA, ARGENTINA",
        "destino": "SANTA CRUZ, ARGENTINA",
        "fecha": {
            "dia": 3,
            "mes": 6,
            "anio": 2026
        },
        "horario": "8:30",
        "avion": "av1"
    },

    {
        "codigo": 1006,
        "tipo": "nacional",
        "origen": "SANTA CRUZ, ARGENTINA",
        "destino": "MENDOZA, ARGENTINA",
        "fecha": {
            "dia": 3,
            "mes": 6,
            "anio": 2026
        },
        "horario": "12:30",
        "avion": "av2"
    },

    {
        "codigo": 1007,
        "tipo": "internacional",
        "origen": "CARACAS, VENEZUELA",
        "destino": "BOGOTA, COLOMBIA",
        "fecha": {
            "dia": 4,
            "mes": 6,
            "anio": 2026
        },
        "horario": "8:30",
        "avion": "av8"
    },

    {
        "codigo": 1008,
        "tipo": "internacional",
        "origen": "BOGOTA, COLOMBIA",
        "destino": "CARACAS, VENEZUELA",
        "fecha": {
            "dia": 4,
            "mes": 6,
            "anio": 2026
        },
        "horario": "16:30",
        "avion": "av9"
    },

    {
        "codigo": 1009,
        "tipo": "internacional",
        "origen": "MADRID, ESPAÑA",
        "destino": "ROMA, ITALIA",
        "fecha": {
            "dia": 5,
            "mes": 6,
            "anio": 2026
        },
        "horario": "12:30",
        "avion": "av10"
    },

    {
        "codigo": 1010,
        "tipo": "internacional",
        "origen": "ROMA, ITALIA",
        "destino": "MADRID, ESPAÑA",
        "fecha": {
            "dia": 5,
            "mes": 6,
            "anio": 2026
        },
        "horario": "20:30",
        "avion": "av4"
    },

    {
        "codigo": 1011,
        "tipo": "internacional",
        "origen": "LYON, FRANCIA",
        "destino": "PEKÍN, CHINA",
        "fecha": {
            "dia": 6,
            "mes": 6,
            "anio": 2026
        },
        "horario": "8:30",
        "avion": "av5"
    },

    {
        "codigo": 1012,
        "tipo": "internacional",
        "origen": "PEKÍN, CHINA",
        "destino": "LYON, FRANCIA",
        "fecha": {
            "dia": 6,
            "mes": 6,
            "anio": 2026
        },
        "horario": "16:30",
        "avion": "av6"
    },

    {
        "codigo": 1013,
        "tipo": "nacional",
        "origen": "BUENOS AIRES, ARGENTINA",
        "destino": "MENDOZA, ARGENTINA",
        "fecha": {
            "dia": 8,
            "mes": 6,
            "anio": 2026
        },
        "horario": "20:30",
        "avion": "av3"
    },

    {
        "codigo": 1014,
        "tipo": "nacional",
        "origen": "MENDOZA, ARGENTINA",
        "destino": "BUENOS AIRES, ARGENTINA",
        "fecha": {
            "dia": 8,
            "mes": 6,
            "anio": 2026
        },
        "horario": "23:30",
        "avion": "av2"
    },

    {
        "codigo": 1015,
        "tipo": "internacional",
        "origen": "BOGOTA, COLOMBIA",
        "destino": "MADRID, ESPAÑA",
        "fecha": {
            "dia": 9,
            "mes": 6,
            "anio": 2026
        },
        "horario": "12:30",
        "avion": "av7"
    }

]

aviones = [

    {
        "nroAvion": "av1",
        "tipoUso": "nacional",
        "cantAsientos": 120
    },

    {
        "nroAvion": "av2",
        "tipoUso": "nacional",
        "cantAsientos": 140
    },

    {
        "nroAvion": "av3",
        "tipoUso": "nacional",
        "cantAsientos": 160
    },

    {
        "nroAvion": "av4",
        "tipoUso": "internacional",
        "cantAsientos": 240
    },

    {
        "nroAvion": "av5",
        "tipoUso": "internacional",
        "cantAsientos": 260
    },

    {
        "nroAvion": "av6",
        "tipoUso": "internacional",
        "cantAsientos": 280
    },

    {
        "nroAvion": "av7",
        "tipoUso": "internacional",
        "cantAsientos": 300
    },

    {
        "nroAvion": "av8",
        "tipoUso": "internacional",
        "cantAsientos": 320
    },

    {
        "nroAvion": "av9",
        "tipoUso": "internacional",
        "cantAsientos": 340
    },

    {
        "nroAvion": "av10",
        "tipoUso": "internacional",
        "cantAsientos": 360
    }

]

#Funcion para la guardar los diccionarios en archivos json 
def  guardar_json(nombre_archivo,datos):
    with open(nombre_archivo,"w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4 )  

guardar_json("administradores.json",administradores)
