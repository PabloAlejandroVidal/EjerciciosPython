#Crear un programa que lea una cadena de texto y cuente cuántas veces aparece cada letra en la cadena.

cadena = "Esta es una cadena"
diccionario = {}

for caracter in cadena:
    caracter = caracter.lower()
    if caracter.isalpha():
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1

for letra in diccionario:
    print(f"La letra {letra} aparece en el diccionario {diccionario[letra]} veces")