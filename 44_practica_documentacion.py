from modulos import funciones_matematicas
class Area:
    '''Esta clase calcula las áreas de diferentes figuras geométricas'''
    def area_cuadrado(lado):
        """
        Calcula el área de un cuadrado.

        Parámetros:
        - lado (float): longitud del lado del cuadrado.

        Retorna:
        - float: área del cuadrado.
        """
        return lado * lado

    def area_triangulo(base, altura):
        """
        Calcula el área de un triángulo.

        Parámetros:
        - base (float): longitud de la base del triángulo.
        - altura (float): altura del triángulo.

        Retorna:
        - float: área del triángulo.
        """
        return (base * altura) / 2

# Mostrar los docstrings
print("📝 Documentación de la función area_cuadrado:")
print(Area.area_cuadrado.__doc__)

print("\n📝 Documentación de la función area_triangulo:")
print(Area.area_triangulo.__doc__)

# Ejemplos de uso
print(f"\nÁrea del cuadrado (lado = 4): {Area.area_cuadrado(4)}")
print(f"Área del triángulo (base = 6, altura = 3): {Area.area_triangulo(6, 3)}")

help(Area)
help(funciones_matematicas)

