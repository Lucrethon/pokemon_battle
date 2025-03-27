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
            
            case 1: 
                print("Descripcion del juego")
                
            
            case 2:
                print("Depliegue lista de pokemones existentes")
            
            case 3: 
                
                jugador_1 = stringInput("Nombre del jugador 1: ")
                jugador_2 = stringInput("Nombre del jugador 2: ")
                
                jugadores = [jugador_1, jugador_2]
                
                print("\nEl primero en comenzar el duelo es... ")
                
                primer_turno = random.choice(jugadores)
                print(primer_turno)
                
                #valor_si_verdadero if condición else valor_si_falso
                segundo_turno = jugadores[0] if primer_turno == jugadores[1] else jugadores[1]
                
                print("!Que comience el duelo!")
                
                while True: 
                    
                    print(primer_turno)
                    
                    select = numberInput(
                        """\n1. Atacar
                            2. Defenderse
                            3. Descansar
            
                            Elige tu accion: """
                    )
                    
                    match select: 
                        
                        case 1: 
                            print("Ataque")
                        
                        case 2: 
                            print("Defender")
                            
                        case 3:
                            print("Descansar")
                    
                    print(segundo_turno)
                    
                    select = numberInput(
                        """\n1. Atacar
                            2. Defenderse
                            3. Descansar
            
                            Elige tu accion: """
                    )
                    
                    match select: 
                        
                        case 1: 
                            print("Ataque")
                        
                        case 2: 
                            print("Defender")
                            
                        case 3:
                            print("Descansar")
            
            case 4:
                print("¡Vuelve pronto para otro combate pokemon!")
                break
            
            case _:
                print("\nOpcion no valida. Por favor intente de nuevo")
