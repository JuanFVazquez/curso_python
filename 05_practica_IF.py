def evaluacion(nota):
    if nota >= 5:
        return "Aprobado"
    else:
        return "Suspendido"

# Título del programa
print("=== Evaluación del Alumno ===")

# Pedir nota al usuario
try:
    nota_usuario = float(input("Introduce la nota del alumno (de 0 a 10): "))
    if 0 <= nota_usuario <= 10:
        resultado = evaluacion(nota_usuario)
        print(f"Resultado: {resultado}")
    else:
        print("Error: La nota debe estar entre 0 y 10.")
except ValueError:
    print("Error: Por favor, introduce un número válido.")

