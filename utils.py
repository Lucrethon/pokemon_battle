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

    var = input(message)

    return var


def desplegar_lista(lista):
    for indice, elemento in enumerate(lista, start=1):
        print(f"{indice}: {elemento}")


# def select_element(list, select):
    
#     if select > 0 and select <= len(list):
#         return list[select - 1]
    
#     raise IndexError(f"Índice de selección inválido: {select}.")

