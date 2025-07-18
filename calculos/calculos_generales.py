def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Error: Division by zero is not allowed")
    
def potencia(base, exponente):
    return base ** exponente
    
def redondear(a):
    return round(a)
