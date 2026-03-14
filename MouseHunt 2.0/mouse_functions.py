import random
from globals import *
from ascii_art import tiny_mouse, brown_mouse, white_mouse, grey_mouse, field_mouse, mouse_king

def generate_mouse(cheese="Cheddar", enchant=False, points=0) -> str | None:
    while True:
        probability = generate_probabilities(cheese, enchant)
        num = random.random()
        # Check if Mouse King probability exists
        mouse_king_chance = probability[6] if len(probability) == 7 else 0
        # using cumulative probability
        if num >= (1 - mouse_king_chance):
            spawn_mouse = "MouseKing"
        elif num >= (1 - mouse_king_chance - probability[5]):
            spawn_mouse = "Tiny"
        elif num >= (1 - mouse_king_chance - probability[5] - probability[4]):
            spawn_mouse = "White"
        elif num >= (1 - mouse_king_chance - probability[5] - probability[4] - probability[3]):
            spawn_mouse = "Grey"
        elif num >= (1 - mouse_king_chance - probability[5] - probability[4] - probability[3] - probability[2]):
            spawn_mouse = "Field"
        elif num >= (1 - mouse_king_chance - probability[5] - probability[4] - probability[3] - probability[2] - probability[1]):
            spawn_mouse = "Brown"
        else:
            spawn_mouse = None
        # Mouse Unlocking Based on Points
        if points < 100:
            if spawn_mouse not in [None, "Field"]:
                continue
        elif points < 300:
            if spawn_mouse not in [None, "Field", "Grey", "White", "Brown"]:
                continue
        elif points < 1000:
            if spawn_mouse == "MouseKing":
                continue  
        break
    return spawn_mouse

def generate_probabilities(cheese_type, enchant=False):
    global points
    if cheese_type.lower() == "cheddar":
        # (None, Brown, Field, Grey, White, Tiny)
        if points < 100:
            # Increased Field Mouse chance for beginners
            return (0.6, 0, 0.4, 0, 0, 0)  # Only None, Brown, and Field mice available
        else:
            return (0.5, 0.1, 0.15, 0.1, 0.1, 0.05)
    elif cheese_type.lower() == "marble":
        return (0.6, 0.05, 0.2, 0.05, 0.02, 0.08)
    elif cheese_type.lower() == "swiss":
        if points > 1000:
            if not enchant:
                # (None, Brown, Field, Grey, White, Tiny, Mouse King)
                return (0.6, 0.01, 0.05, 0.05, 0.04, 0.14, 0.11)  # 11% chance for Mouse King
            else:
                return (0.35, 0.01, 0.05, 0.05, 0.04, 0.39, 0.11)  # Increased Tiny chance, Mouse King remains
        else:
            if not enchant:
                return (0.7, 0.01, 0.05, 0.05, 0.04, 0.15)  # No Mouse King yet
            else:
                return (0.45, 0.01, 0.05, 0.05, 0.04, 0.4)  # No Mouse King yet (enchanted case)
            
def generate_coat(type):
    if type == "Tiny":
        return tiny_mouse()
    elif type == "Brown":
        return brown_mouse()
    elif type == "White":
        return white_mouse()
    elif type == "Grey":
        return grey_mouse()
    elif type == "Field":
        return field_mouse()
    elif type == "MouseKing":
        return mouse_king()
    
def check_mouse_present():
    # Get current mice inventory

    current_dict = {}
    mouse_list = ["Brown", "Field", "Grey", "White", "Tiny"]
    
    # Count mice
    count = 0
    for key, val in box["content"].items():
        if key in mouse_list:
            current_dict[key] = current_dict.get(key, 0) + val
            count += val
    
    if count == 0:
        return None
    
    return current_dict
        
def loot_lut(mouse_type: str | None) -> tuple:
    if mouse_type == None:
        gold = 0
        points = 1              # hunt korlei 1 xp
    elif mouse_type == "Brown":
        gold = 70
        points = 60
    elif mouse_type == "Field":
        gold = 15
        points = 20
    elif mouse_type == "Grey":
        gold = 60
        points = 50
    elif mouse_type == "White":
        gold = 80
        points = 70
    elif mouse_type == "Tiny":
        gold = 100
        points = 100
    elif mouse_type == "MouseKing":
        gold = 10000
        points = 500
    return (gold, points)

def display_mouse_inventory(current_dict, name):
    print("\n---------------------------------")
    print(f"Hunter {name}, you currently have:")
    for key, val in current_dict.items():
        print(f"{key}: {val}")
    print("----------------------------------\n")