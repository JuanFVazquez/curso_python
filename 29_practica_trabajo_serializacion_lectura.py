import pickle

# Leer el fichero binario y recuperar la lista
with open("nombres.dat", "rb") as fichero:
    nombres_recuperados = pickle.load(fichero)

print("Lista recuperada desde el fichero binario:")
print(nombres_recuperados)
