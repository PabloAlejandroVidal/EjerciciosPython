#10 - Crear un programa que simule una calculadora básica, 
# pidiendo al usuario que ingrese dos números y 
# una operación (+, -, *, /) y devolviendo el resultado.

def div(op1, op2):
    try:
        r = op1 / op2
    except ZeroDivisionError:
        return None
    else:
        return r

def mult(op1, op2):
    return op1 * op2

def suma(op1, op2):
    return op1 + op2

def resta(op1, op2):
    return op1 - op2


def pedirOperando(msgPeticion):
    while True:
        try:
            op = int(input(msgPeticion))
            break
        except ValueError:
            print("El numero ingresado no es valido.")
    return op

def pedirOperador():
    opDic = {
        '+': suma,
        '-': resta,
        '*': mult,
        '/': div
    }
    
    while True:
        op = input(f"Elije un operador: ({', ' .join(opDic)}): ")
        if op in opDic:
            break
        else:
            print("Debes elegir un operador valido.")
        continue
    
    return opDic[op]

operando_uno = pedirOperando("Ingrese el primer operando: ")
operando_dos = pedirOperando("Ingrese el segundo operando: ")


while True:
    operador = pedirOperador()
    valor = operador(operando_uno, operando_dos)
    if valor is not None:
        print(f"El resultado de su operacion es: {valor}")
        break
    else:
        print("La operacion no es valida")
        continue

