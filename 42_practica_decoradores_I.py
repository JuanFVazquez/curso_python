# Función decoradora
def decorador(funcion):
    def funcion_decorada():
        print("🔷 Vamos a hacer un cálculo...")
        funcion()  # Se ejecuta la función decorada
        print("✅ Cálculo finalizado.\n")
    return funcion_decorada

# Función suma decorada
@decorador
def suma():
    resultado = 10 + 5
    print(f"Resultado de la suma: {resultado}")

# Función resta decorada
@decorador
def resta():
    resultado = 10 - 5
    print(f"Resultado de la resta: {resultado}")

# Ejecutamos ambas funciones
suma()
resta()
