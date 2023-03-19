#7 - Crear un programa que lea una lista de números y devuelva la suma de todos los elementos.

def sumarLista(numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado
    
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
        
print(f"La lista de numeros es: {lista_numeros}")

suma = sumarLista(lista_numeros)

print(f"La suma de los numeros en la lista es {suma}")