import re

# Lista de nombres
nombres = [
    "Antonio",
    "Beatriz",
    "Cristina",
    "Luis",
    "Marcos",
    "Patricia",
    "Raúl",
    "Sofía",
    "Ulises",
    "Tomás",
    "Óscar",
    "Lucía"
]

# Expresión regular: cualquier letra entre O y T (mayúscula o minúscula)
patron = r"[o-tO-T]"

# Filtramos los nombres que contienen al menos una letra entre O y T
coincidencias = list(filter(lambda nombre: re.search(patron, nombre), nombres))

# Mostramos el resultado
if coincidencias:
    print("Nombres que contienen al menos una letra entre 'O' y 'T':")
    for nombre in coincidencias:
        print("-", nombre)
else:
    print("No se encontraron nombres con letras entre 'O' y 'T'.")
