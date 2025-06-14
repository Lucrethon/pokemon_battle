import os

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


def standby():
    pause = input("\nPresiona enter para continuar.")
    print(pause)


def clear():
    os.system("clear")

#colocar numero determinado de espacios 
def esp(space_number):
	if space_number <= 0:
		space_numner = 0
	if type(space_numner) == float:
		space_number = round(space_number)
	for i in range(space_number):
		print(" ", end="")
  
def lines(n): 
	for i in range(n): print("")




