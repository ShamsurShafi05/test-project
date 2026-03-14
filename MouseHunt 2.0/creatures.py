from ascii_art import tiger_art, wild_boar_art
from globals import player_health
from mouse_functions import generate_mouse, loot_lut, generate_coat



class Animal:
    def __init__(self, type):
        if type == "tiger":
            self.type = "tiger"
            self.damage = 60
            self.art = tiger_art()
        elif type == "wild boar":
            self.type = "wild boar"
            self.damage = 20
            self.art = wild_boar_art()

    def attack(self):
        global player_health
        player_health -= self.damage
        if player_health <= 0:
            player_health = 0
        print(self.art)
        print(f"\nA {self.type} just attacked you! You lost {self.damage} HP!\n\n")
    
class Mouse:
    def __init__(self, cheese = "Cheddar", enchant = False, points = 0):
        self.name = generate_mouse(cheese, enchant, points)
        values = loot_lut(self.name)
        self.gold = values[0]
        self.points = values[1]
        self.coat = generate_coat(self.name)

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points

    def get_coat(self):
        return self.coat

    def __str__(self) -> str:
        if self.name == None:
            return "None"
        else:
            return self.name