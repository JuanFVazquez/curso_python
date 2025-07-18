def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        resultado = op1 / op2
    except ValueError:
        print("Error: Debes introducir números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print("La división es " + str(resultado))
    finally:
        print("Cálculo finalizado")

divide()
