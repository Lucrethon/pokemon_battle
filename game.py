import random
import os
import game_logic as g
import functions as f
import utils as u
import models as m



def run_game():

    player1, player2 = g.initial_setup()

    print("\n!Que comience el duelo!")

    # Elegir primer pokemon de batalla
    # Utilizar atributo de clase PokemonTrainer


    # g.elegir_pokemon(jugador1, pokemon_en_juego1)
    # g.elegir_pokemon(jugador2, pokemon_en_juego2)

    while True:
        if player1.is_first_player:
            print(f"\nTurno de {player1.name}:")
            # turno(jugador_1)
        else:
            print(f"\nTurno de {player2.name}:")
            # turno(jugador_2)

        os.system("clear")
