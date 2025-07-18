# Creando un diccionario de países y sus capitales
paises_capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Reino Unido": "Londres",
    "Portugal": "Lisboa",
    "Países Bajos": "Ámsterdam",
    "Bélgica": "Bruselas"
}

print("Diccionario de países y capitales:", paises_capitales)
print("La capital de Francia es:", paises_capitales["Francia"])
print("La capital de España es:", paises_capitales["España"])
paises_capitales["Grecia"] = "Budapest"
print("La capital de Grecia es:", paises_capitales["Grecia"])
# Corrigiendo el error: la capital de Grecia es Atenas, no Budapest
paises_capitales["Grecia"] = "Atenas"
print("La capital corregida de Grecia es:", paises_capitales["Grecia"])
# Eliminando Países Bajos del diccionario
del paises_capitales["Países Bajos"]
print("Diccionario después de eliminar Países Bajos:", paises_capitales)
# Creando un diccionario con claves mixtas (numéricas y alfanuméricas)
diccionario_mixto = {
    1: "Valor numérico",
    "clave2": 200,
    3.14: "Pi",
    "ABC123": True
}

print("\nDiccionario con claves mixtas:", diccionario_mixto)
print("Valor de la clave 1:", diccionario_mixto[1])
print("Valor de la clave 'clave2':", diccionario_mixto["clave2"])
print("Valor de la clave 3.14:", diccionario_mixto[3.14])
print("Valor de la clave 'ABC123':", diccionario_mixto["ABC123"])
# Creando una tupla de países
paises = ("México", "Brasil", "Argentina", "Colombia")
print("\nTupla de países:", paises)
print("Número de países en la tupla:", len(paises))
# Creando un diccionario usando la tupla de países como claves
paises_latinoamerica = {
    paises[0]: "Ciudad de México",
    paises[1]: "Brasilia", 
    paises[2]: "Buenos Aires",
    paises[3]: "Bogotá"
}

print("\nDiccionario de países latinoamericanos:", paises_latinoamerica)
print("La capital de México es:", paises_latinoamerica[paises[0]])
print("La capital de Brasil es:", paises_latinoamerica["Brasil"])
# Creando un diccionario con conceptos matemáticos
conceptos_matematicos = {
    "pi": 3.14159,
    "coordenadas_origen": (0, 0),  # Usando una tupla como valor
    "operaciones_basicas": ["suma", "resta", "multiplicación", "división"],
    "teorema_pitagoras": "a² + b² = c²",
    "numeros_primos": (2, 3, 5, 7, 11, 13)  # Otra tupla como valor
}

print("\nDiccionario de conceptos matemáticos:", conceptos_matematicos)
print("Valor de pi:", conceptos_matematicos["pi"])
print("Coordenadas del origen:", conceptos_matematicos["coordenadas_origen"])
print("Primer número primo:", conceptos_matematicos["numeros_primos"][0])
print("Teorema de Pitágoras:", conceptos_matematicos["teorema_pitagoras"])
# Creando una copia del diccionario con operaciones_basicas como diccionario anidado
conceptos_matematicos_v2 = {
    "pi": 3.14159,
    "coordenadas_origen": (0, 0),
    "operaciones_basicas": {"operaciones": ["suma", "resta", "multiplicación", "división"]},
    "teorema_pitagoras": "a² + b² = c²", 
    "numeros_primos": (2, 3, 5, 7, 11, 13)
}

print("\nNuevo diccionario de conceptos matemáticos:", conceptos_matematicos_v2)
print("Lista de operaciones básicas:", conceptos_matematicos_v2["operaciones_basicas"]["operaciones"])
# Obteniendo las claves del diccionario
print("\nClaves del diccionario conceptos_matematicos_v2:", conceptos_matematicos_v2.keys())

# Obteniendo el valor de la longitud del diccionario
print("\Longitud del diccionario conceptos_matematicos_v2:", len(conceptos_matematicos_v2))
