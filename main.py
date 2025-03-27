import pokemon_class as p_class
import random
import json
from pathlib import Path

#if __name__ == "__main__":

ruta_archivo = Path(__file__).parent / "pokemon_list.json"  

with open(ruta_archivo, mode='r') as file:
    pokemons = json.load(file)

# for pokemon in pokemons:
#     print(f"\n{pokemon}")

def numberInput(message):

    while True:

        try:
            var = int(input(message))

            break
        except ValueError as error:
            print(
                "\nHas introducido un caracter invalido. Por favor intentalo de nuevo"
            )
            print(error)
    return var


def stringInput(message):

    try:
        var = str(input(message))
    except ValueError as error:
        print("\nHas introducido un caracter invalido. Por favor intentalo de nuevo")
        print(error)
    return var

def pokemon_duel(): 
    
    while True: 
        
        print("\nBienvenido a Pokemon Duel. Elije una opcion:")
        print("1. Descripcion del juego")
        print("2. Lista de Pokemones")
        print("3. Comenzar juego")
        print("4. Salir")
        
        select = numberInput("\Elije una de las 4 opciones: ")
        
        match select: 
            
            case 3: 
                
                jugador_1 = stringInput("Nombre del jugador 1: ")
                jugador_2 = stringInput("Nombre del jugador 2: ")
                
                jugadores = [jugador_1, jugador_2]
                
                print("El primero en comenzar el duelo es... ")
                
                random_choice = random.choice(jugadores)
                
                
                
                print("!Que comience el duelo!")
                
                while True: 
                    
                    print(
                        """\nAcciones:
            1. Atacar
            2. Defenderse
            3. Descansar"""
                    )
                    
                jugador_1 = numberInput()