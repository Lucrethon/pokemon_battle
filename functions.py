import models as p_class

def numberInput(message):

    while True:

        try:
            var = int(input(message))

            break
        except ValueError as error:
            print(
                "\nHas introducido un caracter invalido. Por favor intentalo de nuevo"
            )
            print(error)
    return var


def stringInput(message):

    try:
        var = str(input(message))
    except ValueError as error:
        print("\nHas introducido un caracter invalido. Por favor intentalo de nuevo")
        print(error)
    return var

def turno():
                        
    print("1. Atacar")
    print("2. Defenderse")
    print("3. Descansar")
                    
    select = numberInput("\nElige tu accion: ")
                    
    match select: 
                        
        case 1: 
            print("\nAtaque")
            
            #seleccionar ataque
            
            
            #comprobar energia
            if p_class.energy_check():
                p_class.attack()
            else:
                print("No hay suficiente energia para realizar este ataque")
                        
        case 2: 
            print("\nDefender")
            
            p_class.defend()
                            
        case 3:
            print("\nDescansar")
            
            p_class.rest()
            
        case _:
                print("\nOpcion no valida. Por favor intente de nuevo")
        
    return select

def desplegar_lista(lista):
    for indice, elemento in enumerate(lista, start=1):
        print(f"{indice}: {elemento}")


        
def elegir_equipo(jugador_1, jugador_2, lista_pokemon): 
    
    equipo_jugador1 = []
    equipo_jugador2 = []
    
    while True: 
        
        print("\nLista de pokemones disponibles:")
        desplegar_lista(lista_pokemon)
        
        while True:
            
            select1 = numberInput(f"\n{jugador_1}, elige un Pokémon de la lista: ")
            
            if 0 <= select1 - 1 < len(lista_pokemon):
                pokemon = lista_pokemon.pop(select1 - 1)
                equipo_jugador1.append(pokemon)
                
                print(f"\nEquipo Pokemon de {jugador_1}")
                desplegar_lista(equipo_jugador1)
                break  
            
            else: 
                print("Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo.")

        print("\nLista de pokemones disponibles:")
        desplegar_lista(lista_pokemon)
        
        while True:
            
            select2 = numberInput(f"\n{jugador_2}, elige un Pokémon de la lista: ")
            
            if 0 <= select2 - 1 < len(lista_pokemon):
                pokemon = lista_pokemon.pop(select2 - 1)
                equipo_jugador2.append(pokemon)
                
                print(f"\nEquipo Pokemon de {jugador_2}")
                desplegar_lista(equipo_jugador2)
                break  
            
            else: 
                print("Ese número no se encuentra en la lista. Por favor, inténtalo de nuevo.")

        if len(equipo_jugador1) == 2 and len(equipo_jugador2) == 2:
            break
        
    return equipo_jugador1, equipo_jugador2