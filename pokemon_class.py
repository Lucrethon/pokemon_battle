import random

class Pokemon:

    def __init__(self, name, element, HP, crit_rate, crit_damage):
        self.name = name
        self.element = element
        self.HP = HP
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.energy_points = 10
        self.attacks = []
        self.defend = False
        
    
    def __repr__(self):
        return (f"\nNombre: {self.name} \nElemento: {self.element} \nPuntos de vida: {self.HP} \nProbabilidad de ataque critico: {self.crit_rate} \nBonificador de ataque critico: {self.crit_damage}")

    elemental_bonus = {
        "fuego": {"planta": 0.2, "agua": 0, "fuego": 0, "neutral": 0},
        "agua": {"planta": 0, "agua": 0, "fuego": 0.2, "neutral": 0},
        "planta": {"planta": 0, "agua": 0.2, "fuego": 0, "neutral": 0},
        "neutral": {"planta": 0, "agua": 0, "fuego": 0, "neutral": 0},
    }


def elemental_bonus(attacking_pokemon: Pokemon, defender_pokemon: Pokemon): 
    
    if defender_pokemon.defend == False: 
        bonus_elemental = Pokemon.elemental_bonus.get(attacking_pokemon.element, {}).get(defender_pokemon.element)
        return bonus_elemental
    
    else:
        return 0
    
def crit_damage(crit_damage, crit_rate):
    
    value = random.random(0, 1)
    
    if value <= crit_rate:
        return crit_damage
    else:
        return 0
    


def energy_check(pokemon: Pokemon, energy_cost): #-> Bool
    if pokemon.energy_points >= energy_cost:
        return True
    else:
        False        

def attack(
    success_rate,
    attack_damage,
    attacking_pokemon: Pokemon,
    defender_pokemon: Pokemon,
    energy_cost,
):

    value = random.random(0, 1)
    attacking_pokemon.defend = False
    attacking_pokemon.energy_points -= energy_cost

    if value <= success_rate:
            print("El ataque ha impactado")

            defender_pokemon.HP -= (
                attack_damage
                + (attack_damage * crit_damage(attacking_pokemon.crit_damage, attacking_pokemon.crit_rate))
                + (attack_damage * elemental_bonus(attacking_pokemon, defender_pokemon))
            )
            return defender_pokemon.HP, attacking_pokemon.energy_points

    else:
        print("El ataque ha fallado")
        return defender_pokemon.HP, attacking_pokemon.energy_points



def defend(pokemon: Pokemon):

    pokemon.energy_points += 1
    pokemon.defend = True

    return pokemon.energy_points, pokemon.defend


def rest(pokemon: Pokemon):
    pokemon.energy_points += 2
    pokemon.defend = False
    return pokemon.energy_points, pokemon.defend





import json
from pathlib import Path

ruta_archivo = Path(__file__).parent / "pokemon_list.json"  

with open(ruta_archivo, mode='r') as file:
    pokemons = json.load(file)
    
    


def crear_objetos_pokemon(lista_pokemon):
    
    objetos_creados = []
    
    for diccionario in lista_pokemon: 
        pokemon = Pokemon(diccionario.get("nombre"), 
                diccionario.get("tipo"), 
                diccionario.get("puntos_vida"),
                diccionario.get("probabilidad_critico")/100,
                diccionario.get("bonificacion_critico")/100)
        
        objetos_creados.append(pokemon)
    
    return objetos_creados
        
        





