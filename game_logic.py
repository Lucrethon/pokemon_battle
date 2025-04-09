import utils as u
import models
import os
import random
import main

# turnos


def turn(player: models.PokemonTrainer, oposing_pokemon: models.Pokemon):
    
    while True:
        
        #generador: x for x in lista if x == valor (Produce los valores uno a uno)(iterador)
        #next sintaxis: next(iterador, valor_por_defecto) --> Devuelve el siguiente elemento del iterador
        current_pokemon = next((pokemon for pokemon in player.pokemon_team if pokemon.name == player.current_pokemon))

        print("1. Atacar")
        print("2. Defenderse")
        print("3. Descansar")
        print("4. Cambiar de pokemon")

        select = u.numberInput("\nElige tu accion: ")

        match select:

            case 1:
                print(f"\n{current_pokemon.name} tiene {current_pokemon.energy_points} puntos de energia.")
                
                #elegir ataque
                u.desplegar_lista(current_pokemon.attacks)
                select_attack = u.numberInput("\nSelecciona el ataque que quieres realizar:")
                
                if 0 <= select_attack - 1 < len(current_pokemon.attacks):
                    current_attack = current_pokemon.attacks[select_attack-1]
                    if current_pokemon.has_enough_energy(current_attack): #comprobrar energia
                        current_pokemon.attack(oposing_pokemon, current_attack) #atacar
                    
                    else:
                        print("No tienes suficiente energia para realizar este ataque. Por favor elige otro")

            case 2:
                current_pokemon.defend()
                print(f"\n{current_pokemon.name} se esta defendiendo.")
                break

            case 3:               
                a, b = current_pokemon.rest()
                print(f"\n{current_pokemon.name} esta descansando.")
                break

                # descansar
            
            case 4: 
                choose_pokemon(player)
                break

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
    turns = pokemons_per_player * 2
    counter = 1

    name_current_turn = player1
    team_current_turn = team_player1

    while counter <= turns:

        print("\nLista de pokemones disponibles:")
        u.desplegar_lista(pokemon_list)

        while True:

            select1 = u.numberInput(f"\n{name_current_turn}, elige un Pokémon de la lista: ")

            if 0 <= select1 - 1 < len(pokemon_list):
                pokemon = pokemon_list.pop(select1 - 1)
                team_current_turn.append(pokemon)

                print(f"\nEquipo Pokemon de {name_current_turn}")
                u.desplegar_lista(team_current_turn)
                break

            else:
                print(
                    "Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo."
                )

        # if-else  compacto: valor_si_verdadero if condicion else valor_si_falso
        name_current_turn = player2 if name_current_turn == player1 else player1
        team_current_turn = (
            team_player2
            if team_current_turn == team_player1
            else team_player1
        )
        counter += 1

    return team_player1, team_player2


def choose_pokemon(player: models.PokemonTrainer):
    while True:

        u.desplegar_lista(player.pokemon_team)
        seleccion = u.numberInput(f"\n{player.name}, elige tu siguiente pokemon:")

        if 0 <= seleccion - 1 < len(player.pokemon_team):
            current_pokemon = player.pokemon_team[seleccion-1]
            player.current_pokemon = current_pokemon.name
            print(f"\n<{player.name} ha elegido a {current_pokemon.name}!")
            return player

        else:
            print("Ese numero no esta en tu lista. Intentalo de nuevo")


def initial_setup():
    
    os.system("clear")
    name_1 = u.stringInput("Nombre del jugador 1: ")
    name_2 = u.stringInput("Nombre del jugador 2: ")

    players = [name_1, name_2]

    print("\nEl primero en comenzar elegir su equipo Pokemon es... ")

    name_1st_turn = random.choice(players)
    print(f"\n¡{name_1st_turn}!")

    # variable = valor_si_verdadero if condición else valor_si_falso
    name_2nd_turn = players[0] if name_1st_turn == players[1] else players[1]

    # Elegir equipos

    team_player1, team_player2 = choose_pokemon_team(
        name_1st_turn, name_2nd_turn, main.init_app()
    )

    player1 = models.PokemonTrainer(name_1st_turn, team_player1)
    player2 = models.PokemonTrainer(name_2nd_turn, team_player2)
    player1.is_first_player = True
    
    return player1, player2

