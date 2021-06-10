from os import system
import random
from colorama import Fore, Style, init

# Colorama init
init(autoreset=True)

# Functions
def welcome() :
    
    welcome_message = '''
Bienvenido a Number Guesser!
'''
    
    print(Fore.BLUE + welcome_message)
    
    while True :
        menu = '''
Utiliza el numero correspondiente para hacer una seleccion:
1) Iniciar una partida.
2) Instrucciones.
3) Salir
> '''
    
        decision = int(input(menu))
    
        if decision == 1 :
            system('cls')
            difficulty_level()
        elif decision == 2 :
            system('cls')
            instructions()
        elif decision == 3 :
            system('cls')
            print(Fore.MAGENTA + "\nHasta pronto!")
            exit()
        else :
            system('cls')
            print(Fore.BLUE + welcome_message)
            print(Fore.RED + "Opcion incorrecta, vuelva a intentarlo.")
    

def instructions() :
    
    inst = '''
Las instrucciones son las siguientes:

El juego es simple, el objetivo principal del juego es adivinar el numero.
Hay pistas, estas se te daran en caso de dar el numero incorrecto.
Éxito en tus partidas.
    '''
    
    print(Fore.GREEN + inst)
    
    while True :
        menu = '''
Utiliza el numero correspondiente para hacer una seleccion:
1) Ir al inicio.
2) Salir.
> '''
    
    
        decision = int(input(menu))
    
        if decision == 1 :
            system('cls')
            welcome()
        elif decision == 2 :
            system('cls')
            print(Fore.MAGENTA + "\nHasta pronto!")
            exit()
        else :
            system('cls')
            print(Fore.GREEN + inst)
            print(Fore.RED + "Opcion incorrecta, vuelva a intentarlo")

def difficulty_level() :
    menu = '''
Escoje la dificultad:
    
Utiliza el numero correspondiente para hacer una seleccion:
1) Facil.
2) Normal.
3) Dificil.
4) Maestro.
> '''

    while True :
        
        decision = int(input(menu))
        
        if decision == 1 :
            system('cls')
            match(10)
            break
        elif decision == 2 :
            system('cls')
            match(30)
            break
        elif decision == 3 :
            system('cls')
            match(60)
            break
        elif decision == 4 :
            system('cls')
            match(1000)
            break
        else :
            system('cls')
            print(Fore.RED + "Opcion incorrecta, vuelve a intentarlo")
            

def match(diffLevel) :
    random_number = random.randint(1, diffLevel)
    user_guess = 0
    
    while user_guess != random_number :
        user_guess = int(input(f"Adivina el numero entre 1 y {diffLevel}. -> "))
        if user_guess > random_number :
            print(Fore.YELLOW + "Lo siento. Muy arriba.")
        elif user_guess < random_number :
            print(Fore.YELLOW + "Lo siento. Muy abajo.")
    
    print(Fore.CYAN + f"\nCorrecto! Adivinaste el numero {random_number}.")
        

# Output
welcome()