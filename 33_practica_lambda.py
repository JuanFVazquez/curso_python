'''
def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dados su base y su altura.

    Parámetros:
    - base (float): La base del triángulo.
    - altura (float): La altura del triángulo.

    Retorna:
    - float: El área del triángulo.
    """
    return (base * altura) / 2

# Ejemplo de uso
print(area_triangulo(10, 5))  # Salida: 25.0
'''

area_triangulo = lambda base, altura: (base * altura) / 2

# Ejemplo de uso
print(area_triangulo(10, 5))  # Salida: 25.0

al_cubo = lambda x: x ** 3

# Ejemplo de uso
print(al_cubo(2))  # Salida: 8

print((lambda x: x ** 3)(2))  # Salida: 8


entre_exclamaciones = lambda x: f"¡{x:.2f}€!"

print(entre_exclamaciones(42))     # Salida: ¡42.00€!
print(entre_exclamaciones(3.5))    # Salida: ¡3.50€!
