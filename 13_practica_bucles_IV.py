import math

edad = int(input("Introduce la edad, por favor: "))

while edad<5 or edad>100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad = int(input("Introduce la edad, por favor: "))

print("Edad del aspirante", edad, "años")
print("Gracias")


print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce un número, por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break

    numero = int(input("Introduce un número, por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))    
