import utils as u
import models
import os
import random
import models as m
import json
import functions as f
from pathlib import Path


# importar Json

file_path = Path(__file__).parent / "pokemon_list.json"

with open(file_path, mode="r") as file:
    pokemons = json.load(file)

pokemon_list = f.create_pokemon_objects(pokemons)

# turnos


def turno(player: models.PokemonTrainer):

    print("1. Atacar")
    print("2. Defenderse")
    print("3. Descansar")

    select = u.numberInput("\nElige tu accion: ")

    match select:

        case 1:
            print("\nAtaque")

            # seleccionar ataque
            # comprobar energia
            # atacar

        case 2:
            print("\nDefender")

            # defenderse

        case 3:
            print("\nDescansar")

            # descansar

        case _:
            print("\nOpcion no valida. Por favor intente de nuevo")

    return select


# Elegir equipo


def choose_pokemon_team(
    player1, player2, pokemon_list
):
    
    team_player1 = []
    team_player2 = []

    pokemons_per_player = 3
    shifts = pokemons_per_player * 2
    counter = 1

    name_current_shift = player1
    team_current_shift = team_player1

    while counter <= shifts:

        print("\nLista de pokemones disponibles:")
        u.desplegar_lista(pokemon_list)

        while True:

            select1 = u.numberInput(f"\n{name_current_shift}, elige un Pokémon de la lista: ")

            if 0 <= select1 - 1 < len(pokemon_list):
                pokemon = pokemon_list.pop(select1 - 1)
                team_current_shift.append(pokemon)

                print(f"\nEquipo Pokemon de {name_current_shift}")
                u.desplegar_lista(team_current_shift)
                break

            else:
                print(
                    "Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo."
                )

        # if-else  compacto: valor_si_verdadero if condicion else valor_si_falso
        name_current_shift = player2 if name_current_shift == player1 else player1
        team_current_shift = (
            team_player2
            if team_current_shift == team_player1
            else team_player1
        )
        counter += 1

    return team_player1, team_player2


def choose_pokemon(player: models.PokemonTrainer, pokemon_en_juego):
    while True:

        u.desplegar_lista(player.pokemon_team)
        seleccion = u.numberInput("Elige tu siguiente pokemon:")

        if 0 <= seleccion - 1 < len(player.pokemon_team):
            pokemon_en_juego = jugador.pokemon_team[seleccion]
            print(f"\n<{jugador.name} ha elegido a {pokemon_en_juego.name}!")
            return pokemon_en_juego

        else:
            print("Ese numero no esta en tu lista. Intentalo de nuevo")


def initial_setup():
    
    os.system("clear")
    name_1 = u.stringInput("Nombre del jugador 1: ")
    name_2 = u.stringInput("Nombre del jugador 2: ")

    players = [name_1, name_2]

    print("\nEl primero en comenzar elegir su equipo Pokemon es... ")

    name_1st_shift = random.choice(players)
    print(f"\n¡{name_1st_shift}!")

    # variable = valor_si_verdadero if condición else valor_si_falso
    name_2nd_shift = players[0] if name_1st_shift == players[1] else players[1]

    # Elegir equipos

    team_player1, team_player2 = choose_pokemon_team(
        name_1st_shift, name_2nd_shift, pokemon_list
    )

    player1 = m.PokemonTrainer(name_1st_shift, team_player1)
    player2 = m.PokemonTrainer(name_2nd_shift, team_player2)
    player1.is_first_player = True
    
    return player1, player2