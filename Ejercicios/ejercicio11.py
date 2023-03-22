#11 - Crear un programa que determine si una cadena de texto es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def es_palindromo(texto):
    longitud_texto = len(texto)
    if longitud_texto > 0:
        # Si el texto contiene al menos un caracter se calculara la mitad de su longitud
        # para comparar cada caracter de la primer mitad del texto con sus opuestos en espejo,
        # de manera de que al encontrar una discrepancia no sera un palindromo y por lo tanto
        # la funcion retornara False
        # En caso de ser inpar la cantidad de caracteres el caracter del medio no se comparara
        # ya que la funcion int descarta el valor decimal del resultado de la division
        mitad_longitud = int(longitud_texto / 2)
        for i in range(mitad_longitud):
            if texto[i] != texto[(-(i + 1))]:
                return False
    return True

texto = input("Igrese un texto para determinar si es o no palindromo: ")
if es_palindromo(texto):
    print(f'"{texto}" es un palindromo')
else:
    print(f'"{texto}" no es un palindromo')