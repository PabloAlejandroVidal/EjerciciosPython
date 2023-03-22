# Crear un programa que calcule el área y perímetro de un rectángulo,
# pidiendo al usuario que ingrese los valores de base y altura.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea (self):
        return self.base * self.altura

    def calcularPerimetro (self):
        return self.base * 2 + self.altura * 2
    
base = input("Ingresa la base del rectangulo: ")
altura = input("Ingresa la altura del rectangulo: ")

rectangulo = Rectangulo(int(base), int(altura))

print(f"El area del rectangulo es de {rectangulo.calcularArea()}")
print(f"El perimetro del rectangulo es de {rectangulo.calcularPerimetro()}")
