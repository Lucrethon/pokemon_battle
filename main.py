import os
import utils as u
import game
import json
from pathlib import Path
import functions as f


def init_app():
    
    file_path = Path(__file__).parent / "pokemon_list.json"

    with open(file_path, mode="r") as file:
        pokemons = json.load(file)

    pokemon_list = f.create_pokemon_objects(pokemons)
    
    return pokemon_list


def main_menu():

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
                game.run_game()

            case 4:
                print("¡Vuelve pronto para otro combate pokemon!")
                break

            case _:
                print("\nOpcion no valida. Por favor intente de nuevo")


if __name__ == "__main__":
    init_app()
    main_menu()
