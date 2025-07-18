import pickle

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
        return f"{self.marca} {self.modelo} ha arrancado."

    def acelerar(self):
        if self.enmarcha:
            self.acelera = True
            self.frena = False
            return f"{self.marca} {self.modelo} está acelerando."
        else:
            return "No puedes acelerar si el vehículo no está en marcha."

    def frenar(self):
        if self.enmarcha:
            self.frena = True
            self.acelera = False
            return f"{self.marca} {self.modelo} está frenando."
        else:
            return "No puedes frenar si el vehículo no está en marcha."

    def estado(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, En marcha: {self.enmarcha}, Acelera: {self.acelera}, Frena: {self.frena}"

# Leemos el objeto desde el archivo
with open("coches.dat", "rb") as fichero:
    coches = pickle.load(fichero)

print("Objeto recuperado desde el archivo:")
for c in coches:
    print(c.estado())