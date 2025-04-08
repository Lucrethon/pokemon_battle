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


def desplegar_lista(lista):
    for indice, elemento in enumerate(lista, start=1):
        print(f"{indice}: {elemento}")
