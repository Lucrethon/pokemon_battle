from __future__ import annotations
import game_logic as g

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
        self.is_defending = False

    def __repr__(self):
        return f"\nNombre: {self.name} \nElemento: {self.element} \nPuntos de vida: {self.HP} \nProbabilidad de ataque critico: {self.crit_rate} \nBonificador de ataque critico: {self.crit_damage}"  # \nAtaques: \n{self.attacks}"

    def has_enough_energy(self, attack: Attack):  # -> Bool
        if self.energy_points >= attack.energy_cost:
            return True
        else:
            False

    def get_crit_attack(self):

        value = random.random(0, 1)

        if value <= self.crit_rate:
            return self.crit_damage
        else:
            return 0

    def set_HP(self, number):
        self.HP += number
        
    
    def defend(self):

        self.energy_points += 1
        self.is_defending = True
        
    def rest(self):

        self.energy_points += 2
        self.is_defending = False


    def attack(self, other: Pokemon, attack: Attack):

        self.defend = False

        self.energy_points -= attack.energy_cost

        if Attack.is_successful_attack():

            print("El ataque ha impactado")

            if other.is_defending:

                damage = - (0.6 * (
                    Attack.damage + (Attack.damage * Pokemon.get_crit_attack(self))
                    ))
                    # Esto significa que other.HP perderá solo el 60% del daño calculado originalmente si other.is_defending = True
                other.set_HP(damage)


            else:

                damage = -(
                    Attack.damage
                    + (Attack.damage * Pokemon.get_crit_attack(self))
                    + (Attack.damage * Attack.get_elemental_bonus(other.element))
                    )
                other.set_HP(damage)

        else:
            print("El ataque ha fallado")

    def is_defeated(self):  # --> Bool
        if self.HP <= 0:
            return True

        else:
            return False
    
    def has_elemental_weakness(self, attack: Attack) -> bool:
        return (
            (attack.elemental_effect == "agua" and self.element == "fuego") or
            (attack.elemental_effect == "planta" and self.element == "agua") or
            (attack.elemental_effect == "fuego" and self.element == "planta")
        )


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

    def is_successful_attack(self):  # --> bool

        value = random.random(0, 1)

        if value <= self.success_rate:
            return True
        else:
            return False

    def get_elemental_bonus(self, defender_pokemon: Pokemon):

        if defender_pokemon.is_defending == False:
            if self.elemental_effect == "ninguno":
                return 0
            else:
                bonus_elemental = 0.2 if defender_pokemon.has_elemental_weakness else 0

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

        # indices = [i for i, x in enumerate(array) if x > 3]
        defeated_indice = [
            i for i, pokemon in enumerate(self.pokemon_team) if pokemon.defeated()
        ]  # -> Indice

        if defeated_indice:

            pokemon_defeated = self.pokemon_team.pop(defeated_indice)
            self.defeated_pokemon.append(pokemon_defeated)

        else:
            None
