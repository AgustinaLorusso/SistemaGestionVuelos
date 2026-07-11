
# --- PARA LEER ---
def leer_archivo(ruta):
    """Devuelve una lista de listas (cada línea es una lista de datos)."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return [linea.strip().split(";") for linea in f if linea.strip()]
    except FileNotFoundError:
        return []

# --- PARA ESCRIBIR ---
def escribir_archivo(ruta, lista_datos):
    """Recibe una lista de listas y las escribe en el archivo con punto y coma."""
    with open(ruta, "w", encoding="utf-8") as f:
        for fila in lista_datos:
            # Convertimos todo a string y unimos con ;
            linea = ";".join(map(str, fila))
            f.write(linea + "\n")