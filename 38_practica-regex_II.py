import re

# Lista de personas con nombre y apellido
personas = [
    "Ana García",
    "Antonio López",
    "Alberto Ruiz",
    "Beatriz Martínez",
    "Ana Torres",
    "Carlos Pérez",
    "Anabel Gómez",
    "Lucía García",
    "Pedro Martínez"
]

# ----- BÚSQUEDA POR NOMBRE -----
nombre_buscado = input("Introduce el nombre exacto que quieres buscar: ")

# Patrón: nombre al inicio
patron_nombre = rf"^{re.escape(nombre_buscado)}\b"
coincidencias_nombre = list(filter(lambda persona: re.match(patron_nombre, persona, re.IGNORECASE), personas))

if coincidencias_nombre:
    print(f"\nPersonas cuyo nombre exacto es '{nombre_buscado}':")
    for persona in coincidencias_nombre:
        print("-", persona)
else:
    print(f"\nNo se han encontrado personas con el nombre exacto '{nombre_buscado}'.")

# ----- BÚSQUEDA POR APELLIDO -----
apellido_buscado = input("\nIntroduce el apellido exacto con el que debe terminar el nombre completo: ")

# Patrón: apellido al final
patron_apellido = rf"\b{re.escape(apellido_buscado)}$"
coincidencias_apellido = list(filter(lambda persona: re.search(patron_apellido, persona, re.IGNORECASE), personas))

if coincidencias_apellido:
    print(f"\nPersonas cuyo apellido es '{apellido_buscado}':")
    for persona in coincidencias_apellido:
        print("-", persona)
else:
    print(f"\nNo se han encontrado personas con el apellido exacto '{apellido_buscado}'.")
