import random
import time

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


class Animal:
    def __init__(self, type):
        if type == "tiger":
            self.type = "tiger"
            self.damage = 60
        elif type == "wild boar":
            self.type = "wild boar"
            self.damage = 20

    def attack(self, current_health):
        alive = True
        current_health -= self.damage
        if current_health <= 0:
            current_health = 0
            alive = False

        print(f"A {self.type} just attacked you! You lost {self.damage} HP")
        return (current_health, alive)


def tiny_mouse():
    str = r"""
        (\_/)
        (o.o)  Tiny Mouse
        (")(")
        """
    return str


def brown_mouse():
    str = r"""
        (\_/)
       ( o.o )  Brown Mouse
       (  :  )
       /     \
      /       \
    """
    return str

def white_mouse():
    str = r"""
         (\__/)
        ( o . o )  White Mouse
         (  "  )
         /    \
        /      \
       (________)
    """
    return str

def grey_mouse():
    str = r"""
         (\_/)
        ( o.o )  Grey Mouse
        (  :  )
       /       \
      (         )
       \_______/
    """
    return str

def field_mouse():
    str = r"""
         (\__/)
        ( o.o )  Field Mouse
         (__:__)/

    """
    return str

def generate_mouse(cheese = "Cheddar", enchant = False, points = 0) -> str | None:

    while True:
        probability = generate_probabilities(cheese, enchant)
        num = random.random()

        if num >= (1-probability[5]):
            spawn_mouse = "Tiny"
        elif num >= (1-probability[5]-probability[4]):
            spawn_mouse = "White"
        elif num >= (1-probability[5]-probability[4]-probability[3]):
            spawn_mouse = "Grey"
        elif num >= (1-probability[5]-probability[4]-probability[3]-probability[2]):
            spawn_mouse = "Field"
        elif num >= (1-probability[5]-probability[4]-probability[3]-probability[2]-probability[1]):
            spawn_mouse = "Brown"
        else:
            spawn_mouse = None


        if points < 100:
            if spawn_mouse not in [None, "Field"]:
                continue
            else:
                break
        elif points < 300:
            if spawn_mouse not in [None, "Field", "Grey", "White", "Brown"]:
                continue
            else:
                break
        else:
            break


    return spawn_mouse


def loot_lut(mouse_type: str | None) -> tuple:
    '''
    Look-up-table for gold and points for different types of mouse
    Parameter:
        mouse_type: str | None, type of mouse
    Returns:
        gold:       int, amount of gold reward for mouse
        points:     int, amount of points given for mouse
    '''
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

    return (gold, points)


def generate_probabilities(cheese_type, enchant = False):
    if cheese_type.lower() == "cheddar":
        return (0.5, 0.1, 0.15, 0.1, 0.1, 0.05)
    elif cheese_type.lower() == "marble":
        return (0.6, 0.05, 0.2, 0.05, 0.02, 0.08)
    else:
        if enchant == False:
            return (0.7, 0.01, 0.05, 0.05, 0.04, 0.15)
        else:
            return (0.45, 0.01, 0.05, 0.05, 0.04, 0.4)

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




def get_game_menu():
    return "1. Exit Game\n2. Join the Hunt\n3. The Cheese Shop\n4. Change Trap Cheese\n5. Scavenge Forest Floor\n6. Visit Trader\n7. Visit Witch Doctor\n8. Visit Old Carpenter\n9. Change Trap\n10. Check Stats\n11. Hunting Tutorial\n"


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


def consume_cheese(to_eat: str, my_cheese: list) -> tuple:           #cheese parameter to my_cheese parameter bc of question 7

    left = has_cheese(to_eat, my_cheese)
    if left == 0:
        return (my_cheese, False)
    else:
        for i in range(len(my_cheese)):
            if my_cheese[i][0] == to_eat.capitalize():
                my_cheese[i][1] -= 1

    return (my_cheese, True)

def has_cheese(to_check, my_cheese):            #new for question 7; used in the function above to check is cheese exists in inventory

    # if to_check == None:
    #     print("HAS CHEESE E NONE ASHCHE")
    #     return 0
    for i in range(len(my_cheese)):
        if my_cheese[i][0] == to_check.capitalize():
            if my_cheese[i][1] == 0:
                return 0
            else:
                return my_cheese[i][1]

def get_benefit(cheese):
    if cheese.lower() == "cheddar":
        return "+25 XP drop by next Brown mouse"
    elif cheese.lower() == "marble":
        return "+25 gold drop by next Brown mouse"
    elif cheese.lower() == "swiss":
        return "+0.25 attraction to tiny mouse"


def level_check_1():
    print("=========================================================")
    print("Congrats you have unlocked new items:\n")
    print("NEW CHEESE: MARBLE")
    print("NEW TRAP: REINFORCED WOOD-CAGE")
    print(white_mouse())
    print(grey_mouse())
    print(brown_mouse())
    print("=========================================================")


def level_check_2():
    print("=========================================================")
    print("Congrats you have unlocked new items:\n")
    print("NEW CHEESE: SWISS")
    print("NEW TRAP: MULTILAYER GLUED-BOARD")
    print("ENCHANTMENT UNLOCKED")
    print(tiny_mouse())
    print("=========================================================")

def check_health():
    global player_health

    alive = True
    if player_health <= 0:
        print("\nUnfortunately, you've succumbed to your wounds and illnesses..\n")
        alive = False
        return alive
    elif player_health < 10:
        print("\nYour health needs immediate medical attention. Head out to Hospital asap!\n")

    return alive



def hunt(gold, cheese, trap_cheese, enchant, points, called_functions, attempts, caught_mouse_dictionary, game_over_status):
    global game_time, player_health, box

    hunt = 0
    succes_streak = 0

    if box["created"] == False:
        print("You don’t have a Storage Crate yet! Even if you catch anything, you can’t store it!")
        print("Head out to the carpenter first to get yourself one.\n\n")
        user_input = input('Do you still want to continue? ["yes" or "no"] ')
        if user_input.lower() == "no":
            return (gold, points, cheese, called_functions, attempts, caught_mouse_dictionary, game_over_status)

    while True:
        if box["space"] < 2:
            print("\nWARNING! You don't seem to have enough space in your Storage Crate. Without sufficient space you will be forced to let go of any mouse you catch!\n\n")
        game_over_status = check_game_over()
        if game_over_status == True:
            break

        print("Time", game_time, "Gold:", str(gold) + ", XP:", points)

        # Stopping condition: Sound the horn by typing "yes": #stop hunt

        check_game_time = int(str(game_time)[:2])
                
        if 6 <= check_game_time <= 18:
            risk1, risk2 = 0.1, 0.2  # Daytime risks
        else:
            print("ProTip: The elders say it's best to avoid wondering around once dusk falls. Something lurks in the shadows of these unknown realms after dark.")
            user_input_timewise = input("Do you want to still continue to hunt? ['yes' or 'no'] ")
            if user_input_timewise.lower() == "no":
                break

            risk1, risk2 = 0.5, 0.6  # Night risks


        print("\nSound the horn to call for the mouse...")
        sound_input = input('Sound the horn by typing "yes". Type "stop" to end hunting session: ')
        if sound_input.isdigit() == True:
            print("Invalid input.\n")
            continue

        if sound_input.lower() == "stop":
            break

        # Random chance for encountering an animal
        num_new = random.random()
        if num_new < risk1:
            animal = Animal("tiger")
        elif num_new < risk2:
            animal = Animal("wild boar")
        else:
            animal = None

        if animal:
            player_health, alive = animal.attack(player_health)
            continue
        
            
        if sound_input == '' or sound_input != "yes":
            print("You did not properly sound the horn. Hunt wasted.")
            hunt += 1
            game_time = increase_time(game_time, 3)
        else:
            print("\n~~ ~ ~~~~ ~~~ ~~ ~~ ~ ~~~~\n")
            if trap_cheese == None:
                hunt += 1
                game_time = increase_time(game_time, 1)
                print("Nothing happens. You are out of cheese!")

            else:
                cheese, status = consume_cheese(trap_cheese, cheese)
                if status == False:
                    hunt += 1
                    game_time = increase_time(game_time, 1)
                    print("Nothing happens. You are out of cheese!")
                else:
                    mouse = Mouse(trap_cheese, enchant, points)
                    # print("CURRENTLY Cheese list is:", cheese)

                    if mouse.name != None:
                        hunt = 0
                        points += mouse.get_points()
                        gold += mouse.get_gold()
                        print("``````````````````````````````````````````")
                        print("You caught a {} mouse!".format(mouse.name))
                        print(mouse.get_coat())
                        print("``````````````````````````````````````````")
                        caught_mouse_dictionary[mouse.name] += 1
                        attempts["Successful hunt"] += 1
                        print(f"You earned {mouse.get_gold()} gold and {mouse.get_points()} XP!")
                        game_time = increase_time(game_time, 3)
                        # add_to_box(item, type=None, quantity=1)
                        add_to_box(mouse.name, "mouse")
                    else:
                        #print("H1:", hunt)
                        hunt += 1
                        attempts["Unsuccessful hunt"] += 1
                        #print("H2:", hunt)
                        print("The wilderness can sometimes be cruel. Hunt unsuccessful")
                        game_time = increase_time(game_time, 3)

        # print("Gold:", str(gold) + ", Points:", points)
        print()

        if points >= 100:
            if called_functions["level_check_1"] == False:
                level_check_1()
                called_functions["level_check_1"] = True

        if points >= 300:
            if called_functions["level_check_2"] == False:
                level_check_2()
                called_functions["level_check_2"] = True

        #print(hunt)
        if hunt%5 == 0 and hunt != 0:
            print("Looks like you're not having a great hunting session today.")
            user_input4 = input("Do you want to still continue to hunt? ['yes' or 'no'] ")
            if user_input4.lower() == "no":
                break

    return (gold, points, cheese, called_functions, attempts, caught_mouse_dictionary, game_over_status)



def display_cheese_inventory(name: str, cheese: list) -> None:

    print(f"Hunter {name}, you currently have:")
    #print(cheese)
    print("Cheddar -", cheese[0][1])
    print("Marble -", cheese[1][1])
    print("Swiss -", cheese[2][1])
    print()


def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:

    while True:
        display_cheese_inventory(hunter_name, cheese)

        cheese_name = input("Press 'back' when you're done. Type cheese name to arm trap: ")
        cheese_name = cheese_name.strip().capitalize()

        if cheese_name == "Back":
            return (False, None)

        cheese_found = False
        for i in cheese:
            if i[0] == cheese_name:
                cheese_found = True
                break

        if cheese_found == False:
            print("No such cheese!\n")
            continue


        cheese_available = False
        for i in cheese:
            if i[0] == cheese_name:
                if i[1] != 0:
                    cheese_available = True
                    break

        if cheese_available == False:
            print("Out of cheese!\n")
            continue

        if e_flag == True:
            print("Your {} has a one-time enchantment granting {}".format(trap, get_benefit(cheese_name)))

        #print(cheese_found, cheese_available)
        confirm = input(f"Do you want to arm your trap with {cheese_name}? ")
        confirm = confirm.lower().strip()


        if confirm == "yes":
            print(f"{trap} is now armed with {cheese_name}!")
            return (True, cheese_name)
        elif confirm == "back":
            return (False, None)
        elif confirm == "no":
            print()
            continue


def show_description(message):
    description = message
    lines = description.strip().split("\n")
    for line in lines:
        print(line)
        time.sleep(2)  # Delay of 2 seconds before showing the next line

def game_intro(message):

    # title = "Mousehunt"
    logo = """
      (\_/)
      (• .•)  < Mouse Hunt!
     \(  ><)
    ` ` ` ` `
    """
    Inspired_by = "Inspired by MouseHunt™, a release by ShafsterGames."
    author = "Programmer - Shamsur Shafi"
    credits = "Mice art - ChatGPT"

    # print(title + "\n")
    print(logo)
    print(Inspired_by)
    time.sleep(2)
    print(author)
    time.sleep(2)
    print(credits)
    time.sleep(2)
    print("Version launch - 1.2 (2025)")
    time.sleep(2)
    print()
    show_description(message)
    print()

def check_special_key(char):
    special_keys = {
        27: "Escape (ESC)",
        10: "Enter (LF - Line Feed)",   # Also '\n'
        13: "Enter (CR - Carriage Return)",  # Older Macs
        9:  "Tab (Horizontal Tab)",  # Also '\t'
        8:  "Backspace",
        32: "Space",
        127: "Delete"
    }

    ascii_value = ord(char)
    if ascii_value in special_keys:
        # print(f"Detected: {special_keys[ascii_value]}")
        return True
    else:
        # print("Not a special key.")
        return False

def is_valid_length(name):
    return 1 <= len(name) <= 9


def is_valid_start(name):
    if len(name) == 0:
        return False
    return name[0].isalpha()

def is_one_word(name):
    if len(name) == 0:
        return False
    for i in range(len(name)):
        if name[i] == ' ':
            return False
    return True

def is_valid_name(name):
    if not is_valid_length(name):
        print("Name must be between 1 and 9 characters")
    if not is_valid_start(name):
        print("Name must start with an alphabet")
    if not is_one_word(name):
        print("Name must be at least one word")

    return is_valid_length(name) and is_valid_start(name) and is_one_word(name)


def intro():
    print("``````````````````````````````````````````````````")
    print("                 TUTORIAL                         \n")
    print("Larry: Hi I'm Larry. I'll be your hunting instructor.")


def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    value = input("Press Enter to travel to the Meadow...")
    value = value.strip()
    if value == chr(27):
        return False
    else:
        print("Travelling to the Meadow...")
        print("Larry: This is your camp. Here you'll set up your mouse trap.")


def setup_trap():
    print("Larry: Let's get your first trap...")

    val1 = input("Press Enter to view traps that Larry is holding...")
    val1 = val1.strip()

    if val1 == chr(27):
        return False
    print("Larry is holding...")
    print("Left: Wood-and-Spring Trap")
    print("Right: Reinforced Wood-Cage Trap")
    trap_input = input('Select a trap by typing "left" or "right": ').strip()

    trap_input = trap_input.strip()
    if trap_input == chr(27):
        return False

    if trap_input.lower() == "left":
        print("Larry: Excellent choice.")
        print('Your Wood-and-Spring Trap is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        return ("Wood-and-Spring Trap", 1)
    elif trap_input.lower() == "right":
        print("Larry: Excellent choice.")
        print('Your Reinforced Wood-Cage Trap is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        return ("Reinforced Wood-Cage Trap", 1)
    else:
        print("Invalid command! No trap selected.")
        print("Larry: Odds are slim with no trap!")
        return ("Wood-and-Spring Trap", 0)


def sound_horn(trap_result):                                    #CHANGE
    print("Sound the horn to call for the mouse...")
    horn_sound = input('Sound the horn by typing "yes": ').lower()
    horn_sound = horn_sound.strip()
    horn_sound = horn_sound.lower()

    if horn_sound == chr(27):
        return False

    if horn_sound != "yes" and trap_result == ("Wood-and-Spring Trap", 0): #no trap, no horn
        print("Nothing happens.")

    elif horn_sound == "yes" and trap_result != ("Wood-and-Spring Trap", 0):
        print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.\nGood luck~")
        return "success"

    elif horn_sound == "yes" and trap_result == ("Wood-and-Spring Trap", 0):
         print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")

    else:
        print("Nothing happens.\nTo catch a mouse, you need both trap and cheese!")
        #print("To catch a mouse, you need both trap and cheese!")
    return horn_sound



def basic_hunt(cheddar: int, horn_input: str):
    if cheddar == 1 and horn_input.lower() == 'yes':
        print("Caught a Brown mouse!")
        return True

    elif  cheddar == 0 and horn_input.lower() == 'yes':
        print("Larry: Nothing happens.")
        return False
  # else:
    # print("Larry: Odds are slim with no trap!")
    # return False

def end(hunt_status: bool):
    if hunt_status:
        print("Congratulations. Ye have completed the training.\nGood luck~")



def cheese_shop_art():

    str = r"""
      ________________________
     /                        \
    /    The  Cheese  Shop     \
   /____________________________\
        ||                ||
       _||________________||__
      |                      |
      |   PRICES (IN GOLD)   |
      |                      |
      |     Cheddar - 10     |
      |     Marble  - 50     |
      |     Swiss   - 100    |
      |______________________|
       (____________________)
    """
    print(str)


def cheese_art():
    str = " "
    print(str)

def character_art(name):
    character = r"""
      O
     /|\
     / \
    """
    print(character)
    print(f"~ {name} ~")

def box_art():
    str = r"""
      +------+
     /      /|
    +------+ |
    |      | +
    |      |/
    +------+
    """
    return str

def trap_art():
    
    str = r"""
    ╔═══════╗
    ║ │ │ │ ║
    ║ │ │ │ ║
    ║ │ │ │ ║
    ║ │ │ │ ║
    ╚═══════╝
    """
    return str

def cheese_shop_intro():
    print("Cheese Dealer: How can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop")


def buy_cheese(gold: int, points: int) -> tuple:

    remain = gold
    spent = 0

    cheddar = 0
    marble = 0
    swiss = 0

    while True:

        print(f"You have {gold} gold to spend.")
        user_input = input("Cheese Dealer: Enter 'back' when you're done shopping. To buy, state [cheese quantity]: ")

        if len(user_input) == 0:
            print("Cheese Dealer: I don't seem to understand what you want..", end = '\n\n')
            continue

        #returning to main menu
        if user_input.lower() == "back":
            return (spent, (cheddar, marble, swiss))

        user_input = user_input.split()
        cheese = user_input[0].lower()

        #checking is cheese name is valid
        if cheese not in ["cheddar", "marble", "swiss"]:
            print(f"Cheese Dealer: We don't sell any {cheese}!")
            continue
        else:
            if points < 100:
                if cheese != "cheddar":
                    print(f"Cheese Dealer: You do not have enough XP to unlock this item yet. Choose another cheese.")
                    continue
            elif points < 300:
                if cheese == "swiss":
                    print(f"Cheese Dealer: You do not have enough XP to unlock this item yet. Choose another cheese.")
                    continue


        #checking if quantity is missing
        if len(user_input) == 1:
            print("Cheese Dealer: If you don't tell me what quantity of cheese you want how can I sell?")
            continue
        else:
            quantity = user_input[1]

        #checking if quantity enteres is not a number
        if quantity.isnumeric() == False:
            print("Cheese Dealer: Do you need me to teach you how numbers work..?")
            continue
        else:
            cheese_bought = int(quantity)

        #checking if quantity entered is non-positive
        if cheese_bought <= 0:
            print("Cheese Dealer: You need.. a negative amount of cheese, huh?")
            continue

        #cheese-wise base price setting
        if cheese == "cheddar":
            unit_price = 10
        elif cheese == "marble":
            unit_price = 50
        else:
            unit_price = 100

        gold_needed = cheese_bought * unit_price

        #successful buy or sell
        if gold_needed <= gold:
            print(f"Cheese Dealer: Pleasure doing business with you! You have successfully purchased {cheese_bought} {cheese}.", end = " ")
            cheese_art()
            if cheese == "cheddar":
                cheddar += cheese_bought
            elif cheese == "marble":
                marble += cheese_bought
            else:
                swiss += cheese_bought
            gold -= gold_needed
            spent += gold_needed

        else:
            print("Cheese Dealer: You don't have enough gold.")
            continue



def display_inventory(wood: int, gold: int, cheese: list, trap: str, name: str) -> None:
    global trap_option, trap_cheese, food
    character_art(name)
    print(f"Hunter, you currently have:\n")

    print("Wood -", wood)
    print("Gold -", gold)
    print("Trap selected - ", trap)
    print("Cheeese on trap: - ", trap_cheese)
    print("\nCheese options:")
    print("Cheddar -", cheese[0][1])
    print("Marble -", cheese[1][1])
    print("Swiss -", cheese[2][1])
    print("\nTrap options:")
    print(f"{trap_option[0][0]} - {trap_option[0][1]}")
    print(f"{trap_option[1][0]} - {trap_option[1][1]}")
    print(f"{trap_option[2][0]} - {trap_option[2][1]}")
    print("\nFood options:")
    for key, val in food.items():
        print(f"{key} - {val}")
    print("\n``````````````````````````````````\n")

    remove_choice = input("Do you want to remove any item from Storage Crate? (yes/no): ").strip().lower()
    if remove_choice != "yes":
        return
    
    while True:
        item = input("Enter the name of the item you want to remove (or type 'cancel' to exit): ").strip()
        if item.lower() == 'cancel':
            print("Removal process cancelled.\n")
            return
        
        if item not in box["content"]:
            print("Item not found in the storage crate. Please enter a valid item.\n")
            continue
        
        max_quantity = box["content"][item]  # Get the available quantity of the item
        
        while True:
            try:
                quantity = int(input(f"Enter the quantity of {item} to remove (Max: {max_quantity}): "))
                if quantity < 1:
                    print("Please enter a valid quantity (1 or more).\n")
                elif quantity > max_quantity:
                    print(f"Insufficient stock! You only have {max_quantity} {item}(s). Please enter a valid quantity.\n")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")
        
        remove_from_box(item, quantity)
        


def showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts):
    # Total playtime
    total_time = (time.time() - start_time) / 60
    total_time = round(total_time + minutes_spent, 2)

    print("\n==============================================================\n")
    print("\n--- Game Stats ---")
    print(f"Total time played: {total_time} minutes")

    # Cheese bought summary
    print("\nCheese Bought:")
    for cheese_type, amount in cheese_bought.items():
        print(f"  {cheese_type}: {amount}")

    # Mice caught summary
    print("\nMice Caught:")
    for mouse_type, count in caught_mouse_dictionary.items():
        print(f"  {mouse_type}: {count}")

    # Hunt results
    print("\nHunt Results:")
    print(f"  Successful hunts:  {attempts['Successful hunt']}")
    print(f"  Unsuccessful hunts: {attempts['Unsuccessful hunt']}")

    # Win rate calculation
    total_hunts = attempts['Successful hunt'] + attempts['Unsuccessful hunt']
    if total_hunts > 0:
        success_rate = (attempts['Successful hunt'] / total_hunts) * 100
        print(f"  Hunt success rate: {success_rate:.2f}%")
    else:
        print("  No hunts conducted yet.")

    print("\n==============================================================\n")


def scavenge():
    global wood, food, game_time, points, player_health, box
    check_game_time = int(str(game_time)[:2])
                
    if 6 <= check_game_time <= 18:
        risk1, risk2 = 0.1, 0.2  # Daytime risks
    else:
        print("ProTip: The elders say it's best to avoid wondering around once dusk falls. Something lurks in the shadows of these unknown realms after dark.")
        user_input_timewise = input("Do you want to still continue to hunt? ['yes' or 'no'] ")
        if user_input_timewise.lower() == "no":
            break

        risk1, risk2 = 0.5, 0.6  # Night risks

    if box["created"] == False:
        print("You don’t have a storage crate yet! Even if you find anything, you can’t store it!")
        print("Head out to the carpenter first to get yourself one.\n\n")
        user_input = input('Do you still want to continue? ["yes" or "no"] ')
        if user_input.lower() == "no":
            return
    
    game_time = increase_time(game_time, 1)
    
    success_scavenge_messages = [
        "You carefully search the forest floor and find some dry twigs.. \nThey can be handy!",
        "You dig through the leaves and discover a few sturdy branches.. \nDefinitely some good loots for the day!",
        "You stumble upon a fallen tree branch, perfect for crafting.. \nThe carpenter will be delighted!",
        "You gather some scattered sticks from the ground.. \nGod's mercy, indeed!",
        "You rummage through the underbrush and find a pile of firewood.. \nCan definitely chop it up and put to good use!"
    ]

    fail_scavenge_messages = [
        "You carefully search the forest floor and find some dry twigs.. \nOh no- They are too brittle!",
        "You dig through the leaves and discover a few sturdy branches.. \nNvm- They are too easily snappable!",
        "You stumble upon a fallen tree branch, perfect for crafting.. \nWelp- It's too heavy to carry it back to the carpenter!",
        "You gather some scattered sticks from the ground.. \nDrop and run- Termites!",
        "You rummage through the underbrush and find a pile of firewood.. \nHard luck- It's soaking wet!"
    ]

    food_options = ["apple", "banana", "berries", "mushrooms", "frog"]  # Replaced fish with frog
    food_found = random.choice(food_options)

    if 6 <= check_game_time <= 18:
        risk1, risk2 = 0.1, 0.2  # Daytime risks
    else:
        risk1, risk2 = 0.5, 0.6  # Night risks

    event_roll = random.random()
    random_index = random.randint(0, 4)  # 5 elements, so index range 0-4

    if event_roll < 0.25:
        # print("You found usable wood!")
        msg = success_scavenge_messages[random_index]
        if box["created"] == False:
            show_description(msg)
            print("\nToo bad you don't have a storage chest to store it in..")
            print("You earned no XP!")
        elif box["space"] == 0:
            show_description(msg)
            print("\nYou've run out of space in your storage crate! Get rid of some items or ask the Old Carpenter for a bigger storage limit.")
        else:
            show_description(msg)
            wood += random_index + 1  # Add wood if successful
            points += 2
            # add_to_box(item, type=None, quantity=1)
            add_to_box("wood", "wood", random_index + 1)
            print("\nYou earned 2 XP!\n")
    elif event_roll < 0.50:
        msg = fail_scavenge_messages[random_index]
        # print("You found unusable wood.")
        if box["created"] == False:
            show_description(msg)
            print("\nYou didn't have any storage crate anyways..")
            print("You earned no XP!")
        elif box["space"] == 0:
            show_description(msg)
            print("\nYou didn't have space in your storage crate anyways..")
            print("You earned no XP!")
        else:
            show_description(msg)
            print()
    elif event_roll < 0.75:
        # print(f"You found some food: {food_found}!")
        msg = f"You scavenge the forest and discover a {food_found}. God's plan!"
        if box["created"] == False:
            show_description(msg)
            print("\nToo bad you don't have a storage chest to store it in..")
            print("You earned no XP!")
        elif box["space"] == 0:
            show_description(msg)
            print("\nYou've run out of space in your storage crate! Get rid of some items or ask the Old Carpenter for a bigger storage limit.")
            print("You earned no XP!")
        else:
            show_description(msg)
            points += 2
            food[food_found] += 1
            print("You earned 2 XP!\n")
            # add_to_box(item, type=None, quantity=1)
            add_to_box(food_found, "food")
    else:
        print("You didn’t find anything.")
        msg = "Despite your efforts, the forest floor yields nothing today."
        show_description(msg)
        print("You earned no XP!")

    # print(f"Wood collected: {wood}")



    # Random chance for encountering an animal
    num1 = random.random()
    if num1 < risk1:
        animal = Animal("tiger")
    elif num1 < risk2:
        animal = Animal("wild boar")
    else:
        animal = None

    if animal:
        player_health, alive = animal.attack(player_health)
        check_game_over()



# UNTESTED
def choose_trap(trap_option, current_trap):
    print("You currently have:")
    has_trap = False

    for trap in trap_option:
        print(f"{trap[0]}: will last {trap[1]} more hunts")
        if trap[1] > 0:
            has_trap = True

    if not has_trap:
        print("\nWARNING: You don't have any functional traps! Visit the carpenter to buy one.\n")
        return None

    while True:
        user_input = input("1. Wood-and-Spring Trap\n2. Reinforced Wood-Cage Trap\n3. Multilayer Glued-Board Trap\n")
        if user_input.isdigit() == True:
            user_input = int(user_input)
        else:
            print("Invalid input.")
            continue

        if user_input < 1 or user_input > 3:
            print("Invalid input.")
            continue

        if trap_option[user_input-1][1] == 0:
            print(f"You don't a functional {trap_option[user_input-1][0]}")
            continue
        else:
            current_trap = trap_option[user_input-1][0]
            return current_trap


def count_trap(trap_option):
    total = 0
    for i in trap_option:
        total += i[1]
    return total

def update_trap_option(trap_option, trap_name, trap_menu):
    for i in range(len(trap_option)):
        if trap_option[i][0] == trap_name:
            trap_option[i][1] += trap_option[i][3]
    return trap_option

# TRAP = (("Wood-and-Spring Trap", 10, 5, 10), ("Reinforced Wood-Cage Trap", 30, 15, 20), ("Multilayer Glued-Board Trap", 50, 50, 15))
# format: name - wood - gold - lasting duration(turns/hunts) - making duration (turns) [consider adding later]


def buy_trap(wood: int, gold: int, points: int, trap_menu: tuple, trap_option: list) -> tuple:

    while True:

        print("\nOld Carpenter:")
        print(f"You have {gold} gold to spend.\n")


        print(f"FOR TESTING ========= Wood: {wood}, Gold: {gold}, Points: {points}", "Trap options:", trap_option)
        print("At my age, I can only make one trap of a kind in one go")
        user_input = input("\nEnter '0' when you're done shopping. To buy, choose [trap number]:\n1. Wood-and-Spring Trap\n2. Reinforced Wood-Cage Trap\n3. Multilayer Glued-Board Trap\n")

        if user_input.isdigit() == True:
            user_input = int(user_input)
        else:
            print("Old Carpenter: I did not understand.")
            print()
            continue

        if user_input < 0 or user_input > 3:
            print("Old Carpenter: I did not understand.")
            print()
            continue

        if user_input == 0:
            return (wood, gold, points, trap_option)

        if points < 100:
            if user_input != 1:
                print(f"Old Carpenter: You do not have enough XP to unlock this item yet. Choose another trap.\n")
                continue

        if points < 300:
            if user_input == 3:
                print(f"Old Carpenter: You do not have enough XP to unlock this item yet. Choose another trap.\n")
                continue

        if trap_option[user_input-1][1] > 0:
            print(f"Old Carpenter: Your current {trap_option[user_input-1][1]} is still in fine shape! Come back when it's broken!\n")
            continue

        if wood < trap_menu[user_input-1][1]:
            print("Old Carpenter: You didn't bring enough wood. Select a different trap.\n")
            continue

        if gold < trap_menu[user_input-1][2]:
            print("Old Carpenter: You don't seem to have enough gold, kid. Select a different trap.\n")
            continue

        trap_name = trap_menu[user_input-1][0]
        quantity = 1
        wood -= trap_menu[user_input-1][1]*quantity
        gold -= trap_menu[user_input-1][2]*quantity
        trap_option = update_trap_option(trap_option, trap_name, trap_menu)
        print(f"Old Carpenter: \nI can make {quantity} {trap_name} for you worries, no problem! It will last you {trap_menu[user_input-1][3]} hunts.")
        print()
        print(trap_art())
        print()
        print(f"You got a {trap_name}!\n")
        print("You earned 10 XP!\n")
        points += 10
        # add_to_box(item, type=None, quantity=1)
        add_to_box(trap_name, "trap")

    return (wood, gold, points, trap_option)



def visit_carpenter(menu, trap_option, wood, gold, points, carpenter_visit, cheese, current_trap, name):
    # ALLOW OPTION TO FIXXX TRAP??
    global box

    if carpenter_visit == 0:
        msg = "Old Carpenter:\nI thought I heard some noise last night. But there's just been so much noise lately, innit?\n"
        msg = msg + "Anyways, sorry I can't let you stay here if that's what ya're here for, mate-\n"
        msg = msg + "If you got some wood, I might be able to get you something to help you survive better on your own\n"

        show_description(msg)

        user_input = input("Press Enter to give wooden crate... ")

        msg = "\n\nOld Carpenter:\n"
        msg = msg + "A fine piece, I daresay. Withstood the forces of time but the pine wood can still be utilised. Wait here\n"
        msg = msg + "*chop* .. *grind* .. *scraping* .. *thumping* .. \n"
        show_description(msg)

        print()
        print(trap_art())
        print()

        print("\nYOU GOT WOOD-AND-SPRING TRAP!\n")

        msg = "I have used some scrap wood and a few bits and pieces from my other projects to make you this. Thought you might find it helpful.\n"
        msg = msg + "You are welcome, kid."
        show_description(msg)

        print()
        print(box_art())
        print()

        print("\nYOU HAVE A STORAGE CRATE NOW! YOU CAN STORE YOUR ITEMS IN IT!\n")
        trap_option[0][1] += 1
        carpenter_visit += 1
        wood -= 10

        box["created"] = True
        box["space"] += 15 #(+20 - 5 bc 5 taken up by trap)
        # add_to_box(item, type=None, quantity=1)
        add_to_box(trap_option[0][0], "trap")

        return (wood, gold, points, trap_option, carpenter_visit)

    else:
        # ADD OPTION TO INCREASE SIZE OR STORAGE
        while True:

            user_input = input("Old Carpenter: Ah didn't forget the old fella, I see. How can I help you?\n1. Make Trap\n2. View inventory\n3. Leave shop\n")

            if user_input.isdigit() == True:
                user_input = int(user_input)
            else:
                print("Old Carpenter: I did not understand.")
                print()
                continue

            if user_input < 1 or user_input > 3:
                print("Old Carpenter: I did not understand.")
                print()
                continue

            if user_input == 1:
                result = buy_trap(wood, gold, points, menu, trap_option)
                # return (wood, gold, points, trap_option)
                wood = result[0]
                gold = result[1]
                points = result[2]
                trap_option = result[3]

            elif user_input == 2:
                # display_inventory(wood, gold, cheese, trap, name)
                display_inventory(wood, gold, cheese, current_trap, name)                     # wood add hobe (CHEESE OPTION EO ADD KORA LAGBE)
                print()
            else:
                print("Old Carpenter: Goodbye, then..")
                time.sleep(2)
                break

        carpenter_visit += 1
        return (wood, gold, points, trap_option, carpenter_visit)

def increase_time(game_time, increment):
    game_time = int(game_time[:2])
    game_time = (game_time + increment) % 24
    game_time = str(game_time) + " 00"
    return game_time

def count_food():
    global food

    total = 0
    for i in food.values():
        total += i
    return total



def output_box():
    global box
    
    if not box["created"]:
        print("You currently have no storage crate.")
        return
    
    if not box["content"]:
        print("Your storage crate is empty.")
        return
    
    print("Storage Crate Contents:")
    for item, quantity in box["content"].items():
        print(f"- {item}: {quantity}")

def remove_from_box(item, quantity=1):
    global box
    
    if not box["created"]:
        print("You have no Storage Crate yet")
        return
    
    if item not in box["content"]:
        print(f"{item} is not in the storage crate.")
        return
    
    space_recovered = 5 if item == "trap" else 3 if item == "medicine" else 2 if item == "mouse" else 1
    
    items_removed = min(quantity, box["content"][item])
    box["content"][item] -= items_removed
    box["space"] += items_removed * space_recovered
    
    if box["content"][item] == 0:
        del box["content"][item]
    
    print(f"Removed {items_removed} {item}(s) from the crate. Remaining space: {box['space']}")


def add_to_box(item, type=None, quantity=1):
    global box
    
    if not box["created"]:
        print("You have no Storage Crate yet")
        return
    
    # Determine space needed for item
    space_needed = 5 if type == "trap" else 3 if type == "medicine" else 2 if type == "mouse" else 1
    
    items_added = 0
    
    for _ in range(quantity):
        if box["space"] < space_needed:
            print(f"Only {items_added} {item}(s) added to the crate because space ran out.")
            return
        
        box["space"] -= space_needed
        if item in box["content"]:
            box["content"][item] += 1
        else:
            box["content"][item] = 1
        
        items_added += 1
    
    print(f"{items_added} {item}(s) added to the crate. Remaining space: {box['space']}")

def tutorial():
    while True:
        print()
        intro()
        val1 = travel_to_camp()
        if val1 == False:
            break

        while True:
            tutorial_trap_result = setup_trap()
            if tutorial_trap_result == False:
                break
            tutorial_trap = tutorial_trap_result[0]
            if tutorial_trap == "Wood-and-Spring Trap" or tutorial_trap == "Hot Tub Trap":
                tutorial_enchant = True
                tutorial_trap = "One-time Enchanted " + tutorial_trap

            tutorial_sound = sound_horn(tutorial_trap_result)
            if tutorial_sound == False:
                break
            #cheddar -= 1
            print()
            user_input = input('Press Enter to continue training and "no" to stop training: ')
            user_input = user_input.strip()
            user_input = user_input.lower()
            if user_input == '':
                continue

            if user_input == chr(27) or user_input == "no":
                break

        if tutorial_trap_result == False:
            break

        if tutorial_sound == False:
            break

        if user_input == chr(27) or user_input == "no":
            break




def visit_trader():
    global trader_visit, gold, points, box

    # Check if the player has visited the trader before
    if trader_visit == 0:
        print("Trader:\n")
        msg = "Never seen you around here. First time?\nNo worries! If you got mice, I got 'em gold."
    else:
        msg = "Welcome back to my Trading Hut!"
    
    show_description(msg)

    # Check if the player has a storage crate
    if box["created"] == False:
        print("\nDon't seem to have a Storage Crate yet, huh? Swing by that mad ol' carpenter asap!\n")
        return
    
    # Prepare the current list of mice in the box
    current_dict = {}
    mouse_list = ["Brown", "Field", "Grey", "White", "Tiny"]
    
    # Count the occurrences of each mouse type in the box content
    for key in box["content"].keys():
        if key in mouse_list:
            if key in current_dict.keys():
                current_dict[key] += 1
            else:
                current_dict[key] = 1

    # Output the available mice in the current_dict
    print("Available items in your storage crate:")
    for mouse, qty in current_dict.items():
        print(f"{mouse}: {qty}")
    
    while True:
        # Ask user for the item to remove
        item = input("Enter the name of the item you want to remove (or type 'cancel' to exit): ").strip()
        
        if item.lower() == 'cancel':
            print("Removal process cancelled.\n")
            return
        
        # Check if the item is in the available items list
        if item not in current_dict:
            print("Item not found in the storage crate. Please enter a valid item, or type 'cancel' to exit.\n")
            continue
        
        max_quantity = current_dict[item]  # Get the available quantity of the item
        
        while True:
            # Ask user for the quantity to remove
            quantity = input(f"Enter the quantity of {item} to remove (Max: {max_quantity}), or type 'cancel' to exit: ").strip()
            
            if quantity.lower() == 'cancel':
                print("Removal process cancelled.\n")
                return
            
            try:
                quantity = int(quantity)
                if quantity < 1:
                    print("Please enter a valid quantity (1 or more), or type 'cancel' to exit.\n")
                elif quantity > max_quantity:
                    print(f"Insufficient stock! You only have {max_quantity} {item}(s). Please enter a valid quantity, or type 'cancel' to exit.\n")
                else:
                    # Update the box content
                    box["content"][item] -= quantity
                    if box["content"][item] == 0:
                        del box["content"][item]  # Remove the item from the box if quantity reaches 0
                    
                    # Update the current_dict as well
                    current_dict[item] -= quantity
                    if current_dict[item] == 0:
                        del current_dict[item]  # Remove the item from the dictionary
                    
                    print(f"{quantity} {item}(s) removed successfully.\n")
                    break  # Exit the inner loop to ask for another item or to cancel
            except ValueError:
                print("Invalid input. Please enter a numeric value, or type 'cancel' to exit.\n")


def visit_witchdoctor():
    global player_health, doc_visit, gold, box

    # Check if the player has visited the Witch Doctor before
    if doc_visit == 0:
        print("Witch Doctor:\n")
        msg = "Ah, a fresh face! First time here? I'm the Witch Doctor, and I can help with your health and more, if you're willing to pay the price."
    else:
        msg = "Ah, you've returned! I see you're in need of my healing touch again."

    show_description(msg)

    # If health is full, no need for restoration
    if player_health == 100:
        print("\nYour health is already full. No need for healing right now.\n")
        return

    # If health is critically low, prompt for operation
    if player_health < 20:
        choice = input(f"Your health is critically low ({player_health}). Would you like to undergo an operation to restore it to full health? (yes/no): ").strip().lower()
        if choice == 'yes':
            if gold >= 80:
                gold -= 80
                player_health = 100
                print(f"\nYou underwent the operation! Your health is now {player_health}. You paid 80 gold.\n")
                doc_visit += 1
                return
            else:
                print("\nYou don't have enough gold for the operation. Come back when you have more!\n")
                return
        elif choice == 'no':
            print("\nAlright, be careful! Come back if you change your mind.\n")
            return
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.\n")
            return

    # Ask player to choose a health potion
    print("\nHere are the health potions I offer:")
    print("1. Health Potion (Restores 20 health) - 40 gold")
    print("2. Health Potion (Restores 50 health) - 75 gold")
    print("3. Health Potion (Restores 100 health) - 100 gold")                              # do as show_description(msg)

    while True:
        choice = input("Which potion would you like to buy? (1/2/3), or type 'cancel' to exit: ").strip().lower()

        if choice == 'cancel':
            print("Process cancelled.\n")
            return

        if choice == '1':
            potion_name = "Health Potion (+20 Health)"
            potion_cost = 40
            potion_effect = "Restores 20 health"
            health_increase = 20
        elif choice == '2':
            potion_name = "Health Potion (+50 Health)"
            potion_cost = 75
            potion_effect = "Restores 50 health"
            health_increase = 50
        elif choice == '3':
            potion_name = "Health Potion (+100 Health)"
            potion_cost = 100
            potion_effect = "Restores 100 health"
            health_increase = 100
        else:
            print("\nInvalid choice. Please enter '1', '2', or '3'.\n")
            continue

        # Check if the player has enough gold
        if gold >= potion_cost:
            # Check if the player has space in the storage crate
            if len(box["content"]) < 10:  # Assuming the crate can hold 10 items
                # Deduct gold and add potion to the storage crate
                gold -= potion_cost
                if potion_name in box["content"]:
                    box["content"][potion_name] += 1
                else:
                    box["content"][potion_name] = 1
                print(f"\nYou bought a {potion_name} for {potion_cost} gold! {potion_effect}. You now have {box['content'][potion_name]} in your crate.\n")
            else:
                print("\nYou don't have enough space in your storage crate for a potion!\n")
        else:
            print(f"\nYou don't have enough gold to buy a {potion_name}.\n")



# allow tutorial to be visited anytime later
def main():
    global trap_option, trap_cheese, current_trap, food, wood, gold, points, carpenter_visit, game_over, game_time, player_health, box, trader_vist
    
    TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")
    CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
    TRAP = (("Wood-and-Spring Trap", 10, 5, 10), ("Reinforced Wood-Cage Trap", 30, 15, 20), ("Multilayer Glued-Board Trap", 50, 50, 15))
    # format: name - wood - gold - lasting duration(turns/hunts) - making duration (turns) [consider adding later]

    # add time to make for each trap (speed up korte extra gold: double its price)
    # vary hunt chance based on trap too (LATER)[add buffs like 2% or 3%]


    start_gold = (200, 150, 125)
    game_over = False
    box = {"created": False, "space": 0, "content":{}}

    # box er content ki dictionary banabo naki list

    doc_visit = 0
    trader_vist = 0
    carpenter_visit = 0                                                                              # set wood alada bhabe (need to collect)
    points = 0
    gold = 0
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap_option = [["Wood-and-Spring Trap", 0], ["Reinforced Wood-Cage Trap", 0], ["Multilayer Glued-Board Trap", 0]]
    food = {"apple": 0, "banana": 0, "berries": 0, "mushrooms": 0, "frog": 0}

    trap_cheese = None
    current_trap = None

    enchant = False
    wood = 0
    player_health = 100
    game_time = "09 00"

    called_functions = {
        "level_check_1": False,
        "level_check_2": False
    }

    caught_mouse_dictionary = {}
    for i in TYPE_OF_MOUSE:
        caught_mouse_dictionary[i] = 0

    minutes_spent = 0
    attempts = {"Successful hunt": 0, "Unsuccessful hunt": 0}
    cheese_bought = {"Cheddar": 0, "Marble": 0, "Swiss": 0}
    start_time = time.time()


    intro_text = "In this thrilling adventure game, you step into the boots of a skilled hunter on a daring quest to outwit and capture elusive mice.\nYou must use strategy and be cunning to lure your tiny targets while carefully managing your limited gold.\nEvery decision counts—choose the right cheese, set the perfect trap, and adapt to the ever-changing challenges ahead.\nAs you progress, you'll earn gold, unlock powerful upgrades, and discover new tools to catch even rarer and trickier mice.\nBut beware! Your ultimate goal is to reach 500 XP before your gold runs dry.\nA true hunter knows that every misstep could mean an empty purse and a failed quest.\nWill you rise to the challenge, master the hunt, and claim your place among the legendary trappers?\nThe adventure begins now!"
    game_intro(intro_text)
    print()
    print("What's ye name, Hunter?")
    name = input()
    flag = is_valid_name(name)
    flag_check = 3

    while flag != True and flag_check != 0:
        print(f"You have {flag_check} tries remaining")
        name = input("Re-enter your name, Hunter: ")
        flag = is_valid_name(name)
        flag_check -= 1

    if flag != True:
        name = "Bob"
        print(f"\nOur systems has decided to name you Bob!\n")

    print("Welcome to the Kingdom, Hunter", name+"!")
    print("\nBefore we begin, let's train you up!")
    user_input1 = input('Press "Enter" to start training or "skip" to Start Game: ')

    if user_input1 != 'skip':
        tutorial()

    if enchant == False:
        trap_cheese = None

    while True:
        print()
        difficulty = input("Choose game difficulty:\n1. Noob\n2. Adventurer\n3. Survivalist\n")

        if difficulty.isdigit() == True:
            difficulty = int(difficulty)
        else:
            print("Invalid option.\n")
            continue

        if difficulty < 1 or difficulty > 3:
            print("Invalid option.\n")
            continue
        else:
            if difficulty == 1:
                print("Oh my.. with such little nerve, you might not be able to come out alive from what awaits you ahead..")
            elif difficulty == 2:
                print("A rational thinker, I see. Too scared to risk it, are we..")
            else:
                print("Daring, are we? We all sometimes live to regret the decisions we make. Will you too..")
            break

    # add je you check your pockets to find name is Bob

    print("\nStarting...\n")
    time.sleep(2)
    print()
    gold += start_gold[difficulty-1]
    message = "Stranded.\n\nLost.\n\nScavenging...\n\nYou find a broken wooden crate behind a towering, damp oak tree..\n"
    show_description(message)
    r_press = input("Press Enter to check its contents...")
    message = ""
    message = message + f"\nYOU FOUND {gold} GOLD!\n"
    message = message + "\nBefore you can start hunting you need a trap.\nI've heard there's an Old Carpenter who still lives in these god-foresaken lands\nTake the wooden crate to him. I've heard the man still got plenty of tricks up his sleeve."
    message = message + "\nHe will get the job done but often for a charge. Maybe he'll feel pity for you and get started with a free trap.."
    show_description(message)
    wood += 10

    while True:
        if game_over == True:
            if points < 500:
                print(f"Thanks for joining our adventure, Hunter {name}! Better luck next time.")
                time.sleep(3)
                print("\nDon't forget to check out your achievements:\n\n")
                showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts)
                print("\nStay tuned for upcoming versions~")
                key = input("Enter any key to exit... ")
                break
            else:
                print(f"Congrats on surviving this adventure, Hunter {name}!")
                print("There are moments I doubted you but you surely knew your way in the face of crisis!")
                time.sleep(3)
                print("\nDon't forget to check out your achievements:\n\n")
                showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts)
                print("\nStay tuned for upcoming versions~")
                key = input("Enter any key to exit... ")
                break


        print()

        if trap_cheese == None:
            enchant = False
        elif trap_cheese.lower() == "swiss":
            enchant = True
        else:
            enchant = False

        print(f"Time: {game_time}   Health: {player_health}\n")

        print("What do ye want to do now, Hunter",name+'?')
        # print("=================================")
        # print("Current cheese is:", trap_cheese)
        # print("=================================")
        print(get_game_menu())

        while True:
            cheese_count = 0
            for i in range(len(cheese)):
                cheese_count += cheese[i][1]

            if count_food() == 0:
                print("Pro Tip: You don't have any food! You can try scavenging nearby for food or visit the Witch Doctor to buy off some of her rations.")
                print("REMEMBER: When unfed for too long, you can die from starvation!\n")
            
            if current_trap == None:
                if trap_option[0][1] + trap_option[1][1] + trap_option[2][1] != 0:
                    print("Pro Tip: You still have functional traps. Choose one!")                      
                else:
                    print("Pro Tip: Before joining the hunt, you need a trap. Heading to the Carpenter might be a wise idea!")
            else:
                if cheese_count == 0:
                    print("Pro Tip: Before joining the hunt, you need cheese. Heading to the Cheese Shop might be a wise idea!")
                else:
                    if trap_cheese == None:
                        print("Pro Tip: Get started by placing your cheese on the trap!")
                    elif has_cheese(trap_cheese, cheese) == 0:
                        print("Pro Tip: Call it a cheesy advice but you know a cheese is only good for a hunt when placed in a trap, right?")
                    else:
                        print("Looking like a pro right there! Ready to hunt?")


            user_input2 = (input("Enter a number between 1 and 10: "))
            if user_input2.isdigit() == True:
                user_input2 = int(user_input2)
            else:
                print("Invalid input.\n\n")
                continue
            if user_input2 < 1 or user_input2 > 10:
                print("Must be between 1 and 10.\n\n")
                continue
            else:
                break
        print()

        if user_input2 == 11:
            tutorial()

        elif user_input2 == 10:
            showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts)

        elif user_input2 == 9:
            current_trap = choose_trap(trap_option, current_trap)
            game_time = increase_time(game_time, 1)

        elif user_input2 == 8:
            print("Travelling to Old Carpenter...\n\n")
            game_time = increase_time(game_time, 2)

            time.sleep(3)
            result = visit_carpenter(TRAP, trap_option, wood, gold, points, carpenter_visit, cheese, current_trap, name)
            # return (wood, gold, points, trap_option, carpenter_visit)
            wood = result[0]
            gold = result[1]
            points = result[2]
            trap_option = result[3]
            carpenter_visit = result[4]

            print("Returning..\n\n")
            time.sleep(3)
            game_time = increase_time(game_time, 2)

        elif user_input2 == 7:
            print("Travelling to Witch Doctor...\n\n")
            game_time = increase_time(game_time, 2)
            visit_witchdoctor()
            print("WitchDoctor: Don't come crying to me with your sick ass anytime soon I hate it!\n")
            print("Returning..\n\n")
            time.sleep(3)
            game_time = increase_time(game_time, 2)
            pass

        elif user_input2 == 6:
            print("Travelling to Trader...\n\n")
            game_time = increase_time(game_time, 2)
            visit_trader()
            print("Trader: Pleasure doing business with you!\n")
            print("Returning..\n\n")
            time.sleep(3)
            game_time = increase_time(game_time, 2)

        elif user_input2 == 5:
            scavenge()
            print("Returning..\n\n")
            time.sleep(3)
            # game_time = increase_time(game_time, 1)               # HANDLED INSIDE FUNCTION

        elif user_input2 == 4:
            if enchant == True:
                cheese_val = change_cheese(name, current_trap, cheese, True)
                #print(f"\nAfter change cheese: {cheese_val}\n")
            else:
                cheese_val = change_cheese(name, current_trap, cheese)

            trap_cheese = cheese_val[1]

            print("Returning..\n\n")
            time.sleep(3)
            game_time = increase_time(game_time, 1)


        elif user_input2 == 3: #untested

            print("Travelling to Cheese Shop... \n\n")
            time.sleep(3)
            game_time = increase_time(game_time, 2)

            print("Cheese Dealer: Welcome to The Cheese Shop!")
            cheese_shop_art()
            print()

            while True:
                cheese_shop_intro()
                user_input3 = input()

                if user_input3.isdigit() == True:
                    user_input3 = int(user_input3)
                else:
                    print("Cheese Dealer: I did not understand.")
                    print()
                    continue

                if user_input3 < 1 or user_input3 > 3:
                    print("Cheese Dealer: I did not understand.")
                    print()
                    continue

                if user_input3 == 1:                        # need to do something with cheese dictioanry
                    print("Cheese Dealer: Welcome! Don't be stingy around here.\nThe more expensive cheese will help you have more successful and rewarding hunts!")
                    value = buy_cheese(gold, points)
                    gold -= value[0]
                    cheese[0][1] += value[1][0]
                    cheese[1][1] += value[1][1]
                    cheese[2][1] += value[1][2]
                    cheese_bought["Cheddar"] += value[1][0]
                    cheese_bought["Marble"] += value[1][1]
                    cheese_bought["Swiss"] += value[1][2]
                    #print(cheese)
                    print()
                elif user_input3 == 2:
                    # display_inventory(wood, gold, cheese, trap, name)
                    display_inventory(wood, gold, cheese, current_trap, name)
                    print()
                else:
                    print("Cheese Dealer: Goodbye, then..")
                    print("Returning...")
                    time.sleep(2)
                    game_time = increase_time(game_time, 2)
                    break

        elif user_input2 == 1:
            # show final stats
            print(f"Thanks for joining our adventure, Hunter {name}!")
            time.sleep(3)
            print("\nDon't forget to check out your achievements:\n\n")
            showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts)
            key = input("Enter any key to exit... ")
            break

        else: #user_input = 2
            results = hunt(gold, cheese, trap_cheese, enchant, points, called_functions, attempts, caught_mouse_dictionary, game_over)
            gold = results[0]
            points = results[1]
            cheese = results[2]
            called_functons = results[3]
            attempts = results[4]
            caught_mouse_dictionary = results[5]
            game_over = results[6]



if __name__ == '__main__':
    main()





# implement health reducing auto (relation with food or autoset since last full health restoration)