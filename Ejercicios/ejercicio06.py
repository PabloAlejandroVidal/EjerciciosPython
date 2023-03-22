#6 - Crear un programa que calcule el factorial de un número ingresado por el usuario.

def calcularFactorial(valor):
    resultado = 1
    for i in range(valor):
        resultado *= (valor - i)
    return resultado
    
while True:
    try:
        numero_ingresado = int(input("Ingrese un numero: "))
    except Exception:
        print("Ingresa un numero valido!")
    else:
        break

numero_factorial = calcularFactorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es {numero_factorial}")