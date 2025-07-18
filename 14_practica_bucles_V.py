for letra in "Python":
    if letra=="h":
        continue

    print("Viendo la letra", letra)


nombre = "Pildoras Informaticas"

contador = 0

for i in nombre:

    if i==" ":
        continue
    contador+=1

print(contador)

print(len(nombre))

email = input("Introduce tu email, por favor: ")

for i in email:

    if i == "@":
        arroba = True
        break
    else:
        arroba = True
else:

    arroba = False

print(arroba)

