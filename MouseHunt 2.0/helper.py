import time
from globals import *
from ascii_art import character_art, white_mouse, grey_mouse, brown_mouse, tiny_mouse


def show_description(message):
    description = message
    lines = description.strip().split("\n")
    for line in lines:
        print(line)
        time.sleep(2)  # Delay of 2 seconds before showing the next line

# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def has_cheese(to_check, my_cheese):
    for i in range(len(my_cheese)):
        if my_cheese[i][0] == to_check.capitalize():
            if my_cheese[i][1] == 0:
                return 0
            else:
                return my_cheese[i][1]
            
# `````````````````````````````````````````` PLAYER HEALTH CHECK ````````````````````````````````````````````````````````````````````````````
def check_health(player_health):
    alive = True
    if player_health <= 0:
        print("\n\n\nOHNOH! Unfortunately, you've succumbed to your wounds and illnesses..\n")
        alive = False
        return alive
    elif player_health < 10:
        print("\nWARNING! Your health needs immediate medical attention. Head out to Hospital asap!\n")
    elif player_health < 50:
        print("\nHEADS UP! Your health is deteriorating. Food and potion items will be handy to recover!\n")
    return alive

def increase_time(game_time, increment):
    global game_day
    hours = int(game_time[:2])
    new_time = hours + increment
    if new_time >= 24:
        game_day += new_time // 24  # Increase the day count
        new_time = new_time % 24  # Keep time within 24-hour format    
    game_time = f"{new_time:02d} 00"  # Pad with zero if less than 10
    return game_time

def add_to_box(item, type=None, quantity=1):
    global box
    items_added = 0
    if not box["created"]:
        print("You have no Storage Crate yet")
        return items_added
    # Determine space needed for item
    space_needed = 5 if type == "trap" else 3 if type == "potion" else 2 if type == "mouse" else 1
    for _ in range(quantity):
        if box["space"] < space_needed:
            print(f"Only {items_added} {item}(s) added to the crate because space ran out.")
            return items_added
        box["space"] -= space_needed
        if item in box["content"]:
            box["content"][item] += 1
        else:
            box["content"][item] = 1    
        items_added += 1
    if type == "mouse":
        extra = "mouse"
    else:
        extra = ""
    if items_added != 0:
        print(f"{items_added} {item} {extra} has been added to your Storage Crate. You can now add only {box['space']} more items to your Crate!")
    return items_added


def remove_from_box(box, item, quantity=1):
    # global box
    if not box["created"]:
        print("You have no Storage Crate yet!\n")
        return
    if item not in box["content"]:
        print(f"{item} is not in the storage crate.\n")
        return
    
    item_type = get_item_type(item)

    # Space recovered based on type
    if item_type == "trap":
        space_recovered = 5
    elif item_type == "potion":
        space_recovered = 3
    elif item_type == "mouse":
        space_recovered = 2
    elif item_type == "cheese":
        space_recovered = 1
    elif item_type == "food":
        space_recovered = 1
    else:
        space_recovered = 1  # Default fallback

    items_removed = min(quantity, box["content"][item])
    box["content"][item] -= items_removed
    box["space"] += items_removed * space_recovered
    if box["content"][item] == 0:
        del box["content"][item]
    # eta ekhane print na kore amra pore print korbo inside Remove from Inventory function
    print(f"Removed {items_removed} {item}(s) from the crate. Remaining space: {box['space']}\n")
    return box

def get_item_type(item):
    global TYPE_OF_MOUSE, TRAP, CHEESE_MENU, meds_dict, food
    if item in TYPE_OF_MOUSE:
        return "mouse"
    elif any(item == cheese[0] for cheese in CHEESE_MENU):
        return "cheese"
    elif any(item == trap[0] for trap in TRAP):
        return "trap"
    elif item in food:
        return "food"
    elif item in meds_dict:
        return "potion"
    else:
        return "other"
    

def search_box(obj):
    global box
    foundobj = False
    for key, val in box["content"].items():
        if obj.lower() == key.lower():
            foundobj = True
    return foundobj


def display_inventory(wood: int, gold: int, cheese: list, trap: str, name: str) -> None:
    global trap_option, trap_cheese, food, meds_dict
    character_art(name)
    print(f"Hunter, you currently have:\n")
    print("Wood -", wood)
    print("Gold -", gold)
    print("Trap selected - ", trap)
    print("Cheese on trap: - ", trap_cheese)
    print("\nCheese options:")
    print("Cheddar -", cheese[0][1])
    print("Marble -", cheese[1][1])
    print("Swiss -", cheese[2][1])
    print("\nTrap options:")
    print(f"{trap_option[0][0]} - will last {trap_option[0][1]} more hunts.")
    print(f"{trap_option[1][0]} - will last {trap_option[1][1]} more hunts.")
    print(f"{trap_option[2][0]} - will last {trap_option[2][1]} more hunts.")
    print("\nFood options:")
    for key, val in food.items():
        print(f"{key} - {val}")
    print("\nPotions options:")
    for key, val in meds_dict.items():
        print(f"{key} - {val}")
    print("\n``````````````````````````````````\n")
    # Check if the storage crate exists and is not empty before asking for removal
    if not box["created"] or not box["content"]: 
        return
    # self note: box["content"] is assumed to be a dictionary storing items inside the storage crate. In Python, an empty dictionary ({}) is considered False in a boolean context.
    while True:
        remove_choice = input("Do you want to remove any item from Storage Crate? Enter 'yes' or 'no': ").strip().lower()
        if remove_choice.lower() != "yes" and remove_choice.lower() != "no":
            print("Please enter a valid input.\n")
            return
        else: 
            if remove_choice.lower() == "no":
                print("It's wise to hold onto your inventory items.\n")
                return
            else:
                break
    while True:
        # print(box["content"])
        item = input("Enter the name of the item you want to remove (or type 'cancel' to exit): ").strip()
        if item.lower() == 'cancel':
            print("Removal process cancelled.\n")
            time.sleep(3)
            return
        try:
            max_quantity = box["content"][item]  # Get the available quantity of the item
        except KeyError:
            print("Item not found in the Storage Crate. Please enter a valid item.\n")
            print("Note: If there is an item listed 'Wood-Cage' in your inventory which you want to remove, entering 'Wood Cage' or 'wood-cage' will not suffice!\n")
            continue

        while True:
            try:
                quantity = int(input(f"Enter the quantity of {item} to remove (Max: {max_quantity}): "))
                if quantity == 0:
                    print("No items removed.\n")
                    break
                elif quantity < 0:
                    print("Please enter a valid quantity (0 or more).\n")
                elif quantity > max_quantity:
                    print(f"Insufficient stock! You only have {max_quantity} {item}(s). Please enter a valid quantity.\n")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value (e.g., 1, 2, 3). Non-numeric inputs like letters or symbols are not allowed.\n")
        box = remove_from_box(box, item, quantity)
        return box

def display_cheese_inventory(name: str, cheese: list) -> None:
    # try to get rid of bc display_inventory() exists
    global trap_cheese
    print("\n---------------------------------")
    print(f"Hunter {name}, you currently have:")
    print("Cheese on trap: ", trap_cheese)
    print("\nAvailable:")
    print("Cheddar -", cheese[0][1])
    print("Marble -", cheese[1][1])
    print("Swiss -", cheese[2][1])
    print("----------------------------------\n")

def get_benefit(cheese):
    # Look-back
    if cheese.lower() == "swiss":
        return "+0.25 attraction to tiny mouse"
    
def check_game_over():
    global gold, cheese, points
    status = check_health()
    if status == False:
        print("\nYou have succumbed to your injuries... Game over!\n")
        return True
    if gold < 10:
        total = 0
        for i in cheese:
            total += i[-1]
        if total == 1:
            print("\nYour survival comes down to this cheese.\n")
            print("Here's our special ritual that is believed to help a long generation of hunters alike yourself:\n")
            print(r"""
                    Waluuudulan dandanali
                    Watoblutob tobtobali
            """)
            print()
            return False
        if total == 0:
            print("\nSorry you've run out of cheese and do not have any more gold to make purchases!")
            return True
    else:
        return False

def consume_cheese(to_eat: str, my_cheese: list) -> tuple:           
    left = has_cheese(to_eat, my_cheese)
    if left == 0:
        return (my_cheese, False)
    else:
        for i in range(len(my_cheese)):
            if my_cheese[i][0] == to_eat.capitalize():
                my_cheese[i][1] -= 1
    return (my_cheese, True)

def has_cheese(to_check, my_cheese):
    for i in range(len(my_cheese)):
        if my_cheese[i][0] == to_check.capitalize():
            if my_cheese[i][1] == 0:
                return 0
            else:
                return my_cheese[i][1]

def level_check_1():
    global box
    print("\n\n\n=========================================================")
    print("Congrats you have unlocked new items:\n")
    time.sleep(2)
    print("NEW CHEESE: MARBLE")
    time.sleep(2)
    print("NEW TRAP: REINFORCED WOOD-CAGE")
    time.sleep(2)
    # meds_dict = {"Herbal Remedy": 0, "Bloodroot Elixir": 0, "Witch’s Brew": 0}
    print("NEW POTION: BLOODROOT ELIXIR")
    time.sleep(2)
    print("STORAGE CRATE CAPACITY INCRESED: +5 ITEMS")
    time.sleep(2)
    box["space"] += 5
    print(white_mouse())
    time.sleep(2)
    print(grey_mouse())
    time.sleep(2)
    print(brown_mouse())
    time.sleep(2)
    print("========================================================\n\n")

def level_check_2():
    print("\n\n\n=========================================================")
    print("Congrats you have unlocked new items:\n\n")
    time.sleep(2)
    print("NEW CHEESE: SWISS")
    time.sleep(2)
    print("NEW TRAP: MULTILAYER GLUED-BOARD")
    time.sleep(2)
    print("NEW POTION: WITCH'S BREW")
    time.sleep(2)
    print("ENCHANTMENT UNLOCKED")
    time.sleep(2)
    print("STORAGE CRATE CAPACITY INCRESED: +10 ITEMS")
    box["space"] += 10
    time.sleep(2)
    print(tiny_mouse())
    time.sleep(2)
    print("=========================================================\n\n")

def announcement():
    global points, called_functions
    if points >= 100:
        if called_functions["level_check_1"] == False:
            level_check_1()
            called_functions["level_check_1"] = True
    if points >= 300:
        if called_functions["level_check_2"] == False:
            level_check_2()
            called_functions["level_check_2"] = True
    
def consume_item(food, meds_dict, player_health, max_health):
    # global food, meds_dict, player_health, max_health
    count1 = 0
    str1 = "\nFood options:\n"
    for key, val in food.items():
        str1 = str1 + f"{key}: {val} left\n"
        count1 += val
    str1.strip()
    count2 = 0
    str2 = "\nPotion options:\n"
    for key, val in meds_dict.items():
        str2 = str2 + f"{key}: {val} left\n"
        count2 += val
    str2.strip()
    if count1 == 0 and count2 == 0:
        print("You don't have any consumeable items in your Storage Crate!\n")
        return False
    elif count1 == 0:
        print("You don't have any food items in your Storage Crate!\n")
        time.sleep(2)
        print(str2)
        time.sleep(2)
    elif count2 == 0:
        print("You don't have any potion items in your Storage Crate!\n")
        time.sleep(2)
        print(str1)
        time.sleep(2)
    else:
        print(str1)
        time.sleep(2)
        print(str2)
        time.sleep(2)
    print("\n---------------------------------\n")
    while True:
        item = input("What would you like to consume? You gotto type in the exact name (Press '0' to exit): ").strip()
        if item == '0':
            return False
        if item in food:
            food_options = ["Apple", "Banana", "Berry", "Mushroom", "Frog"]
            if  food[item] > 0:
                food[item] -= 1
                print(f"\nYou consumed {item}. {food[item]} left.\n")
                inc = food_options.index(item)+1
                player_health += inc
                if player_health > max_health:
                    player_health = max_health
                time.sleep(5)
                print(f"You got much needed rest.. {inc} HP restored!\n")
                box = remove_from_box(box, item)
                return box
                break
            else:
                print(f"\n{item} is out of stock")
        elif item in meds_dict:
            meds_option = ["Herbal Remedy", "Bloodroot Elixir", "Witch’s Brew"]
            if meds_dict[item] > 0:
                meds_dict[item] -= 1
                print(f"\nYou consumed {item}. {meds_dict[item]} left.\n")
                if item == "Herbal Remedy":
                    inc = 20
                elif item == "Bloodroot Elixir":
                    inc = 50
                else:
                    inc = max_health - player_health 
                player_health += inc
                if player_health > max_health:
                    player_health = max_health
                time.sleep(5)
                print(f"You fell asleep soon after.. {inc} HP restored!\n")
                box = remove_from_box(box, item)
                return box
                break
            else:
                print(f"\n{item} is out of stock\n")
        else:
            print(f"\nYou dont have {item} in your Storage Crate\n")

def check_box(box):
    # global box
    if not box["created"]:
        print("You don't have a Storage Crate yet. Head out to the Old Carpenter to help you get one!\n")
        time.sleep(2)
        return False
    elif not box["content"]:
        print("You don't have any items in your Storage Crate right now!\n")
        time.sleep(2)
        return False
    elif box["space"] == 0:
        print("You can't add any more items in your Storage Crate right now. It is full!")
        print("Try clearing your inventory or trade off some items at the trader to cash in some gold!\n")
        time.sleep(2)
        return None
    else:
        return True
    
