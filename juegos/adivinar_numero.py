from random import *

def adivinar_numero():
    while True:
        num = randint(1,10)
        while True:
            guess = input('Adivina un número entre 1 y 10\n')
            if guess not in "0123456789":
                print("Introduce un número válido")

            elif int(guess) < 1 or int(guess) > 10:
                print('Introduce un número válido entre 1 y 10')
            elif int(guess) == num:
                print('Adivinaste!')
                break
            elif int(guess) != num:
                print('Adivinaste mal. Intenta de nuevo')
        replay = input("Quieres jugar de nuevo?\nY/N\n")
        if replay not in "YN":
            print("Opción no válida")
        if replay == "N":
            break
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
adivinar_numero()