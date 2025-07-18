import math

def raiz_cuadrada(lista_numeros):
    """
    Devuelve una lista con la raíz cuadrada de los números en la lista original.
    Solo procesa números no negativos (para evitar errores con raíces de negativos).

    Ejemplo:
    >>> lista = []
    >>> for num in [1, 4, 9]:
    ...     lista.append(num)
    >>> raiz_cuadrada(lista)
    [1.0, 2.0, 3.0]
    """
    return [math.sqrt(num) for num in lista_numeros if num >= 0]

# Si quieres que se ejecute el doctest automáticamente al lanzar el script:
if __name__ == "__main__":
    import doctest
    doctest.testmod()
