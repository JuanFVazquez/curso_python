import pickle
import os

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, vive en {self.ciudad}"


class ListaPersonas:
    def __init__(self, archivo="personas.dat"):
        self.archivo = archivo
        self.personas = self._cargar_desde_fichero()

    def _cargar_desde_fichero(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "rb") as f:
                try:
                    return pickle.load(f)
                except EOFError:
                    return []
        return []

    def _guardar_en_fichero(self):
        with open(self.archivo, "wb") as f:
            pickle.dump(self.personas, f)

    def agregar(self, persona):
        self.personas.append(persona)
        self._guardar_en_fichero()
        print(f"{persona.nombre} ha sido añadida a la lista y guardada en el archivo.")

    def mostrar_todas(self):
        print("Lista de personas:")
        for persona in self.personas:
            print(persona)

    def buscar_por_nombre(self, nombre):
        print(f"Buscando personas con el nombre: {nombre}")
        for persona in self.personas:
            if persona.nombre.lower() == nombre.lower():
                print(persona)
                return
        print("No se encontró ninguna persona con ese nombre.")

persona1 = Persona("Laura", 28, "Madrid")
print(persona1)

# Crear la lista
lista = ListaPersonas()

# Crear y añadir personas
p1 = Persona("María", 21, "Sevilla")
p2 = Persona("Jorge", 45, "Bilbao")

lista.agregar(p1)
lista.agregar(p2)

# Mostrar todas las personas
lista.mostrar_todas()

# Buscar una persona
lista.buscar_por_nombre("Luis")

