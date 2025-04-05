import models
import random
import os
import game_logic as g
import utils as u
import functions as f
import json
from pathlib import Path
    
    # importar Json

ruta_archivo = Path(__file__).parent / "pokemon_list.json"

with open(ruta_archivo, mode="r") as file:
    pokemons = json.load(file)
        
lista_pokemon = f.crear_objetos_pokemon(pokemons)
    




def pokemon_duel():

    while True:

        print("\nBienvenido a Pokemon Duel. Elije una opcion:")
        print("1. Descripcion del juego")
        print("2. Lista de Pokemones")
        print("3. Comenzar juego")
        print("4. Salir")

        select = u.numberInput("\nElije una de las 4 opciones: ")

        match select:

            case 1:
                print("Descripcion del juego")

            case 2:
                print("Depliegue lista de pokemones existentes")

            case 3:

                os.system("clear")
                nombre_jugador_1 = u.stringInput("Nombre del jugador 1: ")
                nombre_jugador_2 = u.stringInput("Nombre del jugador 2: ")

                jugadores = [nombre_jugador_1, nombre_jugador_2]

                print("\nEl primero en comenzar elegir sus pokemones es... ")

                primer_turno = random.choice(jugadores)
                print(f"\n¡{primer_turno}!")

                # variable = valor_si_verdadero if condición else valor_si_falso
                segundo_turno = (
                    jugadores[0] if primer_turno == jugadores[1] else jugadores[1]
                )

                # Elegir equipos

                g.elegir_equipo(primer_turno, segundo_turno, lista_pokemon)

                print("\n!Que comience el duelo!")

                while True:

                    print(f"\nTurno de {primer_turno}:")

                    f.turno()

                    print(f"\nTurno de {segundo_turno}:")

                    f.turno()

                    os.system("clear")

            case 4:
                print("¡Vuelve pronto para otro combate pokemon!")
                break

            case _:
                print("\nOpcion no valida. Por favor intente de nuevo")


if __name__ == "__main__":
    #init_app()
    pokemon_duel()
