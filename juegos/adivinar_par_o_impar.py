import random

def adivinar_par_o_impar():
    numero = random.randint(1,2)
    guess = input("Adivina si el numero es par o impar: ")
    guess = guess.lower()
    while True:
        if guess != "impar" and guess != "par":
            guess = input("Por elige solo entre par e impar: ")
            guess = guess.lower()
        else:
            break
    if guess.lower() == "par":
        if numero%2 == 0:
            print("Era par, adivinaste!")
        else:
            print("Perdiste, intentalo de nuevo")
    elif guess.lower() == "impar":
        if numero%2 == 1:
            print("Era impar, adivinaste!")
        else:
            print("Perdiste, intentalo de nuevo")