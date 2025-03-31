import pokemon_class as p_class
import random
import os
import functions as f

def pokemon_duel(): 
    
    while True: 
        
        print("\nBienvenido a Pokemon Duel. Elije una opcion:")
        print("1. Descripcion del juego")
        print("2. Lista de Pokemones")
        print("3. Comenzar juego")
        print("4. Salir")
        
        select = f.numberInput("\nElije una de las 4 opciones: ")
        
        match select: 
            
            case 1: 
                print("Descripcion del juego")
                
            
            case 2:
                print("Depliegue lista de pokemones existentes")
            
            case 3: 
                
                os.system('clear')
                jugador_1 = f.stringInput("Nombre del jugador 1: ")
                jugador_2 = f.stringInput("Nombre del jugador 2: ")
                
                jugadores = [jugador_1, jugador_2]
                
                print("\nEl primero en comenzar el duelo es... ")
                
                primer_turno = random.choice(jugadores)
                print(f"\n¡{primer_turno}!")
                
                #variable = valor_si_verdadero if condición else valor_si_falso
                segundo_turno = jugadores[0] if primer_turno == jugadores[1] else jugadores[1]
                
                #Elegir equipos 
                
                f.elegir_equipo(primer_turno, segundo_turno, p_class.lista_pokemon)
                
                print("\n!Que comience el duelo!")
                
                while True: 
                    
                    print(f"\nTurno de {primer_turno}:")
                    
                    f.turno()
                    
                    print(f"\nTurno de {segundo_turno}:")
                    
                    f.turno()
                    
                    os.system('clear')
            
            case 4:
                print("¡Vuelve pronto para otro combate pokemon!")
                break
            
            case _:
                print("\nOpcion no valida. Por favor intente de nuevo")
                



if __name__ == "__main__":
    pokemon_duel()