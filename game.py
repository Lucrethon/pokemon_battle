import random
import os
import game_logic as g
import functions as f
import utils as u
import models as m



def run_game():

    player1, player2 = g.initial_setup()

    print("\n!Que comience el duelo!")

    # Elegir primer pokemon de batalla utilizando atributo de clase PokemonTrainer

    g.choose_pokemon(player1)
    g.choose_pokemon(player2)
    

    while True:
        if player1.is_first_player:
            print(f"\nTurno de {player1.name}:")
            g.turn(player1)
        else:
            print(f"\nTurno de {player2.name}:")
            g.turn(player2)

        os.system("clear")
