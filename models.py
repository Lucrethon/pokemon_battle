from __future__ import annotations

import random


class Pokemon:

    def __init__(self, name, element, HP, crit_rate, crit_damage, attacks):
        self.name = name
        self.element = element
        self.HP = HP
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        self.energy_points = 10
        self.attacks = attacks  # --> array
        self.defend = False

    def __repr__(self):
        return f"\nNombre: {self.name} \nElemento: {self.element} \nPuntos de vida: {self.HP} \nProbabilidad de ataque critico: {self.crit_rate} \nBonificador de ataque critico: {self.crit_damage}" #\nAtaques: \n{self.attacks}"

    def get_crit_attack(self):

        value = random.random(0, 1)

        if value <= self.crit_rate:
            return self.crit_damage
        else:
            return 0

    def defending(self):

        self.energy_points += 1
        self.defend = True

        return self.energy_points, self.defend

    def resting(self):

        self.energy_points += 2
        self.defend = False

        return self.energy_points, self.defend

    def attack(self, other, attack: Attack):

        self.defend = False

        if Attack.has_enough_energy(self.energy_points):

            self.energy_points -= attack.energy_cost

            if Attack.is_successful_attack():

                print("El ataque ha impactado")

                if other.defend:

                    other.HP -= 0.6 * (
                        Attack.damage + (Attack.damage * Pokemon.get_crit_attack(self))
                    )
                    # Esto significa que other.HP perderá solo el 60% del daño calculado originalmente si other.defend = True

                    return other.HP, self.energy_points

                else:

                    other.HP -= (
                        Attack.damage
                        + (Attack.damage * Pokemon.get_crit_attack(self))
                        + (Attack.damage * Attack.get_elemental_bonus(other.element))
                    )
                    return other.HP, self.energy_points

            else:
                print("El ataque ha fallado")
                return self.energy_points
        else:
            print("No tienes suficiente energia para realizar este ataque")
    
    def defeated(self): #--> Bool
        if self.HP <= 0: 
            return True
        
        else:
            return False


class Attack:

    def __init__(
        self,
        name,
        description,
        energy_cost,
        success_rate,
        damage,
        elemental_effect,
        special_effect,
    ):
        self.name = name
        self.description = description
        self.energy_cost = energy_cost
        self.success_rate = success_rate
        self.damage = damage
        self.elemental_effect = elemental_effect
        self.special_effect = special_effect

    def __repr__(self):
        return f"\nNombre: {self.name} \nDescripcion: {self.description} \nCosto de Energia: {self.energy_cost} \nProbabilidad de impacto: {self.success_rate} \nDaño: {self.damage} \nEfecto Elemental: {self.elemental_effect} \nEfecto Especial: {self.special_effect}"

    elemental_bonus = {
        "fuego": {"planta": 0.2, "agua": 0, "fuego": 0, "neutral": 0},
        "agua": {"planta": 0, "agua": 0, "fuego": 0.2, "neutral": 0},
        "planta": {"planta": 0, "agua": 0.2, "fuego": 0, "neutral": 0},
    }

    def has_enough_energy(self, attacking_pokemon: Pokemon):  # -> Bool
        if attacking_pokemon.energy_points >= self.energy_cost:
            return True
        else:
            False

    def is_successful_attack(self):  # --> bool

        value = random.random(0, 1)

        if value <= self.success_rate:
            return True
        else:
            return False

    def get_elemental_bonus(self, defender_pokemon: Pokemon):

        if defender_pokemon.defend == False:
            if self.elemental_effect == "ninguno":
                return 0
            else: 
                bonus_elemental = Attack.elemental_bonus.get(self.elemental_effect, {}).get(
                    defender_pokemon.element
            )

                return bonus_elemental

        else:
            return 0


class PokemonTrainer: 
    
    def __init__(self, name, pokemon_team):
        self.name = name
        self.pokemon_team = pokemon_team
        self.defeated_pokemon = []
        self.is_first_player = False
        self.current_pokemon = None
    
    def defeated_pokemon_list(self):
        
        #indices = [i for i, x in enumerate(array) if x > 3]
        defeated_indice = [i for i, pokemon in enumerate(self.pokemon_team) if pokemon.defeated()] #-> Indice
        
        if defeated_indice: 
            
            pokemon_defeated = self.pokemon_team.pop(defeated_indice)
            self.defeated_pokemon.append(pokemon_defeated)
            
            return self.pokemon_team, self.defeated_pokemon
        
        else: 
            return self.pokemon_team, self.defeated_pokemon
        
        