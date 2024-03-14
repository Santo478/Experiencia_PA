import random
import time

def memoria():
    nivel = input("Elige un nivel de dificultad del 1 al 3: ")
    lista = ["1","2","3"]
    while True:
        if nivel not in lista:
            nivel = input("Elige un nivel de dificultad del 1 al 3: ")
        else:
            break
    if nivel == "1":
        numero = random.randint(1,10)
        numero = str(numero)
        print(f"Recuerda este numero: {numero}")
        time.sleep(3)
        for i in range(50):
            print("")
        guess = str(input("Cual es el numero que viste: "))
        if guess == numero:
            print("Ganaste!")
        else:
            print("Perdiste, intentalo de nuevo")
    elif nivel == "2":
        numero = random.randint(10000,10000000)
        numero = str(numero)
        print(f"Recuerda este numero: {numero}")
        time.sleep(5)
        for i in range(50):
            print("")
        guess = str(input("Cual es el numero que viste: "))
        if guess == numero:
            print("Felicidades, ganaste!")
        else:
            print("Perdiste, intentalo de nuevo")
    else:
        numero = random.randint(10000000000,100000000000000)
        numero = str(numero)
        print(f"Recuerda este numero: {numero}")
        time.sleep(6)
        for i in range(50):
            print("")
        guess = str(input("Cual es el numero que viste: "))
        if guess == numero:
            print("Felicidades, ganaste!")
        else:
            print("Perdiste, intentalo de nuevo")