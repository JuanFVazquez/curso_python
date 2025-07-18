# Pedir al usuario que introduzca un correo electrónico
correo = input("Introduce tu correo electrónico: ")

# Variables de control
arroba_encontrada = False
punto_despues_arroba = False

# Recorrer cada carácter del correo
for i in range(len(correo)):
    if correo[i] == '@':
        if arroba_encontrada:
            # Ya había un @ antes: error
            break
        arroba_encontrada = True
    elif correo[i] == '.' and arroba_encontrada:
        punto_despues_arroba = True

# Comprobar las condiciones finales
if arroba_encontrada and punto_despues_arroba:
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")
