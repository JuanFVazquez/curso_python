# Mostrar el título
print("=== Programa de Solicitud de Becas ===")

# Solicitar datos al usuario (todos como enteros)
distancia_escuela = int(input("Introduce la distancia a la escuela (en kilómetros, número entero): "))
numero_hermanos = int(input("Introduce el número de hermanos en el centro: "))
salario_anual = int(input("Introduce el salario anual bruto (€): "))

# Mostrar los valores ingresados
print("\n--- Datos ingresados ---")
print(f"Distancia a la escuela: {distancia_escuela} km")
print(f"Número de hermanos en el centro: {numero_hermanos}")
print(f"Salario anual bruto: {salario_anual} €")

# Comprobar si tiene derecho a beca
if salario_anual <= 20000 or (distancia_escuela > 40 and numero_hermanos > 2):
    print("\n¡Tienes derecho a beca! 🎓")
else:
    print("\nNo tienes derecho a beca.")