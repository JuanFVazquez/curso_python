# Creando una tupla mixta con números y strings
tupla_mixta = 1, "Python", 3.14, "Programación", 42

print("Tupla mixta:", tupla_mixta)
print("Primer elemento:", tupla_mixta[0])
print("Elemento string:", tupla_mixta[1])
print("Número decimal:", tupla_mixta[2])
# Convirtiendo la tupla a lista
lista_mixta = list(tupla_mixta)
print("Tupla convertida a lista:", lista_mixta)
# Creando una nueva lista con valores mixtos
nueva_lista_mixta = ["Hola", 25, "Python", True, 3.1416, "Python"]
print("Nueva lista mixta:", nueva_lista_mixta)

# Convirtiendo la lista a tupla
nueva_tupla = tuple(nueva_lista_mixta)
print("Lista convertida a tupla:", nueva_tupla)
# Comprobando si "Python" está en la tupla
print("¿Está 'Python' en la tupla?:", "Python" in nueva_tupla)
# Comprobando si "Java" está en la tupla
print("¿Está 'Java' en la tupla?:", "Java" in nueva_tupla)
# Contando las ocurrencias de "Python" en la tupla
print("Número de veces que aparece 'Python' en la tupla:", nueva_tupla.count("Python"))
# Contando el número total de elementos en la tupla
print("Número total de elementos en la tupla:", len(nueva_tupla))
# Creando una tupla unitaria (con un solo elemento)
tupla_unitaria = (42,)  # La coma es necesaria para crear una tupla unitaria
print("Tupla unitaria:", tupla_unitaria)
print("Longitud de la tupla unitaria:", len(tupla_unitaria))
# Ejemplo de desempaquetado de tupla
coordenadas = 10, 20, 30
x, y, z = coordenadas
print("\nDesempaquetado de tupla de coordenadas:")
print("x:", x)
print("y:", y) 
print("z:", z)

# Otro ejemplo con diferentes tipos de datos
persona = ("Ana", 25, "Madrid")
nombre, edad, ciudad = persona
print("\nDesempaquetado de tupla con datos personales:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
