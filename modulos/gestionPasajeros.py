# lista para guardar todos los pasajeros registrados
from .data import reservas, pasajeros

def validar_datos():
    """Valida los datos ingresados por el usuario antes de registrar un pasajero."""

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

        if not dni.isdigit(): #asegura que solo haya números    
            print("Error: el DNI debe contener SOLO números, sin puntos ni espacios.")
            continue

        if len(dni) not in [7, 8, 9]:
            print("Error: el DNI debe tener entre 7 y 9 dígitos.")
            continue
    
        repetido = False
        for pasajero in pasajeros:
            if pasajero[1] == dni:
                repetido = True
                break

        if repetido:
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

        # VALIDAR REPETIDOS
        repetido = False
        for pasajero in pasajeros:
            if pasajero[2] == email:
                repetido = True
                break

        if repetido:
            print("Error: ese email ya existe.")
            continue

        break

    # VALIDAR CONTRASEÑA
    while True:
        contraseña = input("Ingrese contraseña (mínimo 6 caracteres): ")

        if len(contraseña) >= 6 and contraseña.strip() != "":
            break

        print("Error: la contraseña debe tener al menos 6 caracteres.")

    # CREAR CAMPO MILLAS
    millas = 0

    return [nombre, dni, email, contraseña, millas]


def registrar_pasajero():
    """Registra un nuevo pasajero."""
    print("\n--- REGISTRO DE PASAJERO ---")

    pasajero = validar_datos()
    pasajeros.append(pasajero)

    print("Pasajero registrado correctamente.\n")


def buscar_reserva_por_numero(pasajero):
    """Busca una reserva a partir de su número de reserva."""
    
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
        if reserva[0] == numero_reserva:
            if reserva[3] != pasajero[1]:
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
    """Busca un pasajero según su DNI."""
    for pasajero in pasajeros:
        if pasajero[1] == dni:
            return pasajero
    return None


def login_cliente():
    """Permite iniciar sesión al cliente y ofrece la opción de crear una cuenta."""
    while True:

        while True:
            email = input("\nEmail: ").strip().lower()

            if email == "" or " " in email or email.count("@") != 1:
                print("El email es inválido.")
                continue

            parte1, parte2 = email.split("@")

            if parte1 == "" or parte2 == "" or "." not in parte2:
                print("El email es inválido.")
                continue

            # VALIDAR PROVEEDOR
            if not (parte2.startswith("gmail") or parte2.startswith("hotmail") or parte2.startswith("yahoo")):
                print("Solo se permiten emails de gmail, hotmail o yahoo.")
                continue

            # VALIDAR TERMINACIÓN
            if not (parte2.endswith(".com") or parte2.endswith(".com.ar")):
                print("El email debe terminar en .com o .com.ar")
                continue

            break

        usuario_encontrado = None
        for pasajero in pasajeros:
            if pasajero[2] == email:
                usuario_encontrado = pasajero
                break

        if usuario_encontrado is None:
            print("Ese email no está registrado.")

            opcion = input("¿No tiene cuenta? Crear cuenta (s/n): ").lower()
            while opcion not in ["s", "n"]:
                print("Error: elija una opción válida.")
                opcion = input("¿No tiene cuenta? Crear cuenta (s/n): ").lower()

            if opcion == "s":
                registrar_pasajero()
            else:
                print("Intente nuevamente.")
            continue

        while True:
            contraseña = input("Contraseña: ")

            if len(contraseña) >= 6 and contraseña.strip() != "":
                break
            else:
                print("La contraseña debe contener mínimo 6 caracteres.")

        if usuario_encontrado[3] == contraseña:
            print("Login correcto.")
            return usuario_encontrado
        else:
            print("Contraseña incorrecta.")


def consulta_reserva():
    """Muestra los datos de una reserva existente a partir de su número."""

    while True:
        numero_reserva = input("Ingrese su número de reserva: ").strip()

        if numero_reserva.isdigit():
            numero_reserva = int(numero_reserva)
            break

        print("Error: debe ingresar solo números.")

    reserva = buscar_reserva_por_numero(numero_reserva)

    if reserva is None:
        print("No se encontró una reserva con ese número.")
        return
    
    if reserva[3] != pasajero[1]:
        print("Esa reserva no te pertenece.")
        return
    
    
    dni_reserva = reserva[3]
    pasajero = buscar_pasajero_por_dni(dni_reserva)

    if pasajero is None:
        print("No se encontró el pasajero asociado a la reserva.")
        return

    print("\n--- INFORMACIÓN ---")
    print("Reserva Nº:", reserva[0])
    print("Vuelo:", reserva[1])
    print("Pasajero:", reserva[2])
    print("DNI:", reserva[3])
    print("Fila:", reserva[4], "Columna:", reserva[5])
    print("Día/Mes:", reserva[6], "/", reserva[7])
    print("Equipaje:", reserva[8])
    print("Avión:", reserva[9])
    print("------------------------")