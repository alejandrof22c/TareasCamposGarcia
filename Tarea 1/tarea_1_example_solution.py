# La funcion invert case recibe un solo parametro "cadena" que es un string
# y retorna lo siguiente

# Caso de éxito => 0

# Error en caso de que la entrada no sea un string => -16
# Error en caso de un caracter fuera del abecedario => -32
# Error en caso de un string vacio => -48

# Parametros
# Entrada: Un string llamado cadena
# Salida: La cadena invertida (exito) o None (error) y un codigo

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

# Errores esparados metodo de números primos
# Error en caso de que no se pase un número entero => -64
# Error en caso de que el número entero sea mayor a 100 => -80

def numero_primo(numero):
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if  isinstance(numero, int):
        if numero < 100:
            Salida = []
            for i in primos:
                if i <= numero:
                    Salida.append(i)
                else:
                    break
        else:
            return -80, None
    else:
        return -64, None
    return 0, Salida
