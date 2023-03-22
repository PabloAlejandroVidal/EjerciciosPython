#9 - Crear un programa que determine si un número ingresado por el usuario es primo o no.

import math

def es_primo(n):
    if n <= 1:
        return False
 # Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número (inclusive)
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        numero_ingresado = int(input("Ingrese un numero para determinar "
                                     "si es o no un numero primo: "))
        if numero_ingresado < 1:
            print("El numero ingresado debe ser mayor o igual a 1.")
        else:
            break
    except ValueError:
        print("El numero ingresado no es valido.")

if es_primo(numero_ingresado):
    print("El numero ingresado es un numero primo.")
else:
    print("El numero ingresado no es un numero primo")