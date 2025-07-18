class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario  # salario mensual

    def __str__(self):
        return f"Empleado: {self.nombre}, Cargo: {self.cargo}, Salario con comisión: {self.salario:.2f}€"

def calculo_comision(empleado):
    """Calcula un 3% de comisión solo si el salario es menor o igual a 2500€ y sobre el salario y lo suma al salario base."""
    if empleado.salario <= 2500:
        comision = empleado.salario * 0.03
        empleado.salario += comision
    return empleado

# Lista de empleados con salario mensual
empleados = [
    Empleado("Laura", "Desarrolladora", 2500),
    Empleado("Carlos", "Analista", 2200),
    Empleado("María", "Diseñadora UX", 2100),
    Empleado("Jorge", "Administrador de sistemas", 2700),
    Empleado("Ana", "Product Manager", 3200)
]

# Aplicar la comisión a todos los empleados
empleados_con_comision = list(map(calculo_comision, empleados))

# Mostrar los empleados con el salario actualizado
print("Empleados tras aplicar la comisión del 3%:")
for empleado in empleados_con_comision:
    print(empleado)
