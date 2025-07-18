nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre.upper()}!")

print(f"Hola, {nombre.lower()}!")

print(f"Hola, {nombre.capitalize()}!")


edad = input("Introduce tu edad: ")

while True:
    edad = input("Introduce tu edad: ")
    if edad.isdigit():
        edad = int(edad)
        break
    else:
        print("Error: la edad debe ser un número válido. Inténtalo de nuevo.")

if edad >= 18:
    print("Adelante")
else:
    print("Prohibido el paso")


