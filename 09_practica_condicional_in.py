# Mostrar el título
print("=== Elección de Asignatura Optativa de Informática ===")

# Lista de asignaturas optativas
optativas = ["Ciberseguridad", "Inteligencia Artificial", "Desarrollo Web", "Big Data", "Realidad Virtual", "Robótica"]

# Mostrar la lista de asignaturas
print("\nAsignaturas disponibles:")
for asignatura in optativas:
    print(f"- {asignatura}")

# Pedir al alumno que escoja 1 asignatura
print("\nElige una asignatura de la lista anterior.")
opcion = input("Asignatura elegida: ").strip().lower()

# Crear una lista de optativas en minúscula para comparar
optativas_minusculas = [asig.lower() for asig in optativas]

# Comprobar si la asignatura elegida está en la lista (sin importar mayúsculas/minúsculas)
if opcion in optativas_minusculas:
    # Buscar la forma original para mostrarla bien escrita
    indice = optativas_minusculas.index(opcion)
    asignatura_correcta = optativas[indice]
    print(f"\nHas elegido correctamente: {asignatura_correcta}")
else:
    print("\nLa asignatura elegida no está en la lista. Por favor, revisa y vuelve a intentarlo.")
