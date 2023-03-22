#12 - Crear un programa que lea una lista de números y devuelva el promedio de todos los elementos.


def sumarLista(numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

def calcular_promedio(lista_numeros):
    longitud_lista = len(lista_numeros)
    if longitud_lista > 0:
        suma = sumarLista(lista_numeros)
        return suma / longitud_lista
    return None
    
lista_numeros = []

while True:
    try:
        num_ingresado = input("Ingresa un numero para agregar a la lista: ")
        if num_ingresado == "":
            break
        num_ingresado = int(num_ingresado)
        lista_numeros.append(num_ingresado)
    except Exception:
        print("El numero ingresado no es valido")
        
if len(lista_numeros) > 0:
    print(f"La lista de numeros es: {lista_numeros}")
else:
    print("La lista de numeros esta vacia")

promedio = calcular_promedio(lista_numeros)

if promedio is not None:
    print(f"El promedio de los numeros de la lista es {promedio}")
else:
    print("No hay elementos en la lista para calcular el promedio")