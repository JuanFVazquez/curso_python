import re

# Lista de palabras
palabras = [
    "niños",
    "niñas",
    "niño",
    "niña",
    "niñato",
    "niñosas",
    "abuelos",
    "niños",
    "madres",
    "niñas",
    "niñ@s"
]

# Patrón para encontrar "niños" o "niñas" exactamente
patron = r"\bniñ[oa]s\b"

# Filtramos la lista
coincidencias = list(filter(lambda palabra: re.fullmatch(patron, palabra, re.IGNORECASE), palabras))

# Mostramos los resultados
if coincidencias:
    print("Palabras encontradas que son 'niños' o 'niñas':")
    for palabra in coincidencias:
        print("-", palabra)
else:
    print("No se encontraron coincidencias para 'niños' o 'niñas'.")
