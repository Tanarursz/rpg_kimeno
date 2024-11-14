import json

with open('rpg_characters.json', 'r') as file:
    data = json.loads(file)

class Charcter:
    def __init__(self, name, level, health, attack, defense):
        self.nam = name
        self.lv = level
        self.heal = health
        self.atk = attack
        self.defns = defense

    def take_damge(self, damage):
        self.heal -= damage * 2 
        if self.heal < 0:
            self.heal = 0
        print(f"{self.nam} took {damage} damage and now has {self.heal} health left.")

characters = [Charcter(**char) for char in data['characters']]

def fightt(character1, character2):
    print(f"Battle between {character1.nam} and {character2.nam} starts!")
    while character1.heal > 0 and character2.heal > 0:
        damage = character1.atk - character2.defns  
        character2.take_damge(damage)

        if character2.heal <= 0:
            print(f"{character2.nam} is defeated! {character1.nam} wins!")
            break

       
        damage = character2.atk - character1.defns
        character1.take_damge(damage)

   
        if character1.heal <= 0:
            print(f"{character1.nam} is defeated! {character2.nam} wins!")
            break

fightt(characters[0], characters[1])
