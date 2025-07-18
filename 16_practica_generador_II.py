def devuelve_ciudades(*ciudades):  # aquí acepta múltiples argumentos sueltos
    for ciudad in ciudades:
        yield ciudad



for ciudad in devuelve_ciudades("Madrid", "Barcelona", "Valencia"):
    print(ciudad)

print("")

generador = devuelve_ciudades("Madrid", "Barcelona", "Valencia", "Sevilla")

print(next(generador))
print(next(generador))

def devuelve_letras(*ciudades):
    for ciudad in ciudades:             # Recorre todas las ciudades
        #for letra in ciudad:        # Toma solo las dos primeras letras de cada ciudad
            #yield letra
        yield from ciudad


print("")

generador = devuelve_letras("Madrid", "Barcelona", "Valencia", "Sevilla")

print(next(generador))
print(next(generador))