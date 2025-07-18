import math

def evaluar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuídate"
    else:
        return "Edad fuera de rango considerado"

print(evaluar_edad(18))   # Eres muy joven
print(evaluar_edad(25))   # Eres joven
print(evaluar_edad(50))   # Eres maduro
print(evaluar_edad(80))   # Cuídate
print(evaluar_edad(105))  # Edad fuera de rango considerado



def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(numero)

# Solicitar al usuario un número entero
try:
    valor = int(input("Introduce un número entero: "))
    resultado = raiz_cuadrada(valor)
    print(f"La raíz cuadrada de {valor} es {resultado}")
except ValueError as e:
    print("Error:", e)
