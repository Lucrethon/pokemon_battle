import random
import os
import game_logic as g
import functions as f
import utils as u
import models as m


def run_game():

    os.system("clear")

    player1, player2 = g.initial_setup()

    turn_counter = 1

    print("\n!Que comience el duelo!")

    # Elegir primer pokemon de batalla utilizando atributo de clase PokemonTrainer
    
    os.system("clear")
    g.choose_pokemon(player1)
    pause = input()
    os.system("clear")
    g.choose_pokemon(player2)

    while len(player1.pokemon_team) > 0 and len(player2.pokemon_team) > 0:
        # si se utilizara or en vez de and aqui, seria incorrecto porque seria "sigue el juego mientras al menos uno de los jugadores tenga Pokémon"
        # si uno de los dos ya perdió, el juego seguiría ejecutando turnos innecesariamente.
        # Lo correcto sería que el juego continúe mientras ambos tengan Pokémon disponibles
        
        
        if len(player1.pokemon_team) == 0 or len(player2.pokemon_team) == 0:
            break  # sale del bucle inmediatamente si ya no hay Pokémon disponibles

        print(f"\nTurno No.{turn_counter}")
        
        if turn_counter % 2 != 0:
            print(f"\nTurno de {player1.name}:")
            g.turn(player1, player2.current_pokemon)
            player2.set_defeated_pokemon_list()
        else:
            print(f"\nTurno de {player2.name}:")
            g.turn(player2, player1.current_pokemon)
            player1.set_defeated_pokemon_list()
        
        turn_counter += 1

        pause = input()
        os.system("clear")

    winner = player1.name if len(player1.pokemon_team) > 0 else player2.name
    print(f"\nEl duelo ha terminado. El ganador es {winner}!")
    return winner
