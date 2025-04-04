import utils as u
import models

#turnos

def turno():

    print("1. Atacar")
    print("2. Defenderse")
    print("3. Descansar")

    select = u.numberInput("\nElige tu accion: ")

    match select:

        case 1:
            print("\nAtaque")

            # seleccionar ataque

            # comprobar energia
            #atacar

        case 2:
            print("\nDefender")

            #defenderse

        case 3:
            print("\nDescansar")

            #descansar

        case _:
            print("\nOpcion no valida. Por favor intente de nuevo")

    return select

#Elegir equipo

def elegir_equipo(jugador_1, jugador_2, lista_pokemon):

    equipo_jugador1 = []
    equipo_jugador2 = []

    while True:

        print("\nLista de pokemones disponibles:")
        u.desplegar_lista(lista_pokemon)

        while True:

            select1 = u.numberInput(f"\n{jugador_1}, elige un Pokémon de la lista: ")

            if 0 <= select1 - 1 < len(lista_pokemon):
                pokemon = lista_pokemon.pop(select1 - 1)
                equipo_jugador1.append(pokemon)

                print(f"\nEquipo Pokemon de {jugador_1}")
                u.desplegar_lista(equipo_jugador1)
                break

            else:
                print(
                    "Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo."
                )

        print("\nLista de pokemones disponibles:")
        u.desplegar_lista(lista_pokemon)

        while True:

            select2 = u.numberInput(f"\n{jugador_2}, elige un Pokémon de la lista: ")

            if 0 <= select2 - 1 < len(lista_pokemon):
                pokemon = lista_pokemon.pop(select2 - 1)
                equipo_jugador2.append(pokemon)

                print(f"\nEquipo Pokemon de {jugador_2}")
                u.desplegar_lista(equipo_jugador2)
                break

            else:
                print(
                    "Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo."
                )

        if len(equipo_jugador1) == 2 and len(equipo_jugador2) == 2:
            break

    return equipo_jugador1, equipo_jugador2
