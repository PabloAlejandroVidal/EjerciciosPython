'''
Ejercicio:
Escribe un programa en Python que tome una cadena de texto como entrada y realice las siguientes operaciones:
'''

# Imprime la longitud de la cadena.
# Imprime la cadena en mayúsculas.
# Imprime la cadena en minúsculas.
# Imprime la primera letra de cada palabra en la cadena.
# Reemplaza todas las ocurrencias de la letra "a" por la letra "e".
# Divide la cadena en una lista de palabras y cuenta cuántas palabras tiene.

texto_entrada = input("Ingrese un texto: ")

print(f"La longitud de la cadena es: {len(texto_entrada)}")
print(f"Texto en mayúsculas: {texto_entrada.upper()}")
print(f"Texto en minúsculas: {texto_entrada.lower()}")
lista_texto = texto_entrada.split(" ")

iniciales = []
for palabra in lista_texto:
    iniciales.append(palabra[0])
    
print(f"Las primeras letras de cada palabra son: {iniciales}")

print(texto_entrada.replace("a", "e"))
print(f"En la cadena ingresada hay un total de {len(lista_texto)} palabras")