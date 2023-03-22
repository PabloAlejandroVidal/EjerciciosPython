#Crear un programa que simule un juego de piedra, papel o tijera entre dos jugadores, 
# pidiendo que ingresen su elección y mostrando el resultado.

manos = ["piedra", "papel", "tijera"]

def pedirMano(jugador):
    while True:
        mano = input(f'{jugador}: Ingrese "piedra", "papel" o "tijera"')
        if mano in manos:
            break
        else:
            print("Debes ingresar una opcion correcta.")
    return mano

def mostrarGanador(mano1, mano2):
    gana1 = "El jugador 1 ha ganado."
    gana2 = "El jugador 2 ha ganado."
    empate = "Han empatado"
    
    if mano1 == "piedra":
        if mano2 == "papel":
            res = gana2
        elif mano2 == "tijera":
            res = gana1
        else:
            res = empate
    elif mano1 == "papel":
        if mano2 == "piedra":
            res = gana1
        elif mano2 == "tijera":
            res = gana2
        else:
            res = empate
    else:
        if mano2 == "piedra":
            res = gana2
        elif mano2 == "papel":
            res = gana1
        else:
            res = empate
    return res

mano1 = pedirMano("jugador 1")
mano2 = pedirMano("jugador 2")

print(mostrarGanador(mano1, mano2))