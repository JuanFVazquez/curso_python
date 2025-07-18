import re

# Texto base donde se realizará la búsqueda
texto = (
    "En un pequeño pueblo rodeado de montañas, vivía una comunidad tranquila y trabajadora. "
    "Cada mañana, los vecinos se reunían en la plaza para compartir historias, tomar café y planificar el día. "
    "La escuela del pueblo estaba al lado de la biblioteca, y los niños solían pasar allí las tardes leyendo cuentos de aventuras."
)

# Solicita al usuario la cadena que desea buscar
cadena_buscar = input("Introduce la cadena que quieres buscar en el texto: ")

# Realiza la búsqueda principal (primera aparición)
coincidencia = re.search(re.escape(cadena_buscar), texto, re.IGNORECASE)

# Encuentra todas las coincidencias para contar cuántas veces aparece
todas_las_coincidencias = re.findall(re.escape(cadena_buscar), texto, re.IGNORECASE)
numero_apariciones = len(todas_las_coincidencias)

if coincidencia:
    inicio, fin = coincidencia.span()
    print(f"\nSe ha encontrado el texto buscado desde la posición {inicio} hasta la {fin - 1}.")
    print(f"Tupla de posiciones: ({inicio}, {fin - 1})")
    print(f"Número de veces que aparece en el texto: {numero_apariciones}")
    posiciones = (inicio, fin - 1)
else:
    print("\nNo se ha encontrado el texto buscado.")
    posiciones = None
