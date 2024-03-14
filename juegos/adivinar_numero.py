from random import *

def adivinar_numero():
    num = randint(1,10)
    while True:
        guess = int(input('Adivina un número entre 1 y 10\n'))
        if guess < 1 or guess > 10:
            print('Introduce un número válido')
        elif guess == num:
            print('Adivinaste!')
            break
        elif guess != num:
            print('Intenta de nuevo')
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
adivinar_numero()