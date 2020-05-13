# Luis David López Raquec
# 1990-19-9146
# Seccion C
# Grupo 4 
from collections import deque
import random

variable_quieres_seguir = True

while variable_quieres_seguir:
       
    aleatorio = random.randrange(0, 3)
    elijePc = ""
    print("Elija su opción: ")
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    opcion = int(input("Su Opción: "))

# declaramos el numero de opcion que el usuario elegira.
    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print("Tu elejiste: ", elijeUsuario)

# declaramos el numero de posicion que la computadora "PC" elejira utilizando [o, 1, 2] Piedra, Papel, Tijera.
    if aleatorio == 0:
        elijePc = "Piedra"
    elif aleatorio == 1:
        elijePc = "Papel"
    elif aleatorio == 2:
        elijePc = "Tijera"
    print("PC elijio: ", elijePc)

    print("\n::::::------::::::::\n")
# declaramos las comparaciones del usuario contra la computadora
    if elijePc == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste\nPapel envulve piedra")
    elif elijePc == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste\nTijera corta papel")
    elif elijePc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste\nPiedra pisa tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra":
        print("Perdiste\nPapel envulve piedra")
    elif elijePc == "Tijera" and elijeUsuario == "Papel":
        print("Perdiste\nTijera corta papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("Perdiste\nPiedra pisa tijera")
    elif elijePc == elijeUsuario:
        print("Empate")
    # preguntamos al usuario si quieres seguir jugando o salir del juego
    # "y" seguir jugando
    # "n" salir del juego
    entrada_usuario = input("\nQuieres seguir jungado. y/n: ")

    if(entrada_usuario == "y"):
        variable_quieres_seguir = True
    elif (entrada_usuario == "n"):
        variable_quieres_seguir = False
        print("Gracias por Participar\n")
    else:
        print('Ingrese una entrada correcta...')

historial = deque()
for historial in [elijePc]:
    historial.append(elijePc)
    historial.append(elijePc)
    historial.append(elijePc)
    historial.append(elijePc)

print(f"Historial actual {historial}")
print('#################')


while len(historial) > 0:
    # extraer el último elemento utilizando pop
    ultima_acction = historial.pop()


    print(f'Acción más reciente: {ultima_acction}')
    print(f'Historial actual: {historial}')
    print('#################')

