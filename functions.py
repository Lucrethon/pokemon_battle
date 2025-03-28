import pokemon_class as p_class

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
            
            #comprobar energia
            if p_class.energy_check():
                p_class.attack()
            else:
                print("No hay suficiente energia para realizar este ataque")
                        
        case 2: 
            print("\nDefender")
            
                            
        case 3:
            print("\nDescansar")
        
    return select