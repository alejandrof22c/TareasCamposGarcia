# La funcion invert case recibe un solo parametro "Cadena" que es un string
# y retorna lo siguiente:

# Caso de éxito => 0

# Error en caso de que la entrada no sea un string => -16
# Error en caso de un caracter fuera del abecedario => -32
# Error en caso de un string vacio => -48

# Parametros
# Entrada: Un string llamado Cadena.
# Salida: Un codigo y la cadena invertida (exito) o None (error).

def invert_case(Cadena):
    invertida = ""

    #Condicional para variables tipo string
    if not isinstance(Cadena, str):
        return -16, None

    #Condicional para strings vacios
    if Cadena == "":
        return -48, None

    # Bucle for recorre Cadena e invierte el character
    for i in Cadena:
        if not i.isalpha():
            return -32, None
        if i.isupper():
            invertida += i.lower()
        else:
            invertida += i.upper()

    return 0, invertida

# La funcion numero_primo recibe un solo parametro "base" que es un integer
# y retorna lo siguiente:

# Errores esparados metodo de números primos
# Error en caso de que no se pase un número entero => -64
# Error en caso de que el número entero sea mayor a 100 => -80

# Parametros
# Entrada: Un integer llamado base.
# Salida: Un codigo y un arreglo con todos los números primos
# entre 1 y “base" (exito) o None (error).


def numero_primo(base):
    salida = []
    primos = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ]

    #Condicional para variable no enteras
    if not isinstance(base, int):
        return -64, None

    # Es necesario agregar este caso en especifico ya que python
    # toma el True booleano como un 1
    if base is True:
        return -64, None

    # Condicional para numeros mayores a 100
    if base > 100:
        return -80, None
    
    # Bucle for recorre el arreglo de numeros primos
    # Agrega primos al arreglo salida hasta superar la base
    for i in primos:
        if i <= base:
            salida.append(i)
        else:
            break

    return 0, salida
