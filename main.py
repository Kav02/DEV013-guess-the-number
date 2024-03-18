''' Guess the number'''
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103
import random
#Generar un número aleatorio entre 1 y 100
secret_number= random.randint(1,100)
print(secret_number)
#Ingresar el nombre del participante
participant_name = input("Por favor ingresar su nombre?  ")
participants = [participant_name,"Computadora"]
player_guess=[]
computer_guess=[]
#Variables globales usadas para ajustar los intentos de la computadora
low_range = 1
high_range = 100
#Turnos
def turn(player):
    #Solicitar un número usando un loop para guardar cada intento
    if player == participant_name:
        guess = int(input("Ingresa un número del 1 al 100: "))
        if guess > 100 or guess < 0:
            print('Ingreso inválido, ingresa un número del 1 al 100')
        else:
            player_guess.append(guess)
    else:
        guess = round((low_range + high_range)/2)
        print("Intento de la computadora: "+ str(guess))
        computer_guess.append(guess)
    return player, guess

#Evaluar el intento
def number_evaluation(player, guess):
    global low_range, high_range
    if guess == secret_number:
        print('El ganador es', player + '! El número secreto es:', str(secret_number) + ' y lo lograste en', str(ATTEMPTS) + ' intentos')
        print('Tus intentos fueron: ', player_guess)
        return False
    if guess > secret_number:
        print("El número es muy alto")
        if guess < high_range:
            high_range = guess
    else:
        print("El número es muy bajo")
        if guess > low_range:
            low_range = guess
    return True

# Compararlo con el número secreto
GUESSING = True
ATTEMPTS = 0
while GUESSING:
    ATTEMPTS += 1
    for participant in participants:
        playing = turn(participant)
        RESULT = number_evaluation(playing[0], playing[1])
        if RESULT is False:
            GUESSING = False
            break
        