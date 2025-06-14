import os
import utils as u
import game
import json
from pathlib import Path
import functions as f
from game_description import show_game_description
from rich.console import Console





def init_app():

    file_path = Path(__file__).parent / "pokemon_list_test.json"

    with open(file_path, mode="r") as file:
        pokemons = json.load(file)

    pokemon_list = f.create_pokemon_objects(pokemons)

    return pokemon_list





def main_menu():

    u.clear()

    while True:
        
        #console = Console(width=os.get_terminal_size())
                
        terminal_size = os.get_terminal_size()
        console = Console(width=terminal_size.columns, height=terminal_size.lines)
        
        u.lines((terminal_size.lines // 2) - 6)
        
        style = "bold white"
        
        console.print("██████╗  ██████╗ ██╗  ██╗███████╗███╗   ███╗ ██████╗ ███╗   ██╗    ██████╗ ██╗   ██╗███████╗██╗", style=style, justify="center")
        console.print("██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗ ████║██╔═══██╗████╗  ██║    ██╔══██╗██║   ██║██╔════╝██║", style=style, justify="center")     
        console.print("██████╔╝██║   ██║█████╔╝ █████╗  ██╔████╔██║██║   ██║██╔██╗ ██║    ██║  ██║██║   ██║█████╗  ██║", style=style, justify="center")    
        console.print("██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║    ██║  ██║██║   ██║██╔══╝  ██║", style=style, justify="center")   
        console.print("    ██║     ╚██████╔╝██║  ██╗███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    ██████╔╝╚██████╔╝███████╗███████╗  ", style=style,justify="center")
        console.print("    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝  ", style=style,justify="center")
        
        u.lines(3)

        console.print("\n¡Bienvenido a Pokemon Duel! Elije una opcion:", style=style, justify="center")
        
        u.lines(2)
        
        console.print("1. Descripcion del juego", style=style, justify="center")
        console.print("2. Lista de Pokemones", style=style, justify="center")
        console.print("3. Comenzar juego", style=style, justify="center")
        console.print("4. Salir", style=style, justify="center")

        select = u.numberInput("\nElije una de las 4 opciones: ")

        match select:

            case 1:
                print("Descripcion del juego")
                show_game_description()
                u.standby()
                u.clear()
                

            case 2:
                print("Pokemones existentes")
                pokemon_list = init_app()
                u.desplegar_lista(pokemon_list)
                u.standby()

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
