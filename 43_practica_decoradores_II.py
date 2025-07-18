# Función decoradora
def decorador(funcion):
    def funcion_decorada(*args, **kwargs):
        print("🔷 Vamos a hacer un cálculo...")
        funcion(*args, **kwargs)  # Se ejecuta la función decorada
        print("✅ Cálculo finalizado.\n")
    return funcion_decorada

# Función suma decorada
@decorador
def suma(num1, num2):
    resultado = num1 + num2
    print(f"Resultado de la suma: {resultado}")

# Función resta decorada
@decorador
def resta(num1, num2):
    resultado = num1 - num2
    print(f"Resultado de la resta: {resultado}")

# Ejecutamos ambas funciones
suma(7, 5)
resta(12, 10)
