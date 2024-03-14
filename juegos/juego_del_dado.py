from random import *

def juego_del_dado():
    usuario = 0
    computador = 0
    while True:
        confirm = input('Aprieta enter para lanzar un dado\n')
        tiro1 = randint(1,6)
        usuario += tiro1
        print(f'Has tirado el dado y ha salido un {tiro1}!')
        print(f'Puntaje: {usuario}')
        if usuario >= 30:
            print('Has ganado!')
            break
        tiro2 = randint(1,6)
        computador += tiro2
        print(f'El computador ha tirado un dado y ha sacado un {tiro2}!')
        print(f'puntaje: {computador}')
        if computador >= 30:
            print('El computador gana!')
            break

    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """

print('xd')
juego_del_dado()