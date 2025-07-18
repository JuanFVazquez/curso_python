import re

# Lista de dominios
dominios = [
    "www.españa.com",
    "www.mundial.org",
    "www.tecnología.net",
    "www.niño.edu",
    "www.google.com",
    "www.mundoñ.com",
    "www.anonimo.net",
    "www.piñata.org"
]

# Patrón para detectar el carácter ñ o Ñ
patron = r"ñ"

# Filtramos los dominios que contienen la letra ñ (insensible a mayúsculas/minúsculas)
dominios_con_ñ = list(filter(lambda url: re.search(patron, url, re.IGNORECASE), dominios))

# Mostramos los resultados
if dominios_con_ñ:
    print("Dominios que contienen el carácter 'ñ':")
    for dominio in dominios_con_ñ:
        print("-", dominio)
else:
    print("No se encontraron dominios con el carácter 'ñ'.")
