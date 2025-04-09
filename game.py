import random
import os
import game_logic as g
import functions as f
import utils as u
import models as m



def run_game():
    
    os.system("clear")

    player1, player2 = g.initial_setup()

    print("\n!Que comience el duelo!")

    # Elegir primer pokemon de batalla utilizando atributo de clase PokemonTrainer

    current_pokemon_player1 = g.choose_pokemon(player1)
    current_pokemon_player2 =g.choose_pokemon(player2)
    

    while len(player1.defeated_pokemon) == 3 or len(player1.defeated_pokemon) == 3:
        
        if player1.is_first_player:
            print(f"\nTurno de {player1.name}:")
            g.turn(player1, current_pokemon_player2)
        else:
            print(f"\nTurno de {player2.name}:")
            g.turn(player2, current_pokemon_player1)

        os.system("clear")
        
    winner = player1.name if len(player1.pokemon_team) == 0 else player2.name
    
    print(f"\nEl duelo ha terminado. El ganador es {winner}!")
