"""Bases de datos del programa"""

# ---------
# RESERVAS 
# ---------
reservas = [
    [1000, 3491, "Juan Perez", "12345678", 2, 3, 1, 1, "Sin equipaje", "av1", "1"],
    [1001, 3495, "Maria Gomez", "23456789", 5, 1, 15, 2, "Equipaje bodega", "av3", "2"],
    [1002, 3493, "Carlos Diaz", "34567890", 10, 4, 5, 1, "Equipaje de mano", "av2", "1"],
    [1003, 3503, "Ana Lopez", "45678901", 7, 2, 10, 2, "Equipaje bodega", "av4", "2"],
    [1004, 3497, "Lucia Fernandez", "56789012", 12, 6, 20, 2, "Sin equipaje", "av5", "2"],
    [1005, 3492, "Pedro Ramirez", "67890123", 3, 2, 1, 1, "Equipaje de mano", "av1", "1"],
    [1006, 3505, "Juan Perez", "12345678", 6, 4, 3, 2, "Sin equipaje", "av3", "2"],
    [1007, 3501, "Maria Gomez", "23456789", 8, 1, 25, 1, "Equipaje bodega", "av1", "1"],
    [1008, 3498, "Carlos Diaz", "34567890", 14, 5, 20, 2, "Equipaje de mano", "av5", "2"],
    [1009, 3504, "Ana Lopez", "45678901", 9, 3, 10, 2, "Sin equipaje", "av4", "2"]
]

"""Contador de reservas funciona como un contador que genera el ID de la reserva"""
contador_reserva = [1010]

# ---------------
# ADMINISTRADORES
# ---------------
administradores =  [
  ["Lucas Fernandez", "45678901", "lucas.fernandez@gmail.com", "lucas321"],
  ["Sofia Martinez", "56789012", "sofia.martinez@gmail.com", "sofia654"],
  ["Diego Alvarez", "67890123", "diego.alvarez@gmail.com", "diego987"]
]

# ------------
# PASAJEROS 
# ------------
pasajeros =  [
    ["Juan Perez", "12345678", "juan.perez@gmail.com", "juan123", 100],
    ["Maria Gomez", "23456789", "maria.gomez@gmail.com", "maria456", 300],
    ["Carlos Diaz", "34567890", "carlos.diaz@gmail.com", "carlos789", 600],
    ["Ana Lopez", "45678901", "ana.lopez@gmail.com", "ana321", 200],
    ["Lucia Fernandez", "56789012", "lucia.fernandez@gmail.com", "lucia654", 0],
    ["Pedro Ramirez", "67890123", "pedro.ramirez@gmail.com", "pedro987", 100]
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