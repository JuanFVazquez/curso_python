class Coche:
    def __init__(self, largoChasis, anchoChasis, ruedas=4):
        self.__largoChasis = largoChasis
        self.__anchoChasis = anchoChasis
        self.__ruedas = ruedas
        self.__enmarcha = False

    def arrancar(self, parar):
        if not self.__enmarcha and not parar:
            chequeo = self.__chequeo_interno()
            if chequeo:
                self.__enmarcha = True
                return "El coche ha arrancado."
            else:
                return "Algo ha ido mal en el chequeo, no podemos arrancar"
        elif self.__enmarcha and not parar:
            return "El coche ya está en marcha."
        elif self.__enmarcha and not parar:
            self.__enmarcha = False
            return "Paramos el covhe..."
        else:
            return "El coche ya está parado"

    def estado(self):
        return f"Largo: {self.__largoChasis}, Ancho: {self.__anchoChasis}, Ruedas: {self.__ruedas}, ¿En marcha?: {self.__enmarcha}"

    def __chequeo_interno(self):
        print ("Realizando chequeo interno")

        gasolina = "ok"
        aceite = "ok"
        puertas = "cerradas"

        if gasolina == "ok" and aceite == "ok" and puertas == "cerradas":
            return True
        else:
            return False
        
mi_coche = Coche(4.5, 1.8)
print(mi_coche.estado())          # Muestra el estado inicial del coche
print(mi_coche.arrancar(False))        # Intenta arrancar el coche
print(mi_coche.estado())          # Verifica si ha cambiado el estado a en marcha

print("------A continuación creamos el segundo objet0--------")

mi_coche2 = Coche(3.5, 1.6)

print(mi_coche2.estado())          # Muestra el estado inicial del coche
print(mi_coche2.arrancar(True))        # Intenta arrancar el coche
mi_coche2.__ruedas = 2
print(mi_coche2.estado())          # Verifica si ha cambiado el estado
