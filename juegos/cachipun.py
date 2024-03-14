
import random
# 1 gana 2
# 2 gana 3
# 3 gana 1
def cachipun():
    Work = True
    print("Bienvenido a Cachipun, te enfrentaras a la computadora en este juego")
    House = random.randint(1,3)
    while Work:
        print("Elige Piedra, Papel o Tijeras")
        person = input()
        compare = person.lower()
        if compare == "piedra":
            Work = False
        elif compare == "papel":
            Work = False
        elif compare == "tijera":
            Work = False
        else:
            print("Parece que ocurrio un error con tu seleccion")


    if compare == "piedra":
        Val = 1
        if House == Val:
            Win = 0
        elif House == 2:
            Win = 2
        elif House == 3:
            Win = 1


    elif compare == "papel":
        Val = 2
        if House == Val:
            Win = 0
        elif House == 3:
            Win = 2
        elif House == 1:
            Win = 1


    elif compare == "tijeras":
        Val = 3
        if House == Val:
            Win = 0
        elif House == 1:
            Win = 2
        elif House == 2:
            Win = 1

    if House == 1:
        Val = "piedra"
    elif House == 2:
        Val = "papel"
    elif House == 3:
        Val = "tijera"
    print("La computadora eligio", Val)
    if Win == 0:
        print("Que tontos... empataron")
    elif Win == 1:
        print("Rayos y centellas, has derrotado a la maquina")
        print("Ganaste")
    elif Win == 2:
        print("La casa siempre gana")
        print("Perdiste")

    print("fin del juego")

cachipun()