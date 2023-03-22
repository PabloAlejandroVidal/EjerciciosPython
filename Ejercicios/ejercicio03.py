# Crear un juego de adivinanza de números,
# donde el programa genera un número aleatorio y el usuario tiene que adivinarlo en un número limitado de intentos.

import random

numero_aleatorio = random.randint(1, 101)
intentos = 10

print(f"Tienes {intentos} intentos para encontrar el numero oculto entre 1 y 100.")

for num_intento in range(intentos):
    intentos_restantes = intentos - (num_intento + 1)
    while True:
        try:
            numero_elegido = int(input("ingrese un numero: "))
            break
        except Exception:
            print("Debes ingresar un numero valido!")
            continue
        
    if numero_elegido == numero_aleatorio:
        print(f"Lo has logrado, el numero era el {numero_aleatorio}.")
        break
    else:
        if intentos_restantes > 0:
            print(f"Intenta una vez mas. Intentos restantes {intentos_restantes}.")

print(f"Haz perdido, el numero oculto era {numero_aleatorio}.")