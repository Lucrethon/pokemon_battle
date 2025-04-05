import random 
import os
import game_logic as g
import functions as f
import utils as u
import json
from pathlib import Path
    
# importar Json

ruta_archivo = Path(__file__).parent / "pokemon_list.json"

with open(ruta_archivo, mode="r") as file:
    pokemons = json.load(file)
        
lista_pokemon = f.crear_objetos_pokemon(pokemons)


def run_game():
    
    os.system("clear")
    nombre_jugador_1 = u.stringInput("Nombre del jugador 1: ")
    nombre_jugador_2 = u.stringInput("Nombre del jugador 2: ")

    jugadores = [nombre_jugador_1, nombre_jugador_2]

    print("\nEl primero en comenzar elegir sus pokemones es... ")

    primer_turno = random.choice(jugadores)
    print(f"\n¡{primer_turno}!")

    # variable = valor_si_verdadero if condición else valor_si_falso
    segundo_turno = (jugadores[0] if primer_turno == jugadores[1] else jugadores[1]
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