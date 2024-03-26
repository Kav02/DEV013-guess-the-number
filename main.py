''' Guess the number'''
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103
import random

# Inicializar variables globales
participant_name = ""
participants = []
participant_guess=[]
computer_guess=[]
attempts=0
secret_number = ""
low_range = 1
high_range = 100

#Inicializar el juego
def reset_game():
    global secret_number, participant_guess, computer_guess, attempts, low_range, high_range
    secret_number = random.randint(1, 100)
    participant_guess = []
    computer_guess = []
    attempts = 0
    low_range = 1
    high_range = 100


#Turnos
def turn(player):
    #Solicitar un número usando un loop para guardar cada intento
    while True:
        if player == participant_name:
            guess = int(input("Ingresa un número del 1 al 100: "))
            if 1 <= guess <= 100:
                participant_guess.append(guess)
                break
            else:
                print('El número ingresado no es válido, debe ser un número del 1 al 100')
        else:
            guess = round((low_range + high_range)/2)
            print("Intento de la computadora: "+ str(guess))
            computer_guess.append(guess)
            break
    return player, guess

#Evaluar el intento
def number_evaluation(player, guess):
    global low_range, high_range
    if guess == secret_number:
        print('El ganador es', player + '! El número secreto es:', str(secret_number) + ' y lo ha adivinado en', str(attempts) + ' intentos')
        print('Los intentos de ', participant_name + ' fueron: ', participant_guess)
        return True
    if guess > secret_number:
        print("El número es muy alto")
        if guess < high_range:
            high_range = guess
    else:
        print("El número es muy bajo")
        if guess > low_range:
            low_range = guess

    return False

def main():
    global participant_name, participants, attempts

    #Ingresar el nombre del participante
    participant_name = input("Por favor ingresar su nombre?  ")
    participants = [participant_name,"Computadora"]

    # Compararlo con el número secreto
    guessing = True
    attempts = 0
    while guessing:
        attempts += 1
        for participant in participants:
            playing = turn(participant)
            RESULT = number_evaluation(playing[0], playing[1])
            if RESULT is True:
                play_again = input("¿Quieres jugar de nuevo? S/N ")
                if play_again.upper() == "S":
                    reset_game()
                else:
                    guessing = False
                    print("¡Gracias por participar!")
                    break
if __name__ == '__main__':
    #Resetear el juego
    reset_game()
    main()
