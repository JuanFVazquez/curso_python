class Coche:
    def desplazamiento(self):
        return "El coche se desplaza sobre 4 ruedas."

class Moto:
    def desplazamiento(self):
        return "La moto se desplaza sobre 2 ruedas."

class Camion:
    def desplazamiento(self):
        return "El camión se desplaza sobre 6 ruedas."


mi_coche = Coche()
mi_moto = Moto()
mi_camion = Camion()

#print(mi_coche.desplazamiento())
#print(mi_moto.desplazamiento())
#print(mi_camion.desplazamiento())

vehiculos = [Coche(), Moto(), Camion()]

for vehiculo in vehiculos:
    print(vehiculo.desplazamiento())

