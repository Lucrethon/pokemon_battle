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

    elemental_bonus = {
        "fire": {"plant": 0.2, "water": 0, "fire": 0, "neutral": 0},
        "water": {"plant": 0, "water": 0, "fire": 0.2, "neutral": 0},
        "plant": {"plant": 0, "water": 0.2, "fire": 0, "neutral": 0},
        "neutral": {"plant": 0, "water": 0, "fire": 0, "neutral": 0},
    }


def elemental_bonus(attacking_pokemon: Pokemon, defender_pokemon: Pokemon): 
    
    if defender_pokemon.defend == False: 
        bonus_elemental = Pokemon.elemental_bonus.get(attacking_pokemon.element, {}).get(defender_pokemon.element)
        return bonus_elemental
    
    else:
        return 0

def attack(
    success_rate,
    attack_damage,
    crit_rate,
    crit_damage,
    attacking_pokemon: Pokemon,
    defender_pokemon: Pokemon,
    energy_cost,
):

    value = random.random(0, 1)
    attacking_pokemon.defend = False

    if value <= success_rate:
        if attacking_pokemon.energy_points >= energy_cost:
            attacking_pokemon.energy_points -= energy_cost
            print("El ataque ha impactado")
            

            if value <= crit_rate:
                defender_pokemon.HP -= attack_damage + (attack_damage * crit_damage) + (attack_damage * elemental_bonus(attacking_pokemon, defender_pokemon))
                return defender_pokemon.HP, attacking_pokemon.energy_points
                

            else:
                defender_pokemon.HP -= attack_damage + (attack_damage * elemental_bonus(attacking_pokemon, defender_pokemon))
                return defender_pokemon.HP, attacking_pokemon.energy_points
            
        else:
            print("No hay suficiente energia para realizar este ataque")
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






