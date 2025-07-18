
def obtener_pares(limite):
    pares = []
    contador = 1

    while contador <= limite:
        pares.append(contador * 2)
        contador += 1

    return pares

print(obtener_pares(5))

def generar_pares(limite):
    contador = 1
    while contador <= limite:
        yield contador * 2
        contador += 1

for numero in generar_pares(5):
    print(numero)

# Obtener solo los 3 primeros valores del generador
generador = generar_pares(10)  # aunque el límite sea mayor, solo sacaremos 3

print(next(generador))
print("Separador")
print(next(generador))
print("Separador")
print(next(generador))
