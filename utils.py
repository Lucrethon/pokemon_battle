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


# def is_between_number(select, list):

#         if select-1 > 0 and select-1 <= len(list):
#             True
#         else:
#             print("Por favor introduce una opcion valida")
