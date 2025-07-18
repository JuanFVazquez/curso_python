class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Empleado: {self.nombre}, Cargo: {self.cargo}, Salario: {self.salario}€"

# Ejemplo de uso:
# Crear una lista de empleados
empleados = [
    Empleado("Laura", "Desarrolladora", 30000),
    Empleado("Carlos", "Analista", 28000),
    Empleado("María", "Diseñadora UX", 27000),
    Empleado("Jorge", "Administrador de sistemas", 32000),
    Empleado("Ana", "Product Manager", 35000)
]

# Mostrar los empleados
for empleado in empleados:
    print(empleado)

# Filtrar empleados con salario >= 30000 usando filter
empleados_bien_pagados = list(filter(lambda e: e.salario >= 30000, empleados))

# Mostrar los empleados seleccionados
print("Empleados con salario igual o superior a 30.000€:")
for empleado in empleados_bien_pagados:
    print(empleado)