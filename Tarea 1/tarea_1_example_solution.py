# La funcion invert case recibe una cadena y tiene el siguiente comportamiento

# Caso de éxito => 0

# Error en caso de que la entrada no sea un string => -16
# Error en caso de un caracter fuera del abecedario => -32
# Error en caso de un string vacio => -48

def invert_case(cadena):
    invertida = ""

    if not isinstance(cadena, str):
        return -16, None

    if cadena == "":
        return -48, None

    for i in cadena:
        if not i.isalpha():
            return -32, None
        if i.isupper():
            invertida += i.lower()
        else:
            invertida += i.upper()

    return 0, invertida
