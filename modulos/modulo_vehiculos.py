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

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.haciendo_caballito = False

    def caballito(self):
        if self.enmarcha and self.acelera:
            self.haciendo_caballito = True
            return f"{self.marca} {self.modelo} está haciendo un caballito! 🏍️"
        else:
            self.haciendo_caballito = False
            return "No se puede hacer un caballito: asegúrate de que la moto esté en marcha y acelerando."

    def estado(self):
        estado_base = super().estado()
        caballito_info = "Sí" if self.haciendo_caballito else "No"
        return f"{estado_base}, Haciendo caballito: {caballito_info}"

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        if cargar:
            return f"La furgoneta {self.marca} {self.modelo} está cargada."
        else:
            return f"La furgoneta {self.marca} {self.modelo} no está cargada."

class VElectrico:
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.autonomia = 100
        return "La batería está completamente cargada."
    
class BicicletaElectrica(VElectrico, Vehiculo):
    def __init__(self, marca, modelo):
        Vehiculo.__init__(self, marca, modelo)
        VElectrico.__init__(self)  # Llamamos explícitamente al constructor de VElectrico

