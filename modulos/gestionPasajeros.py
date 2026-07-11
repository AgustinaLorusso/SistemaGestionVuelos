import hashlib
import re
import time # se agrega el bloqueo por intentos

# --- HELPERS DE SEGURIDAD ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validar_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

def cargar_pasajeros():
    pasajeros = []

    with open("data/pasajeros.txt", "r") as archivo:
        for linea in archivo:
            pasajeros.append(linea.strip().split(";"))

    return pasajeros


def guardar_pasajeros(pasajeros):
    with open("data/pasajeros.txt", "w") as archivo:
        for p in pasajeros:
            archivo.write(";".join(map(str, p)) + "\n")
            
def cargar_reservas():
    reservas = []

    with open("data/reservas.txt", "r") as archivo:
        for linea in archivo:
            reservas.append(linea.strip().split(";"))

    return reservas

def validar_datos():
    """Valida los datos ingresados por el usuario antes de registrar un pasajero."""

    pasajeros = cargar_pasajeros()

    # CONJUNTOS PARA DETECTAR REPETIDOS

    usuarios_registrados = {p[0].lower() for p in pasajeros}
    dnis_registrados = {p[2] for p in pasajeros}
    emails_registrados = {p[3].lower() for p in pasajeros}
    
    # VALIDAR USUARIO
    while True:
        usuario = input("Ingrese nombre de usuario: ").strip().lower()

        if len(usuario) < 4:
            print("Error: el usuario debe tener al menos 4 caracteres.")
            continue

        if " " in usuario:
            print("Error: el usuario no puede contener espacios.")
            continue

        if usuario in usuarios_registrados:
            print("Error: ese nombre de usuario ya existe.")
            continue

        break
    
    # VALIDAR NOMBRE
    while True:
        nombre = input("Ingrese nombre y apellido: ").strip()
        partes = nombre.split()

        if len(partes) < 2:
            print("Error: debe ingresar nombre y apellido.")
            continue

        if not all(p.isalpha() for p in partes):
            print("Error: solo se permiten letras.")
            continue

        if any(len(p) < 2 for p in partes):
            print("Error: cada parte debe tener al menos 2 letras.")
            continue

        break

    # VALIDAR DNI
    while True:
        dni = input("Ingrese su DNI (todo junto y sin puntos): ").strip()

        if not dni.isdigit(): #asegura que solo hayy 9 a números    
            print("Error: el DNI debe contener SOLO números, sin puntos ni espacios.")
            continue

        if len(dni) not in [6, 7, 8]:
            print("Error: el DNI debe tener entre 6 y 8dígitos.")
            continue
    
        if dni in dnis_registrados:
            print("Error: ese DNI ya está registrado.")
            continue

        break

    # VALIDAR EMAIL
    while True:
        email = input("Ingrese email (debe ser gmail, hotmail o yahoo y terminar con .com o .com.ar): ").strip().lower()

        if email == "" or " " in email or email.count("@") != 1:
            print("Error: email inválido.")
            continue

        parte1, parte2 = email.split("@")

        if parte1 == "" or parte2 == "" or "." not in parte2:
            print("Error: email inválido.")
            continue

        # VALIDAR PROVEEDOR
        if not (parte2.startswith("gmail") or parte2.startswith("hotmail") or parte2.startswith("yahoo")):
            print("Error: solo se permiten emails de gmail, hotmail o yahoo.")
            continue

        # VALIDAR TERMINACIÓN
        if not (parte2.endswith(".com") or parte2.endswith(".com.ar")):
            print("Error: el email debe terminar en .com o .com.ar")
            continue

        if email in emails_registrados:
            print("Error: ese email ya existe.")
            continue

        break

    # VALIDAR CONTRASEÑA
    while True:
        contraseña = input("Ingrese contraseña (mínimo 8 caracteres, mayúscula, minúscula y número): ")

        if validar_password(contraseña):
            break

        print("Contraseña débil.")

    # CREAR CAMPO MILLAS
    millas = 0

    return [usuario,nombre, dni, email, hash_password(contraseña), millas]


def registrar_pasajero():
    print("\n--- REGISTRO DE PASAJERO ---")

    pasajeros = cargar_pasajeros()

    pasajero = validar_datos()
    pasajeros.append(pasajero)

    guardar_pasajeros(pasajeros)

    print("Pasajero registrado correctamente.\n")


def buscar_reserva_por_numero(pasajero):
    """Busca una reserva a partir de su número de reserva."""
    
    reservas = cargar_reservas()
    
    while True:
        entrada = input("\nIngrese el número de reserva que desea buscar: ").strip()
        
        if entrada == "":
            print("No podés dejar el campo vacío.")
            continue
        
        if not entrada.isdigit():
            print("Tenés que ingresar un número válido.")
            continue
        
        numero_reserva = int(entrada)
        break

    for reserva in reservas:
        if int(reserva[0]) == numero_reserva:
            if reserva[3] != pasajero[2]:
                print("Esa reserva no te pertenece, solo podés visualizar reservas propias.\n")
                return
            else:
                print("\n--- INFORMACIÓN ---")
                print("Reserva Nº:", reserva[0])
                print("Vuelo:", reserva[1])
                print("Pasajero:", reserva[2])
                print("DNI:", reserva[3])
                print("Fila:", reserva[4], "Columna:", reserva[5])
                print("Día/Mes:", reserva[6], "/", reserva[7])
                print("Equipaje:", reserva[8])
                print("Avión:", reserva[9])
                print("------------------------\n")
                input("Presione enter para continuar...")
                return
    
    print("No se encontró ninguna reserva con ese número.\n")
    
def buscar_pasajero_por_dni(dni):
    pasajeros = cargar_pasajeros()

    for pasajero in pasajeros:
        if pasajero[2] == dni:
            return pasajero

    return None


def login_cliente():
    """Permite iniciar sesión con usuario o email."""

    pasajeros = cargar_pasajeros()

    intentos_fallidos = 0
    bloqueado_hasta = 0

    while True:

        if time.time() < bloqueado_hasta:
            segundos = int(bloqueado_hasta - time.time())

            print(
                f"\nDemasiados intentos fallidos."
                f"\nEspere {segundos} segundos."
            )

            time.sleep(segundos)
            continue

        identificador = input(
            "\nIngrese usuario o email: "
        ).strip().lower()

        if identificador == "":
            print("No puede dejar el campo vacío.")
            continue

        usuario_encontrado = None

        for pasajero in pasajeros:

            usuario = pasajero[0].lower()
            email = pasajero[3].lower()

            if identificador == usuario or identificador == email:
                usuario_encontrado = pasajero
                break

        if usuario_encontrado is None:

            print("Usuario o email no registrado.")

            intentos_fallidos += 1

            if intentos_fallidos >= 3:

                bloqueado_hasta = time.time() + 60
                intentos_fallidos = 0

                print(
                    "\nLogin bloqueado por 1 minuto."
                )

            opcion = input(
                "¿Desea crear una cuenta? (s/n): "
            ).lower()

            while opcion not in ["s", "n"]:
                opcion = input(
                    "¿Desea crear una cuenta? (s/n): "
                ).lower()

            if opcion == "s":
                registrar_pasajero()
                pasajeros = cargar_pasajeros()

            continue

        contraseña = input("Contraseña: ")

        if usuario_encontrado[4] == hash_password(contraseña):

            intentos_fallidos = 0

            print("Login correcto.")
            return usuario_encontrado

        else:

            print("Contraseña incorrecta.")

            intentos_fallidos += 1

            if intentos_fallidos >= 3:

                bloqueado_hasta = time.time() + 60
                intentos_fallidos = 0

                print(
                    "\nLogin bloqueado por 1 minuto."
                )