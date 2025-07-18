def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
   
    #if b == 0:
    #    return "Error: No se puede dividir entre cero"
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por 0. Operación errónea"

def main():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Elige una operación (1-4): ")
    
    while True:
        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            break
        except ValueError:
            print("Error: Debes introducir números válidos. Inténtalo de nuevo")
            #return

    if opcion == '1':
        resultado = sumar(a, b)
    elif opcion == '2':
        resultado = restar(a, b)
    elif opcion == '3':
        resultado = multiplicar(a, b)
    elif opcion == '4':
        resultado = dividir(a, b)
    else:
        print("Opción no válida.")
        return

    print("Resultado:", resultado)

    print("El programa ha finalizado")

if __name__ == "__main__":
    main()
