import models
import random

#Crear objetos Attack

def crear_ataques(lista_ataques):

    objetos_creados = []

    for ataque in lista_ataques:

        ataque = models.Attack(
            ataque.get("nombre"),
            ataque.get("descripcion"),
            ataque.get("costo_energia"),
            ataque.get("probabilidad_exito") / 100,
            ataque.get("puntos_daño"),
            (ataque.get("efecto_elemental")).lower(),
            ataque.get("efecto_especial"),
        )

        objetos_creados.append(ataque)

    return objetos_creados


# Crear objetos Pokemon


def crear_objetos_pokemon(lista_pokemon):

    objetos_creados = []

    for diccionario in lista_pokemon:

        pokemon = models.Pokemon(
            diccionario.get("nombre"),
            (diccionario.get("tipo")).lower(),
            diccionario.get("puntos_vida"),
            diccionario.get("probabilidad_critico") / 100,
            diccionario.get("bonificacion_critico") / 100,
            crear_ataques(diccionario.get("ataques")),
        )

        objetos_creados.append(pokemon)

    return objetos_creados


# Logica para:
# Dentro de un array A con diccionarios, cada diccionario tiene una llave que tiene como valor un array B,
# y dentro de ese array B hay otros diccionarios.
# Como accedo a las llaves de los diccionarios que estan dentro del array B con .get()?


# def crear_ataques(lista_pokemon):

#     objetos_creados = []

#     for pokemon in lista_pokemon:

#         ataques = pokemon.get("ataques", [])

#         for objeto in ataques:

#             ataque = Attack(objeto.get("nombre"),
#                             objeto.get("descripcion"),
#                             objeto.get("costo_energia"),
#                             objeto.get("probabilidad_exito")/100,
#                             objeto.get("puntos_daño"),
#                             objeto.get("efecto_elemental".lower()),
#                             objeto.get("efecto_especial")
#                             )

#             objetos_creados.append(ataque)

#     return objetos_creados

def is_first_player(jugador1 : models.PokemonTrainer, jugador2: models.PokemonTrainer):
    
    jugadores = [jugador1, jugador2]
    
    primer_turno = random.choice(jugadores)
    primer_turno.is_first_player = True

    return primer_turno, primer_turno.is_first_player