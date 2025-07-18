# Imprimir título
print("=== Control de acceso ===")

# Pedir edad
entrada = input("Por favor, introduce tu edad: ")

# Verificar si la entrada es un número entero positivo
if not entrada.isdigit():
    print("Error: La edad debe ser un número entero positivo.")
else:
    edad = int(entrada)
    if edad < 0 or edad > 120:
        print("Error: Introduce una edad entre 0 y 120.")
    elif edad < 18:
        print("Lo siento, no puedes pasar. Eres menor de edad.")
    else:
        print("¡Puedes pasar! Bienvenido/a.")

# Imprimir título
print("=== Evaluación de nota ===")

# Pedir nota
entrada = input("Por favor, introduce la nota del alumno (0 a 10): ")

# Verificar si la entrada es un número válido
try:
    nota = float(entrada)
    if nota < 0 or nota > 10:
        print("Error: La nota debe estar entre 0 y 10.")
    elif nota < 5:
        print("Resultado: Insuficiente")
    elif nota < 6:
        print("Resultado: Suficiente")
    elif nota < 7:
        print("Resultado: Bien")
    elif nota < 9:
        print("Resultado: Notable")
    elif nota <= 10:
        print("Resultado: Sobresaliente")
except ValueError:
    print("Error: La nota debe ser un número válido.")
