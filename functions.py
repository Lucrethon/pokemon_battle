import models
import random


def create_attack_objects(attack_dicctionary): # Crear objetos Attack

    attack_list = []

    for attack in attack_dicctionary:

        attack = models.Attack(
            attack.get("nombre"),
            attack.get("descripcion"),
            attack.get("costo_energia"),
            attack.get("probabilidad_exito") / 100,
            attack.get("puntos_daño"),
            (attack.get("efecto_elemental")).lower(),
            attack.get("efecto_especial"),
        )

        attack_list.append(attack)

    return attack_list



def create_pokemon_objects(pokemon_json): # Crear objetos Pokemon

    pokemon_list = []

    for dictionary in pokemon_json:

        pokemon = models.Pokemon(
            dictionary.get("nombre"),
            (dictionary.get("tipo")).lower(),
            dictionary.get("puntos_vida"),
            dictionary.get("probabilidad_critico") / 100,
            dictionary.get("bonificacion_critico") / 100,
            create_attack_objects(dictionary.get("ataques")),
        )

        pokemon_list.append(pokemon)

    return pokemon_list


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
