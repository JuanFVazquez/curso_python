def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo y devuelve un mensaje con el resultado.

    Parámetros:
    - base (float): longitud de la base del triángulo.
    - altura (float): altura del triángulo.

    Retorna:
    - str: mensaje con el área del triángulo.

    Ejemplos:
    >>> area_triangulo(6, 4)
    'El área del triángulo es: 12.0'

    >>> area_triangulo(10, 5)
    'El área del triángulo es: 25.0'

    >>> area_triangulo(0, 7)
    'El área del triángulo es: 0.0'
    """
    area = (base * altura) / 2
    return f"El área del triángulo es: {area}"

# Ejecutar test y mostrar un ejemplo
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Prueba visual
    print(area_triangulo(6, 4))
