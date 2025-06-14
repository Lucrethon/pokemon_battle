import utils as u
import models
import os
import random
import main


def execute_attack(player: models.PokemonTrainer, oposing_pokemon: models.Pokemon, attack: models.Attack): #ejecutar ataque

        print(
            f"\n{player.current_pokemon.name} va a realizar {attack.name}"
        )
        player.current_pokemon.attack(
            oposing_pokemon, attack
        )  # atacar

        if oposing_pokemon.is_defeated():
            print(
                f"\n{player.current_pokemon.name} ha derrotado a {oposing_pokemon.name}"
            ) #comprobar pokemon derrotado
        else:
            None


def attack_flow(player: models.PokemonTrainer, oposing_pokemon: models.Pokemon): #flujo de ataque
    
    while True:
        # elegir ataque
        u.desplegar_lista(player.current_pokemon.attacks)
        print(f"\n{len(player.current_pokemon.attacks)+1}: Salir al menu principal.")

        select_attack = u.numberInput(
            "\nSelecciona el ataque que quieres realizar: ")
        
        if select_attack == len(player.current_pokemon.attacks)+1:
            return False
        
        if select_attack > 0 and select_attack <= len(player.current_pokemon.attacks):
            
            current_attack = player.current_pokemon.attacks[select_attack - 1]
            
            if player.current_pokemon.has_enough_energy(current_attack):  # comprobrar energia
                
                execute_attack(player, oposing_pokemon, current_attack)
                return True
            
            else:
                print("No tienes suficiente energia para realizar este ataque. Por favor elige otro")
        
        else:
            print("Por favor introduce una opcion valida")



def turn(player: models.PokemonTrainer, oposing_pokemon: models.Pokemon): #flujo de turnos

    # generador: x for x in lista if x == valor (Produce los valores uno a uno)(iterador)
    # next sintaxis: next(iterador, valor_por_defecto) --> Devuelve el siguiente elemento del iterador
    # current_pokemon = next((pokemon for pokemon in player.pokemon_team if pokemon.name == player.current_pokemon))
    # bueno saberlo para que con una caracteristica de un objeto, puedo "traer" el objeto completo

    if player.current_pokemon.is_defeated():
        print(
            f"\n{player.current_pokemon.name} ha sido derrotado. Por favor elige tu siguiente pokemon: "
        )
        choose_pokemon(player)
        print(f"\n¡{player.name} ha elegido a {player.current_pokemon.name}!")
    else:
        None

    while True: #menu principal de turno
        
        print(f"\n{player.current_pokemon.name} tiene {player.current_pokemon.energy_points} puntos de energia.")
        print(f"{player.current_pokemon.name} tiene {player.current_pokemon.HP} puntos de vida.")

        print("\n1. Atacar")
        print("2. Defenderse")
        print("3. Descansar")
        print("4. Cambiar de pokemon")

        select = u.numberInput("\nElige tu accion: ")

        match select:

            case 1: #atacar 
                if attack_flow(player, oposing_pokemon): #si se ejecuto el atauqe
                    break
                else: 
                    continue
                

            case 2: #defenderse
                player.current_pokemon.defend()
                print(f"\n{player.current_pokemon.name} se esta defendiendo.")
                break

            case 3: #descansar
                player.current_pokemon.rest()
                print(f"\n{player.current_pokemon.name} esta descansando.")
                break

            case 4: #elegir pokemon
                choose_pokemon(player)
                print(
                    f"\n{player.name} ha cambiado a {player.current_pokemon.name}"
                )
                break

            case _:
                print("\nOpcion no valida. Por favor intente de nuevo")



def choose_pokemon_team(player1, player2, pokemon_list): #Elegir equipo pokemon

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

            select1 = u.numberInput(
                f"\n{name_current_turn}, elige un Pokémon de la lista: "
            )

            if 0 <= select1 - 1 < len(pokemon_list):
                pokemon = pokemon_list.pop(select1 - 1)
                team_current_turn.append(pokemon)

                print(f"\nEquipo Pokemon de {name_current_turn}")
                u.desplegar_lista(team_current_turn)
                pause = input()
                os.system("clear")
                break

            else:
                print(
                    "Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo."
                )

        # if-else  compacto: valor_si_verdadero if condicion else valor_si_falso
        name_current_turn = player2 if name_current_turn == player1 else player1
        team_current_turn = (
            team_player2 if team_current_turn == team_player1 else team_player1
        )
        counter += 1

    os.system("clear")

    return team_player1, team_player2



def choose_pokemon(player: models.PokemonTrainer): #Elegir pokemon a usar
    while True:

        print(f"\nEquipo de {player.name}:")
        u.desplegar_lista(player.pokemon_team)
        seleccion = u.numberInput(f"\n{player.name}, elige tu siguiente pokemon: ")

        if 0 <= seleccion - 1 < len(player.pokemon_team):
            player_current_pokemon = player.pokemon_team[seleccion - 1]
            player.current_pokemon = player_current_pokemon
            break

        else:
            print("Ese numero no esta en tu lista. Intentalo de nuevo")


def initial_setup(): #Crear objetos PokemonTrainer (jugadores)

    u.clear()
    name_1 = u.stringInput("Nombre del jugador 1: ")
    name_2 = u.stringInput("Nombre del jugador 2: ")

    players = [name_1, name_2]

    print("\nEl primer turno es de... ")

    name_1st_turn = random.choice(players)
    print(f"\n¡{name_1st_turn}!")
    u.standby()

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
