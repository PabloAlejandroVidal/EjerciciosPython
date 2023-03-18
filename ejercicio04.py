#Crear un programa que lea un archivo de texto y cuente cuántas palabras hay en él.

texto = ""
with open('archivo.txt', 'r') as archivo:
    texto = archivo.read()

palabras = texto.split()
num_palabras = len(palabras)
print(f"Este archivo tiene {num_palabras} palabras")