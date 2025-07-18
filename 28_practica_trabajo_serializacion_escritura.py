import pickle

# Lista con 4 nombres de persona
nombres = ["Ana", "Luis", "Carlos", "María"]

# Crear un fichero binario y guardar la lista en él
with open("nombres.dat", "wb") as fichero:
    pickle.dump(nombres, fichero)

print("Lista volcada en el fichero binario 'nombres.dat'.")
