import models

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