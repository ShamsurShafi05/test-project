import random
import time

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
        



#cheese = [["Cheddar", 0], ["Marble", 1], ["Swiss", 1]]       #personal testing er jonno cheese kine rakhsilam

def get_game_menu():
    return "1. Exit game\n2. Join the Hunt\n3. The Cheese Shop\n4. Change Trap Cheese\n5. Check stats\n"


def check_game_over(gold, cheese, points):
    if points >= 500:
        return True

    if gold < 10:
        total = 0
        for i in cheese:
            total += i[-1]

        if total == 1:
            print("Your survival comes down to this cheese.\n")
            print("Here's our special ritual that is believed to help a long generation of hunters alike yourself:\n")
            print(r"""
                    Waluuudulan dandanali
                    Watoblutob tobtobali
            """)
            print()
            return False

        if total == 0:
            print("Sorry you've run out of cheese and do not have any more gold to make purchases!")
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
    print(white_mouse())
    print(grey_mouse())
    print(brown_mouse())
    print("=========================================================")


def level_check_2():
    print("=========================================================")
    print("Congrats you have unlocked new items:\n")
    print("NEW CHEESE: SWISS")
    print("ENCHANTMENT UNLOCKED")
    print(tiny_mouse())
    print("=========================================================")


def hunt(gold, cheese, trap_cheese, enchant, points, called_functions, attempts, caught_mouse_dictionary, game_over_status):

    hunt = 0
    succes_streak = 0

    while True:
        game_over_status = check_game_over(gold, cheese, points)
        if game_over_status == True:
            break

        print("Gold:", str(gold) + ", XP:", points)

        # Stopping condition: Sound the horn by typing "yes": #stop hunt
        print("\nSound the horn to call for the mouse...")
        sound_input = input('Sound the horn by typing "yes". Type "stop" to end hunting session: ')
        if sound_input.isdigit() == True:
            print("Invalid input.\n")
            continue

        if sound_input.lower() == "stop":
            break

        if sound_input == '' or sound_input != "yes":
            print("You did not properly sound the horn. Hunt wasted.")
            hunt += 1
        else:
            print("\n~~ ~ ~~~~ ~~~ ~~ ~~ ~ ~~~~\n")
            if trap_cheese == None:
                hunt += 1
                print("Nothing happens. You are out of cheese!")

            else:
                cheese, status = consume_cheese(trap_cheese, cheese)
                if status == False:
                    hunt += 1
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

                    else:
                        #print("H1:", hunt)
                        hunt += 1
                        attempts["Unsuccessful hunt"] += 1
                        #print("H2:", hunt)
                        print("The wilderness can sometimes be cruel. Hunt unsuccessful")

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
    print("Version launch - 1.1 (2025)")
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
    print("Larry: I'm Larry. I'll be your hunting instructor.")


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
    print("Left: High Strain Steel Trap")
    print("Right: Hot Tub Trap")
    trap_input = input('Select a trap by typing "left" or "right": ').strip()


    trap_input = trap_input.strip()
    if trap_input == chr(27):
        return False

    if trap_input.lower() == "left":
        print("Larry: Excellent choice.")
        print('Your "High Strain Steel Trap" is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        return ("High Strain Steel Trap", 1)
    elif trap_input.lower() == "right":
        print("Larry: Excellent choice.")
        print('Your "Hot Tub Trap" is now set!')
        print("Larry: You need cheese to attract a mouse.")
        print("Larry places one cheddar on the trap!")
        return ("Hot Tub Trap", 1)
    else:
        print("Invalid command! No trap selected.")
        print("Larry: Odds are slim with no trap!")
        return ("Cardboard and Hook Trap", 0)


def sound_horn(trap_result):                                    #CHANGE
    print("Sound the horn to call for the mouse...")
    horn_sound = input('Sound the horn by typing "yes": ').lower()
    horn_sound = horn_sound.strip()
    horn_sound = horn_sound.lower()

    if horn_sound == chr(27):
        return False

    if horn_sound != "yes" and trap_result == ("Cardboard and Hook Trap", 0): #no trap, no horn
        print("Nothing happens.")

    elif horn_sound == "yes" and trap_result != ("Cardboard and Hook Trap", 0):
        print("Caught a Brown mouse!\nCongratulations. Ye have completed the training.\nGood luck~")
        return "success"

    elif horn_sound == "yes" and trap_result == ("Cardboard and Hook Trap", 0):
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




CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))

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
    

def cheese_shop_intro():
    print("How can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop")


def buy_cheese(gold: int, points: int) -> tuple:

    remain = gold
    spent = 0

    cheddar = 0
    marble = 0
    swiss = 0

    while True:

        print(f"You have {gold} gold to spend.")
        user_input = input("Enter 'back' when you're done shopping. To buy, state [cheese quantity]: ")

        if len(user_input) == 0:
            print("Invalid input! Try again.", end = '\n\n')
            continue

        #returning to main menu
        if user_input.lower() == "back":
            return (spent, (cheddar, marble, swiss))

        user_input = user_input.split()
        cheese = user_input[0].lower()

        #checking is cheese name is valid
        if cheese not in ["cheddar", "marble", "swiss"]:
            print(f"We don't sell {cheese}!")
            continue
        else:
            if points < 100:
                if cheese != "cheddar":
                    print(f"You do not have enough XP to unlock this item yet. Choose another cheese.")
                    continue
            elif points < 300:
                if cheese == "swiss":
                    print(f"You do not have enough XP to unlock this item yet. Choose another cheese.")
                    continue


        #checking if quantity is missing
        if len(user_input) == 1:
            print("Missing quanitity.")
            continue
        else:
            quantity = user_input[1]

        #checking if quantity enteres is not a number
        if quantity.isnumeric() == False:
            print("Invalid quantity.")
            continue
        else:
            cheese_bought = int(quantity)

        #checking if quantity entered is non-positive
        if cheese_bought <= 0:
            print("Must purchase positive amount of cheese.")
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
            print(f"Successfully purchase {cheese_bought} {cheese}.", end = " ")
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
            print("Insufficient gold.")
            continue


def display_inventory(gold: int, cheese: list, trap: str, name: str) -> None:

    character_art(name)
    print(f"Hunter, you currently have:\n")
    print("Gold -", gold)
    print("Cheddar -", cheese[0][1])
    print("Marble -", cheese[1][1])
    print("Swiss -", cheese[2][1])
    print("Trap -", trap)
    print("``````````````````````````````````")

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



def main():
    TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")
    start_gold = (200, 150, 125)
    game_over = False
    gold = 0                                                           # set initial amount based on difficulty
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    points = 0
    cheese_to_use = None
    trap = "Cardboard and Hook Trap"                                    # add more weapons
    enchant = False

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
                if tutorial_trap == "High Strain Steel Trap" or tutorial_trap == "Hot Tub Trap":
                    tutorial_enchant = True
                    tutorial_trap = "One-time Enchanted " + trap

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

    print("\nStarting...\n")
    time.sleep(2)
    print()
    gold += start_gold[difficulty-1]
    message = "Stranded.\n\nLost.\n\nScavenging...\n\nYou find a broken wooden crate behind a towering, damp oak tree..\n"
    message = message + f"YOU FOUND {gold} GOLD!"
    message = message + "\nYou are a skillful craftsman. You decide to turn the wooden crate into a makeshift trap..\n"
    message = message + f"YOU HAVE {trap}! Use it well"

    show_description(message)
    trap_cheese = None

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

        print("What do ye want to do now, Hunter",name+'?')
        # print("=================================")
        # print("Current cheese is:", trap_cheese)
        # print("=================================")
        print(get_game_menu())

        while True:
            cheese_count = 0
            for i in range(len(cheese)):
                cheese_count += cheese[i][1]

            if cheese_count == 0:
                print("Pro Tip: Before joining the hunt, you need cheese. Heading to the Cheese Shop might be a wise idea!")
            else:
                if trap_cheese == None:
                    print("Pro Tip: Get started by placing your cheese on the trap!")
                elif has_cheese(trap_cheese, cheese) == 0:
                    print("Pro Tip: Call it a cheesy advice but you know a cheese is only good for a hunt when placed in a trap, right?")
                else:
                    print("Looking like a pro right there! Ready to hunt?")


            user_input2 = (input("Enter a number between 1 and 5: "))
            if user_input2.isdigit() == True:
                user_input2 = int(user_input2)
            else:
                print("Invalid input.")
                continue
            if user_input2 < 1 or user_input2 > 5:
                print("Must be between 1 and 5.")
                continue
            else:
                break
        print()

        if user_input2 == 5:
            showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts)


        elif user_input2 == 4:
            if enchant == True:
                cheese_val = change_cheese(name, trap, cheese, True)
                #print(f"\nAfter change cheese: {cheese_val}\n")
            else:
                cheese_val = change_cheese(name, trap, cheese)

            trap_cheese = cheese_val[1]


        elif user_input2 == 3: #untested

            print("Welcome to The Cheese Shop!")
            cheese_shop_art()
            print()

            while True:
                cheese_shop_intro()
                user_input3 = input()

                if user_input3.isdigit() == True:
                    user_input3 = int(user_input3)
                else:
                    print("I did not understand.")
                    print()
                    continue

                if user_input3 < 1 or user_input3 > 3:
                    print("I did not understand.")
                    print()
                    continue

                if user_input3 == 1:                        # need to do something with cheese dictioanry
                    print("Pro Tip: Welcome! Don't be stingy around here.\nThe more expensive cheese will help you have more successful and rewarding hunts!")
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
                    display_inventory(gold, cheese, trap, name)
                    print()
                else:
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

