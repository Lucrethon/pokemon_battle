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
    
    pokemones_por_jugador = 3
    turnos = pokemones_por_jugador * 2
    contador = 1
    
    turno_actual = jugador_1
    equipo_turno_actual = equipo_jugador1


    while contador <= turnos:

        print("\nLista de pokemones disponibles:")
        u.desplegar_lista(lista_pokemon)

        while True:

            select1 = u.numberInput(f"\n{turno_actual}, elige un Pokémon de la lista: ")

            if 0 <= select1 - 1 < len(lista_pokemon):
                pokemon = lista_pokemon.pop(select1 - 1)
                equipo_turno_actual.append(pokemon)

                print(f"\nEquipo Pokemon de {turno_actual}")
                u.desplegar_lista(equipo_turno_actual)
                break

            else:
                print(
                    "Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo."
                )
        
        #if-else  compacto: valor_si_verdadero if condicion else valor_si_falso
        turno_actual = jugador_2 if turno_actual == jugador_1 else jugador_1
        equipo_turno_actual = equipo_jugador2 if equipo_turno_actual == equipo_jugador1 else equipo_jugador1
        contador += 1

    return equipo_jugador1, equipo_jugador2
