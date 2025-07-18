class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Lugar de residencia: {self.lugar_residencia}"

class Empleado(Persona):
    def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad):
        super().__init__(nombre, edad, lugar_residencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        base = super().descripcion()
        return f"{base}, Salario: {self.salario}€, Antigüedad: {self.antiguedad} años"


persona = Persona("Lucía", 30, "Madrid")
print(persona.descripcion())

empleado = Empleado("Carlos", 45, "Barcelona", 28000, 10)
print(empleado.descripcion())

print(isinstance(persona, Empleado))