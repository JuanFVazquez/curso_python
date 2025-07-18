def obtener_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

# Ejemplo de uso:
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = obtener_pares(lista_original)

print("Lista original:", lista_original)
print("Números pares:", lista_pares)
