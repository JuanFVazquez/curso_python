# Lista de nombres en euskera
nombres_euskera = ["Aitor", "Maite", "Iker", "Maite"]

print("Nombres en euskera:", nombres_euskera)
print("El tercer nombre es:", nombres_euskera[2])
print("El segundo nombre desde el final es:", nombres_euskera[-2])
print("Los tres primeros nombres son:", nombres_euskera[0:3])
print("Los dos primeros nombres son:", nombres_euskera[:2])
print("El segundo nombre usando slicing:", nombres_euskera[1:2])
print("Los dos últimos nombres son:", nombres_euskera[-2:])

# Agregando un nuevo nombre
nombres_euskera.append("Jon")
print("Lista actualizada:", nombres_euskera)

# Insertando un nuevo nombre en la posición 2
nombres_euskera.insert(2, "Unai")
print("Lista con nuevo elemento en posición 2:", nombres_euskera)

# Agregando tres nombres más al final
nombres_euskera.extend(["Mikel", "Leire", "Ander"])
print("Lista con tres nombres más:", nombres_euskera)

# Mostrando el índice de "Jon"
print("El índice de 'Jon' es:", nombres_euskera.index("Jon"))

# Mostrando los índices de "Maite"
primer_maite = nombres_euskera.index("Maite")
print("El índice del primer 'Maite' es:", primer_maite)
segundo_maite = nombres_euskera.index("Maite", primer_maite + 1)
print("El índice del segundo 'Maite' es:", segundo_maite)

# Comprobando si "Iker" está en la lista
print("¿Está 'Iker' en la lista?:", "Iker" in nombres_euskera)

# Comprobando si "Izei" está en la lista
print("¿Está 'Izei' en la lista?:", "Izei" in nombres_euskera)

# Eliminando el último elemento
ultimo_elemento = nombres_euskera.pop()
print("El último elemento eliminado fue:", ultimo_elemento)
print("Lista después de eliminar el último elemento:", nombres_euskera)

# Creando una nueva lista con nombres en castellano
nombres_castellano = ["Juan", "María", "Carlos"]

# Uniendo las dos listas
lista_completa = nombres_euskera + nombres_castellano
print("Lista completa unida:", lista_completa)

# Repitiendo la lista 3 veces
print("Lista repetida 3 veces:", lista_completa * 3)
