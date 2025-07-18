# Crear (o abrir) y escribir dos líneas en el archivo datos.txt
with open("datos.txt", "w") as archivo:
    archivo.write("Esta es la primera línea del archivo.\n")
    archivo.write("Y esta es la segunda línea.\n")

print("Archivo 'datos.txt' creado y escrito correctamente.")

# Abrir el archivo en modo lectura y mostrar su contenido
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido de 'datos.txt':")
    print(contenido)

# Abrir el archivo en modo añadir y escribir más líneas
with open("datos.txt", "a") as archivo:
    archivo.write("Tercera línea añadida al final.\n")
    archivo.write("Cuarta línea también.\n")

print("Líneas añadidas a 'datos.txt' sin borrar su contenido.")


# Abrir el archivo en modo lectura y mostrar el contenido usando readlines()
with open("datos.txt", "r+") as archivo:
    archivo.write("Comienzo del texto")
    lineas = archivo.readlines()
    archivo.seek(0)
    archivo.seek(len(archivo.read())/2)
    print("Archivo: ", archivo.read(30))
    print("Segunda lectura: ", archivo.read())
    archivo.seek(len(archivo.readline()))
    print("Readline:", archivo.read())
    lineas[1] = "Esta línea ha sido incluida desde el exterior\n"
    archivo.seek(0)
    archivo.writelines(lineas)

print("Contenido de 'datos.txt en lista':")
for linea in lineas:
    print("* ", linea, end="")  # Para evitar el doble salto de línea
