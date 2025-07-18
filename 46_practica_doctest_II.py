def evaluar_mail(email):
    """
    Evalúa si un correo electrónico es válido según las siguientes reglas simples:
    - Debe contener exactamente un arroba (@).
    - El arroba no puede estar en la última posición.

    Parámetros:
    - email (str): dirección de correo a evaluar.

    Retorna:
    - bool: True si es válido, False si no.

    Ejemplos:
    >>> evaluar_mail("usuario@dominio.com")
    True

    >>> evaluar_mail("usuario@@dominio.com")
    False

    >>> evaluar_mail("usuariodominio.com")
    False

    >>> evaluar_mail("usuario@")
    False
    """
    if email.count("@") != 1:
        return False
    if email.endswith("@"):
        return False
    return True

# Ejecutar los tests y ejemplo si se ejecuta como script
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Prueba visual
    print(evaluar_mail("usuario@dominio.com"))  # True
