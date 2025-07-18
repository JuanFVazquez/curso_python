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


coche1 = Vehiculo("Mazda", "CX-30")

coche2 = Vehiculo("Peugeot", "307")

coche3 = Vehiculo("Ford", "Fiesta")

coches = [coche1, coche2, coche3]


# Serializamos el objeto al archivo 'persona.dat'
with open("coches.dat", "wb") as fichero:
    pickle.dump(coches, fichero)

print("Objeto serializado correctamente en 'coches.dat'")
