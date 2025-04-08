import random
import os
import game_logic as g
import functions as f
import utils as u
import models as m
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

    print("\nEl primero en comenzar elegir su equipo Pokemon es... ")

    primer_turno = random.choice(jugadores)
    print(f"\n¡{primer_turno}!")

    # variable = valor_si_verdadero if condición else valor_si_falso
    segundo_turno = jugadores[0] if primer_turno == jugadores[1] else jugadores[1]

    # Elegir equipos

    equipo_jugador1 = []
    equipo_jugador2 = []

    g.elegir_equipo(
        primer_turno, segundo_turno, equipo_jugador1, equipo_jugador2, lista_pokemon
    )

    jugador1 = m.PokemonTrainer(primer_turno, equipo_jugador1)
    jugador2 = m.PokemonTrainer(segundo_turno, equipo_jugador2)
    jugador1.is_first_player = True

    print("\n!Que comience el duelo!")

    # Elegir primer pokemon de batalla
    # Utilizar atributo de clase PokemonTrainer

    pokemon_en_juego1 = random.choice(jugador1.pokemon_team)
    pokemon_en_juego2 = random.choice(jugador2.pokemon_team)

    g.elegir_pokemon(jugador1, pokemon_en_juego1)
    g.elegir_pokemon(jugador2, pokemon_en_juego2)

    while True:
        if jugador1.is_first_player:
            print(f"\nTurno de {primer_turno}:")
            # turno(jugador_1)
        else:
            print(f"\nTurno de {segundo_turno}:")
            # turno(jugador_2)

        os.system("clear")
