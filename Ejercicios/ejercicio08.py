#8 - Crear un programa que convierta un número decimal en binario.

while True:
    try:
        numero_ingresado = int(input("Ingrese un numero en decimal para convertir a binario: "))
        if numero_ingresado < 0:
            print("El numero ingresado debe ser positivo.")
        else:
            break
    except ValueError:
        print("El numero ingresado no es valido.")

numero_binario = bin(numero_ingresado)

print(f"El numero en binario es: {numero_binario[2:]}")
print(f"El numero en decimal es: {int(numero_binario, 2)}")