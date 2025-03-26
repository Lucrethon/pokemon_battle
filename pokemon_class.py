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
        

    
    
    
def attack(success_rate, attack_damage, crit_rate, crit_damage, pokemon1: Pokemon, pokemon2: Pokemon, energy_cost): 
    
    value = random.random(0, 1)
    
    if value <= success_rate: 
        pokemon1.energy_points = pokemon1.energy_points - energy_cost
        print("El ataque si impacto")
        
        if value <= crit_rate: 
            pokemon2.HP = pokemon2.HP - attack_damage - crit_damage
            return pokemon2.HP, pokemon1.energy_points
        
        else:
            pokemon2.HP = pokemon2.HP - attack_damage
            return pokemon2.HP, pokemon1.energy_points
    
    else: 
        print("El ataque no ha impactado")
        


def defend(pokemon: Pokemon, attack_damage):
    
    pokemon.HP = pokemon.HP - (40% - attack_damage)
    pokemon.energy_points = pokemon.energy_points + 1
    
    return pokemon.HP, pokemon.energy_points


def rest(pokemon: Pokemon, attack_damage):
    pokemon.HP = pokemon.HP - attack_damage
    pokemon.energy_points = pokemon.energy_points + 2