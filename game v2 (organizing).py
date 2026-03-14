import random
import time

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


def cheese_shop_art():
    art = r"""
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
    print(art)

# TRAP = (("Wood-and-Spring Trap", 10, 5, 10), ("Reinforced Wood-Cage Trap", 30, 15, 20), ("Multilayer Glued-Board Trap", 50, 50, 15))

def old_carpenter_shop_art():
    art = r"""
      _____________________________
     /                             \
    /      Old Carpenter's Shop     \
   /_________________________________\
        ||                      ||
       _||______________________||_
      |                            |
      |  ~~~~ TRAPS & PRICES ~~~~  |
      |                            |
      |  Wood-N-Spring  - 10W  5G  |
      |  R. Wood-Cage   - 30W 15G  |
      |  M. Glued-Board - 50w 50G  |
      |____________________________|
       (__________________________)
    """
    print(art)


def witchdoctor_chamber_art():
    art = r"""
      ________________________
     /                        \
    /   The WitchDoctor's Hut  \
   /____________________________\
        ||                ||
       _||________________||__
      |                       |
      |    HEALTH SERVICES    |
      |                       |
      |  +20 Health   -  40 G |
      |  +50 Health   - 100 G |
      |  Max Health   - 300 G |
      |  Critical Op  - 150 G |
      |_______________________|
       (_____________________)
    """
    print(art)


def trader_shack_art():
    art = r"""
      ________________________
     /                        \
    /     The Trader's Shack   \
   /____________________________\
        ||                ||
       _||________________||__
      |                       |
      | *SECRET GRAND REWARD* |
      |                       |
      |    Mice for Gold!     |
      |  ( + Mystery Deals)   |
      |_______________________|
       (_____________________)
    """
    print(art)


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

def wild_boar_art():
    str = r"""
        (\____/)  
        / `o  o'\ 
       (  (  _ ) )  
        \   ==  /  
        /'-.-.-'\  
       /   | |   \  
      ~    ~ ~    ~  
    WILD BOAR CHARGES!  
    """
    return str

def tiger_art():
    str = r"""
            /\     /\  
    *roar* {  `---'  }  
          {   O   O   }  
          ~~~>  V  <~~~  
             \  ~  /     /|
            /'-.-.-'\   / /
          {           }/_/ 
           ```````````  
         A TIGER STRIKES  
    """
    return str

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

def mouse_king():
    str = r"""
        /\     /\   
       (  >O_O<  )   MOUSE KING  
      /   \ | /   \   
     /  --  ^  --  \   
    (     -----     )  
     \   /     \   /  
      \_/       \_/  
    """
    return str

# ``````````````````````````````````````` CLASSES `````````````````````````````````````````````````````````````````````````````

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
        print(f"\nA {self.type} just attacked you! You lost {self.damage} HP\n\n")
    
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
        
# `````````````````````````````````` NAME SET AND CHECK`````````````````````````````````````````````````````````````````````````
def set_name():
    global name
    intro_text = "\n".join((
        "Welcome,\n\n",
        "The world has fallen into chaos.",

        "A once peaceful land is now overrun by swarms of relentless mice, their bites turning people into frenzied, mindless husks.",
        "Villages lie in ruins. Merchants abandon their stalls. Fear grips the hearts of those who remain.\n",

        "No one knows how it began, but whispers speak of a monstrous force behind it all: The Mouse King.",
        "A cunning, elusive beast said to control the plague, lurking in the shadows, watching.. waiting..\n",

        "And so, the call has gone out.",

        "Only the most skilled hunters dare take up the challenge: to outwit, outlast, and trap the vermin before it’s too late.\n",

        "As one of the last remaining trappers, you must be swift and strategic.", 
        "Choose the right cheese, set the perfect traps, and manage your gold wisely.",
        "Every decision counts. A single misstep could mean failure… or worse.\n",

        "With each mouse you capture, you grow stronger.",
        "Make traps, buy cheese, earn gold, and unlock powerful upgrades along the way.",
        "Your ultimate goal is to catch the Mouse King!",
        "End the madness before the land falls to ruin.\n"
    ))

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

def is_valid_name(name):
    if not is_valid_length(name):
        print("Name must be between 1 and 9 characters")
    if not is_valid_start(name):
        print("Name must start with an alphabet")
    if not is_one_word(name):
        print("Name must be at least one word")
    return is_valid_length(name) and is_valid_start(name) and is_one_word(name)

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

def show_description(message):
    description = message
    lines = description.strip().split("\n")
    for line in lines:
        print(line)
        time.sleep(2)  # Delay of 2 seconds before showing the next line

# ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# ```````````````````````````````````````` TUTORIAL `````````````````````````````````````````````````````````````````````````````

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
            if tutorial_sound == True:  # If tutorial completed
                end(True)  # Call end() with hunt_status=True              
            if tutorial_sound == False:
                break
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

def end(hunt_status: bool):
    if hunt_status:
        print("Congratulations. Ye have completed the training.\nGood luck~")

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# `````````````````````````` DIFFICULTY LEVEL SET ````````````````````````````````````````````````````````````````````

def set_difficulty():
    global difficulty, player_health, max_health
    while True:
        print()
        difficulty = input("Choose game difficulty:\n1. Noob\n2. Survivalist\n")

        if difficulty.isdigit() == True:
            difficulty = int(difficulty)
        else:
            print("Invalid option.\n")
            continue

        if difficulty < 1 or difficulty > 2:
            print("Invalid option.\n")
            continue
        else:
            if difficulty == 1:
                print("Oh my.. with such little nerve, you might not be able to come out alive from what awaits you ahead..")
                max_health = 200
                player_health = max_health
            elif difficulty == 2:
                print("Daring, are we? We all sometimes live to regret the decisions we make. Will you too..")
                max_health = 100
                player_health = max_health
            time.sleep(2)
            break

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# ```````````````````````````````` START OF STORYLINE TEXTS `````````````````````````````````````````````````````````

def storyline_introduction():
    time.sleep(4)
    print("\nStarting...\n")
    # Story introduction
    message = "\n".join((
    "\n\nYou regain consciousness.",
    "Your head feels heavy, your vision blurry. A throbbing pain lingers in your skull.",
    "Tall trees loom overhead, their twisted branches blocking out most of the daylight.",
    "The air is damp, and the scent of wet earth fills your lungs.\n",

    "Then ——— voices.",
    "Distant, but growing closer. Uneven footsteps crunch against the brittle leaves.",
    "You can’t make out the words, but something in their tone chills your bones.\n",

    "Fear grips you. Instinct kicks in.",
    "You dive into the underbrush, pressing yourself against the gnarled roots of an ancient, damp oak tree.",
    "You hold your breath.\n",

    "The voices pass. For now.",
    "You wait... a minute... then another. When you're sure they’re gone, you exhale.",
    "Something’s wrong with this place. Something bad. Something mysterious.\n",

    "And then, just within your reach, you see it—a shattered wooden crate, half-buried beneath the roots..."
    ))


    show_description(message)
    r_press = input("Press Enter to check its contents...")
    message = ""
    message = message + f"\nYOU FOUND {gold} GOLD!\n\n\n"
    message = message + f"\nA jackpot find! This will help you get started with buying accessories which you'll need for hunting!\n"
    message = message + "\nBefore you can start hunting you need a trap.\nI've heard there's an Old Carpenter who still lives in these god-foresaken lands.\nTake the wooden crate to him. I've heard the man still got plenty of tricks up his sleeve."
    message = message + "\nHe will get the job done but often for a charge. Maybe he'll feel pity for you and get started with a free trap.."
    show_description(message)
    print()
    print()
    print()

# ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# ````````````````````````````````` SHOW ALL STATS ```````````````````````````````````````````````````````````````````
# ADD MORE STATS
def showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts):
    global trap_option, doc_visit, carpenter_visit, trader_visit, cheese_dealer_visited, game_day, name
    # Total playtime
    total_time = (time.time() - start_time) / 60
    total_time = round(total_time + minutes_spent, 2)
    print("\n==============================================================\n")
    print(f"Hunter {name}, you survived {game_day} days!")
    print("\n    ---------- Game Stats ----------    ")
    print(f"Total time played: {total_time} minutes")
    print(f"\nYou visited the Cheese Dealer: {cheese_dealer_visited} times")
    print(f"You visited the Old Carpenter: {carpenter_visit} times")
    print(f"You visited the Witch Doctor: {doc_visit} times")
    print(f"You visited the Trader: {trader_visit} times\n")
    time.sleep(2)
    # Cheese bought summary
    print("\nCheese Bought:")
    for cheese_type, amount in cheese_bought.items():
        print(f"  {cheese_type}: {amount}")
    # Mice caught summary
    print("\nMice Caught:")
    for mouse_type, count in caught_mouse_dictionary.items():
        print(f"  {mouse_type}: {count}")
    # Hunt results
    time.sleep(2)
    print("\nHunt Results:")
    print(f"  Successful hunts:  {attempts['Successful hunt']}")
    print(f"  Unsuccessful hunts: {attempts['Unsuccessful hunt']}")
    # Win rate calculation
    total_hunts = attempts['Successful hunt'] + attempts['Unsuccessful hunt']
    if total_hunts > 0:
        success_rate = (attempts['Successful hunt'] / total_hunts) * 100
        print(f"  Hunt success rate: {success_rate:.2f}%")
    else:
        print("  No hunts conducted.")
    time.sleep(2)
    print("\n==============================================================\n")

# ``````````````````````````````````````````````` GAME-MENU AND PRO-TIPS `````````````````````````````````````````````````````````````````````
def get_game_menu():
    return "1. Exit Game\n2. Join the Hunt\n3. Visit Cheese Shop\n4. Select Cheese\n5. Scavenge Forest Floor\n6. Visit Trader\n7. Visit Witch Doctor\n8. Visit Old Carpenter\n9. Select Trap\n10. Check Stats\n11. Hunting Tutorial\n12. Consume Food and Potions\n"

def choose_pro_tip():
    global cheese, current_trap, trap_option, trap_cheese, box
    cheese_count = 0
    for i in range(len(cheese)):
        cheese_count += cheese[i][1]
    if trap_option[0][1] + trap_option[1][1] + trap_option[2][1] != 0:
        if current_trap == None:
            print("Pro Tip: You still have functional traps. Choose one!")                      
        else:
            print("Pro Tip: Before joining the hunt, you need a trap. Heading to the Carpenter might be a wise idea!")
    else:
        if check_box() == True:
            if cheese_count == 0:
                print("Pro Tip: Before joining the hunt, you need cheese. Heading to the Cheese Shop might be a wise idea!")
            else:
                if trap_cheese == None:
                    print("Pro Tip: Get started by placing your cheese on the trap!")
                elif has_cheese(trap_cheese, cheese) == 0:
                    print("Pro Tip: Call it a cheesy advice but you know a cheese is only good for a hunt when placed in a trap, right?")
                else:
                    print("Looking like a pro right there! Ready to hunt?")



def has_cheese(to_check, my_cheese):
    for i in range(len(my_cheese)):
        if my_cheese[i][0] == to_check.capitalize():
            if my_cheese[i][1] == 0:
                return 0
            else:
                return my_cheese[i][1]
            
# `````````````````````````````````````````` PLAYER HEALTH CHECK ````````````````````````````````````````````````````````````````````````````
def check_health():
    global player_health
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

# ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# `````````````````````````````````````````````` CHOOSING TRAP ```````````````````````````````````````````````````````````````````````
def choose_trap(trap_option, current_trap):
    has_trap = False
    for trap in trap_option:
        if trap[1] > 0:
            has_trap = True
            break
    if not has_trap:
        print("\nWARNING: You don't have any functional traps in your Storage Crate! Visit the carpenter to buy one.\n")
        time.sleep(2)
        return None
    print("\nYou currently have:")
    for trap in trap_option:
        print(f"{trap[0]}: will last {trap[1]} more hunts")
        time.sleep(2)
        print()
    while True:
        user_input = input("Select\n1. Wood-and-Spring Trap\n2. Reinforced Wood-Cage Trap\n3. Multilayer Glued-Board Trap\nEnter '0' to exit (previous trap will be deselected)\n")
        
        if user_input.isdigit():
            user_input = int(user_input)
        else:
            print("Invalid input. Enter a number!")
            continue
        if user_input == 0:
            return None  # Exit the function when 0 is entered
        if user_input < 1 or user_input > 3:
            print("Invalid input. Enter a number between 1 and 3!\n")
            continue
        if trap_option[user_input-1][1] == 0:
            print(f"You don't a functional {trap_option[user_input-1][0]} in your Storage Crate!\n")
            continue
        else:
            current_trap = trap_option[user_input-1][0]
            print(f"You have chosen {current_trap} for your next hunt!\n\n")
            time.sleep(2)
            return current_trap

        
# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#```````````````````````````````````````````` INCREASE DAY AND TIME ``````````````````````````````````````````````````````````````

def increase_time(game_time, increment):
    global game_day
    hours = int(game_time[:2])
    new_time = hours + increment
    if new_time >= 24:
        game_day += new_time // 24  # Increase the day count
        new_time = new_time % 24  # Keep time within 24-hour format    
    game_time = f"{new_time:02d} 00"  # Pad with zero if less than 10
    return game_time

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# `````````````````````````````````````````````` CARPENTER VISIT `````````````````````````````````````````````````````````````````

def visit_carpenter(menu, trap_option, wood, gold, points, carpenter_visit, cheese, current_trap, name):
    global box
    old_carpenter_shop_art()
    print()
    if carpenter_visit == 0:
        msg = "Old Carpenter:\nI thought I heard some scurrying last night. A strange chittering, like whispers in the dark.\n"
        msg = msg + "Anyways, sorry I can't let you stay here if that's what ya're here for-\n\n"
        msg = msg + "If you got some wood, I might be able to get you something to help you survive better on your own.\nMight come in handy when the Mouse King’s minions are lurking."
        show_description(msg)
        user_input = input("Press Enter to give wooden crate... ")
        print()
        msg = "A fine piece, I daresay. Withstood the forces of time but the pine wood can still be utilised. Wait here\n"
        msg = msg + "*chop* .. *grind* .. *scraping* .. *thumping* .. \n\n"
        show_description(msg)
        print(trap_art())
        print("\nYOU GOT WOOD-AND-SPRING TRAP!\n")
        msg = "I have used some scrap wood and a few bits and pieces from my other builds to make you this.\n"
        msg = msg + "Thought you might find it helpful. You are welcome, kid.\n\n"
        show_description(msg)
        print(box_art())
        print("\n\nYOU HAVE A STORAGE CRATE NOW! YOU CAN STORE YOUR ITEMS IN IT!\n")
        
        trap_option[0][1] = menu[0][3]
        carpenter_visit += 1
        wood = 0
        box["created"] = True
        box["space"] = 20 
        # add_to_box(item, type=None, quantity=1)
        add_to_box(trap_option[0][0], "trap")
        earned_points = 10
        points += earned_points
        print(f"You earned {earned_points} XP!")
        announcement()
        return (wood, gold, points, trap_option, carpenter_visit)
    else:
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
        print(f"{items_added} {item} {extra} has been added to your Storage Crate. Remaining space: {box['space']}")
    return items_added

def buy_trap(wood: int, gold: int, points: int, trap_menu: tuple, trap_option: list) -> tuple:
    global game_time
    while True:
        print("\nOld Carpenter:")
        print(f"You have {gold} gold to spend.\n")
        # print(f"FOR TESTING ========= Wood: {wood}, Gold: {gold}, Points: {points}", "Trap options:", trap_option)
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
            print("Old Carpenter: You didn't bring enough wood. Scavenge around to collect wood.\n")
            continue
        if gold < trap_menu[user_input-1][2]:
            print("Old Carpenter: You don't have enough gold, kid. Sell rare mice to the trader to earn gold.\n")
            continue
        trap_name = trap_menu[user_input-1][0]
        quantity = 1
        points += 5
        wood -= trap_menu[user_input-1][1]*quantity
        gold -= trap_menu[user_input-1][2]*quantity
        trap_option = update_trap_option(trap_option, trap_name, trap_menu)
        # add_to_box(item, type=None, quantity=1)
        add_to_box(trap_name, "trap")
        print(f"Old Carpenter: \nI can make {quantity} {trap_name} for you worries, no problem! It will last you {trap_menu[user_input-1][3]} hunts.\n")
        print(trap_art())
        print("\n\n... 4 hours later ... \n\n")
        print(f"\nYOU GOT A {trap_name.upper()}!\n")
        print("You earned 5 XP!\n")
        increase_time(game_time, 4)
        announcement()
    
def update_trap_option(trap_option, trap_name, trap_menu):
    for i in range(len(trap_option)):
        if trap_option[i][0] == trap_name:
            trap_option[i][1] += trap_option[i][3]
    return trap_option

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
        print(box["content"])
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
                print("Invalid input. Please enter a numeric value.\n")
        remove_from_box(item, quantity)
    
def remove_from_box(item, quantity=1):
    global box
    if not box["created"]:
        print("You have no Storage Crate yet!\n")
        return
    if item not in box["content"]:
        print(f"{item} is not in the storage crate.\n")
        return
    space_recovered = 5 if item == "trap" else 3 if item == "medicine" else 2 if item == "mouse" else 1
    items_removed = min(quantity, box["content"][item])
    box["content"][item] -= items_removed
    box["space"] += items_removed * space_recovered
    if box["content"][item] == 0:
        del box["content"][item]
    print(f"Removed {items_removed} {item}(s) from the crate. Remaining space: {box['space']}\n")


def search_box(obj):
    global box
    foundobj = False
    for key, val in box["content"].items():
        if obj.lower() == key.lower():
            foundobj = True
    return foundobj
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````` 
# ```````````````````````````````````````` WITCH-DOCTOR VISIT ````````````````````````````````````````````````````````````````````
def visit_witchdoctor():
    witchdoctor_chamber_art()
    print()
    global player_health, doc_visit, gold, box, points, game_time, meds_dict, max_health
    # Check if the player has visited the Witch Doctor before
    print("Witch Doctor:")
    if doc_visit == 0:
        msg = "Ah, a fresh face! First time here?\n" 
        msg += "I'm the Witch Doctor, and I can help with your health and more, if you're willing to pay the price.\n"
        msg += "Strange times we live in... ever since the Mouse King's rise, sickness spreads like a curse.\n"
        msg += "People come to me coughing, fevered ——— whispering of shadows with glowing eyes.\n\n"  
        msg += "Funny, isn't it? Everyone calls me the old hag, whispers behind my back.\n"
        msg += "Yet when the fever burns and wounds fester, suddenly they come crawling to me for aid.\n"
        msg += "Anyways, .."
    else:
        msg = "Ah, you've returned! I see you're in need of my healing expertise again."     
    show_description(msg)
    print()
    doc_visit += 1
    if player_health == max_health:
        print("\nYour health is already full. No need for healing right now.\n\n")
        if doc_visit == 1:
            print("Come back on days I'm offering discounts for better deals!")   
            time.sleep(2) 
        print("Hmph scoot away. Just don’t waste my time anymore!\n")
        return
    if player_health < 10:
        choice = input(f"Your health is critically low! Would you like to undergo an emergency operation to restore it to full health? (yes/no): ").strip().lower()
        if choice == 'yes':
            if gold >= 150:
                gold -= 150
                player_health = max_health
                print("\n... *SNIP* ... *CLINK* ... *GRIND* ...\n")
                time.sleep(4)
                print(f"\nWitch Doctor: You underwent the operation! Your health is now {player_health}.\n")
                game_time = increase_time(game_time, 8)
                return
            else:
                print("\nWitch Doctor: You need 150 gold for emergency treatment. Unfortunately you don't have enough gold for the operation!\n")
                return
        elif choice == 'no':
            print("\nWitch Doctor: Alright, be careful! Come back if you change your mind.\n")
            return
        else:
            print("\nWitch Doctor: Invalid input. Please enter 'yes' or 'no'.\n")
            return
    msg = "Here's what I got to offer you today!\n"
    msg = msg + "1. Herbal Remedy (Restores 20 health) - 40 gold"
    msg = msg + "\n2. Bloodroot Elixir (Restores 50 health) - 100 gold"
    msg = msg + "\n3. Witch’s Brew (Restores full health) - 300 gold"                             # do as show_description(msg)
    show_description(msg)
    print()
    discount_multiplier = 1
    disc_num = random.random()
    if disc_num < 0.2:
        discount_multiplier = 0.5
    elif disc_num < 0.4:
        discount_multiplier = 0.8
    if discount_multiplier != 1:
        print(f"\nIt's your luck day too! I'm clearing out my cabinet so anything you buy is {(1-discount_multiplier)*100}% off!\n")
    while True:
        choice = input("Which potion would you like to buy? Enter '1', '2', or '3'. Type 'cancel' to exit: ").strip().lower()
        if choice == 'cancel':
            print("\nWitch Doctor:")
            if doc_visit == 1:
                print("Come back on days I'm offering discounts for better deals!")   
                time.sleep(2) 
            print("Hmph scoot away. Just don’t waste my time anymore!\n")
            return
        if choice == '1':
            potion_name = "Herbal Remedy"
            potion_cost = 40
            potion_effect = "Restores 20 health"
            health_increase = 20
        elif choice == '2':
            if points < 300:
                print("Witch Doctor: Your body can't handle this dosage yet. Come back when you have more XP!\n")
                continue
            potion_name = "Bloodroot Elixir"
            potion_cost = 100
        elif choice == '3':
            if points < 500:
                print("Witch Doctor: Your body can't handle this dosage yet. Come back when you have more XP!\n")
                continue
            potion_name = "Witch’s Brew"
            potion_cost = 300
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.\n")
            continue
        if gold >= potion_cost:
            add_to_box(potion_name, "potion")
            meds_dict[potion_name] += 1
            earned_points = 3*int(choice)
            points += earned_points
            print(f"You earned {earned_points} XP!")
            announcement()
        else:
            print(f"You don't have enough gold to buy a {potion_name}.\n")

# ```````````````````````````````````````````` TRADER VISIT ````````````````````````````````````````
def visit_trader():
    global trader_visit, gold, points, box
    trader_shack_art()
    print()
    if trader_visit == 0:
        print("Trader:\n")
        msg = (
            "Never seen you around here. First time?\n"
            "No worries! If you got mice, I got 'em gold.\n"
            "But listen... there's one mouse I want more than any other. The Mouse King.\n"
            "That wretched beast took my boy.\n"
            "\nHe was just a lad, barely old enough to hold a trap. One night, he thought he could slay the King himself.\n"
            "They found his trap shattered, blood on the sidewalk, but no sign of him...\n"
            "Only those cursed claw marks leading into the dark..\n"
            "So I put a price on the Mouse King's head. Bring it to me, and not only will you be richer than any hunter here...\n" 
            "I'll see to it that you walk out of this damned place, safe and sound.\n"
        )
        msg += "\nBefore he vanished, my son left behind some notes. I keep them here, but they make little sense to me.\n"
        show_description(msg)
        r_inp = input("Press [Enter] to inspect the notes:  ")

        # Display the notes
        print("\n---------------------- Experiment 821 --------------------------")
        print("                      `````````````````                         ")
        print("To catch the Mouse King, you must use BOTH:\n")
        print("1. Swiss Cheese")
        print("2. A Multilayer Glued-Board Trap")
        print("\nConclusion: Without both, the King will never fall. Be prepared.")
        print("------------------------------------------------------------------\n")
        time.sleep(5)
        print("Anyways.. let's talk business now!")
    else:
        msg = "Welcome back to my Trading Hut! You caught that son of b- yet?"
        show_description(msg)
    if box["created"] == False:
        print("\nTrader: You don't seem to have a Storage Crate yet, huh? Swing by that mad ol' carpenter asap!\n")
        return

    while True: #==============================================================================================
        # Prepare the current list of mice in the box
        current_dict = {}
        mouse_list = ["Brown", "Field", "Grey", "White", "Tiny"]
        # Count the occurrences of each mouse type in the box content
        count = 0
        for key in box["content"].keys():
            if key in mouse_list:
                count += 1
                if key in current_dict.keys():
                    current_dict[key] += 1
                else:
                    current_dict[key] = 1
        if count == 0:
            print("\nTrader: You don't seem to have any mice in your Storage Crate!")
            print("Unfortunately I don't accept any other barter. Come back again when you catch some mice!\n")
            return 
        display_mouse_inventory(current_dict)
        # =====================================================================================================
        # Ask user for the item to remove
        item = input("Trader: Enter the name of the item you want to remove (or type 'cancel' to exit shop) ").strip()
        if item.lower() == 'cancel':
            print("Trader: Pleasure doing business with you! Remember, I'm growing impatient everyday!\n")
            return
        if item not in box["content"]:
            print("Trader: I don't see this item in your Storage Crate. Are you trying to bluff ME?\n")
            print("Note: If there is an item listed 'Wood-Cage' in your inventory which you want to remove, entering 'Wood Cage' or 'wood-cage' will not suffice!\n")
            continue
        max_quantity = current_dict[item]  # Get the available quantity of the item
        
        while True:
            quantity = input(f"\nTrader: Enter the quantity of {item} to remove (Max: {max_quantity}), or type 'cancel' to choose different mice ").strip()
            if quantity.lower() == 'cancel':
                print("Trader: Having second thoughts, are we?\n")
                break
            try:
                quantity = int(quantity)
                if quantity < 1:
                    print("Trader: Please enter a valid quantity (1 or more).\n")
                elif quantity > max_quantity:
                    print(f"Trader: You only have {max_quantity} {item}(s). Please enter a valid quantity, or type 'cancel' to exit.\n")
                else:
                    earned_gold, earned_point = loot_lut(item)  # earned points hunt ei announce kortesi
                    gold += earned_gold
                    points += earned_point
                    remove_from_box(item, quantity)

                    print(f"{quantity} {item}(s) removed successfully.\n")
                    print(f"Trader: Here you go. {earned_gold} gold!")
                    print(f"You earned {earned_point} XP!")
                    announcement()
                    break  
            except ValueError:
                print("Trader: You don't seem to understand but you gotto enter a numeric value, or type 'cancel' to exit.\n")
        
        
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

def display_mouse_inventory(current_dict):
    print("\n---------------------------------")
    print(f"Hunter {name}, you currently have:")
    for key, val in current_dict.items():
        print(f"{key}: {val}")
    print("----------------------------------\n")
    



# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# ```````````````````````````````````````````````  SCAVENGING  ```````````````````````````````````````````````````````````````````
def scavenge():
    global wood, food, game_time, points, player_health, box
    check_game_time = int(str(game_time)[:2])      
    if 5 <= check_game_time <= 23:
        risk1, risk2 = 0.05, 0.2  # Daytime risks
    else:
        risk1, risk2 = 0.1, 0.4  # Night risks
        print("ProTip: The elders say it's best to avoid wondering around once it gets too dark.")
        print("Something lurks in the shadows of these unknown realms after dark.\n")
        user_input_timewise = input("Do you want to still continue to hunt? ['yes' or 'no'] ")
        if user_input_timewise.lower() == "no":
            return False
    if box["created"] == False:
        print("You don’t have a storage crate yet! Even if you find anything, you can’t store it!")
        print("Head out to the carpenter first to get yourself one.\n\n")
        user_input = input('Do you still want to continue? ["yes" or "no"] ')
        if user_input.lower() == "no":
            return False
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
            earned_points = 2
            points += earned_points
            print(f"You earned {earned_points} XP!")
            # add_to_box(item, type=None, quantity=1)
            add_to_box("wood", "wood", random_index + 1)
            announcement()
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
            earned_points = 2 
            points += earned_points
            print(f"You earned {earned_points} XP!")
            food[food_found] += 1
            # add_to_box(item, type=None, quantity=1)
            add_to_box(food_found, "food")
            announcement()
    else:
        print("You didn’t find anything.")
        msg = "Despite your efforts, the forest floor yields nothing today."
        earned_points = 1
        points += earned_points
        print(f"You earned {earned_points} XP!")
        announcement()
    # Random chance for encountering an animal
    num1 = random.random()
    if num1 < risk1:
        animal = Animal("tiger")
    elif num1 < risk2:
        animal = Animal("wild boar")
    else:
        animal = None
    if animal:
        animal.attack()

    return True
    

# ``````````````````````````````````````````````` CHANGE CHEESE ``````````````````````````````````````````````````````````````````
def choose_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    if cheese[0][1] + cheese[1][1] + cheese[2][1] == 0:
        print("You don't have any cheese in your Storage Crate! Head out to the Cheese Dealer before his shop closes.\n")
        time.sleep(2)
        return (False, None)
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
            print("No such cheese exists!\n")
            continue
        cheese_available = False
        for i in cheese:
            if i[0] == cheese_name:
                if i[1] != 0:
                    cheese_available = True
                    break
        if cheese_available == False:
            print(f"You're out of {cheese_name} cheese!\n")
            continue
        if e_flag == True:
            print("Your {} has a one-time enchantment granting {}".format(trap, get_benefit(cheese_name)))
        #print(cheese_found, cheese_available)
        confirm = input(f"Do you want to arm your trap with {cheese_name}? ['yes'/'no']")
        confirm = confirm.lower().strip()
        if confirm == "yes":
            print(f"\n{trap} is now armed with {cheese_name}!\n")
            return (True, cheese_name)
        elif confirm == "back":
            return (False, None)
        elif confirm == "no":
            print()
            continue

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

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````` CHEESE-DEALER VISIT ````````````````````````````````````````````````````````````` 

def visit_cheese_dealer():
    global cheese_dealer_visited, game_time, gold, premium_member, cheese_bought, cheese, points, game_day
    # Check current time
    current_hour = int(game_time[:2])    
    # Check if shop is open
    if not premium_member and (current_hour < 8 or current_hour >= 18):
        print(f"\nDay: {game_day} Time: {game_time}                             HP: {player_health}\n")
        print("\nSorry, the shop is closed! Come back between 08:00 and 18:00.")        
        # Offer premium membership if they have spent over 300 gold on cheese
        total_spent = (
            cheese_bought["Cheddar"] * 10 + 
            cheese_bought["Marble"] * 50 + 
            cheese_bought["Swiss"] * 100
        )
        if total_spent > 300:
            print("Y\nou've been one of my most loyal customers!")
            buy_premium = input("Do you want to buy a Premium Membership for 100 gold? (yes/no): ").strip().lower()
            
            if buy_premium == "yes":
                if gold >= 100:
                    gold -= 100
                    premium_member = True
                    points_earned = 50
                    points += points_earned
                    print("\nCheese Dealer: You've unlocked Premium Membership!")
                    print("Your membership will be processed within the next 3 hours. You can then visit anytime!\n")
                    print(f"You earned {points_earned} XP!\n")
                    time.sleep(2)
                    announcement()
                else:
                    print("\nCheese Dealer: You don't have enough gold for Premium Membership.\n")
            else:
                print("\nCome back later when the shop is open!\n")
        return
    # Offer membership card check (optional)
    if premium_member and (current_hour < 10 or current_hour >= 16):
        show_card = input("\nCheese Dealer: Press Enter to show membership card or type 'skip' to continue: ").strip().lower()
        print("... The Cheese Dealer is inspecting your card ...'")
        time.sleep(3)
        print("Cheese Dealer: You're good to go!\n")
    print("Cheese Dealer: Welcome to The Cheese Shop!")
    cheese_shop_art()
    print()
    # First-time visit story
    if cheese_dealer_visited == 0:
        msg = (
            "You'd think my business has been booming with all the mouse madness, right?\n"
            "I wish! Ever since that cursed Mouse King showed up, mice have been raiding my stock!\n"
            "I barely have enough left to sell... and to make things worse, I had to limit my shop hours.\n"
            "\nI now only operate from 08:00 to 18:00, or I'll have no cheese left to sell!\n"
        )
        show_description(msg)       
    # Cheese purchase loop
    while True:
        cheese_shop_intro()
        user_input3 = input("Enter your choice: ")
        if user_input3.isdigit():
            user_input3 = int(user_input3)
        else:
            print("Cheese Dealer: I did not understand. Enter a numeric value!\n")
            print()
            continue
        if user_input3 < 1 or user_input3 > 3:
            print("Cheese Dealer: I did not understand. Choose a valid option.\n")
            print()
            continue
        if user_input3 == 1:
            print("Don't be stingy around here.")
            print("The more expensive cheese will help you have more successful and rewarding hunts!\n")
            time.sleep(2)

            print("Price per block:\nCheddar - 10\nMarble - 50\nSwiss - 100\n")
            time.sleep(2)

            value = buy_cheese(gold, points)
            gold -= value[0]
            cheese[0][1] += value[1][0]
            cheese[1][1] += value[1][1]
            cheese[2][1] += value[1][2]
            cheese_bought["Cheddar"] += value[1][0]
            cheese_bought["Marble"] += value[1][1]
            cheese_bought["Swiss"] += value[1][2]
            print()
        elif user_input3 == 2:
            display_inventory(wood, gold, cheese, current_trap, name)
            print()
        else:
            print("\nCheese Dealer:")
            if not premium_member and cheese_dealer_visited%5 == 0:
                msg = (
                    "\nAfter you purchase more than 300 gold worth of items from my shop, you can get a premium membership!\n"
                    "Having one will mean you can visit my shop whenever you want!\n"
                    "I know, I know... Capitalism sucks, huh? Not as much as your mo— ahem, never mind.\n"
                )
                show_description(msg)
            print("Goodbye, then..")
            time.sleep(1)
            break
    cheese_dealer_visited += 1  # Track visits

def cheese_shop_intro():
    print("Cheese Dealer: How can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop")

def buy_cheese(gold_in_hand: int, points: int) -> tuple:
    global box
    spent = 0
    cheddar = 0
    marble = 0
    swiss = 0
    while True:
        print(f"\nYou have {gold_in_hand} gold to spend.")
        user_input = input("Cheese Dealer:\nEnter 'back' when you're done shopping. To buy, state [cheese-name cheese-quantity] (eg. cheddar 2): ")
        if len(user_input) == 0:
            print("Cheese Dealer: I don't seem to understand what you want..\n")
            continue
        #returning to main menu
        if user_input.lower() == "back":
            return (spent, (cheddar, marble, swiss))
        user_input = user_input.split()
        cheese_type = user_input[0].lower()
        #checking is cheese name is valid
        if cheese_type not in ["cheddar", "marble", "swiss"]:
            print(f"Cheese Dealer: I don't sell any {cheese_type}!\n")
            continue
        else:
            if points < 100:
                if cheese_type != "cheddar":
                    print(f"Cheese Dealer: You do not have enough XP to unlock this item yet. Choose another cheese.\n")
                    continue
            elif points < 300:
                if cheese_type == "swiss":
                    print(f"Cheese Dealer: You do not have enough XP to unlock this item yet. Choose another cheese.\n")
                    continue
        #checking if quantity is missing
        if len(user_input) == 1:
            print("Cheese Dealer: If you don't tell me what quantity of cheese you want how can I sell?\n")
            continue
        else:
            quantity = user_input[1]
        #checking if quantity enteres is not a number
        if quantity.isnumeric() == False:
            print("Cheese Dealer: Do you need me to teach you how numbers work..?\n")
            continue
        else:
            cheese_purchased = int(quantity)
        #checking if quantity entered is non-positive
        if cheese_purchased <= 0:
            print("Cheese Dealer: You need.. a negative amount of cheese, huh?\n")
            continue
        cheese_type = cheese_type.capitalize()
        #cheese-wise base price setting
        if cheese_type == "Cheddar":
            unit_price = 10
        elif cheese_type == "Marble":
            unit_price = 50
        else:
            unit_price = 100
        # ekhane check kore add to box korbo
        added_quantity = add_to_box(cheese_type, "food", cheese_purchased)
        if added_quantity != 0:
            gold_needed = added_quantity * unit_price
            #successful buy or sell
            if gold_needed <= gold_in_hand:
                print(f"Cheese Dealer: Pleasure doing business with you! You have successfully purchased {cheese_type}.")
                cheese_art()
                if cheese_type == "Cheddar":
                    cheddar += cheese_purchased
                elif cheese_type == "Marble":
                    marble += cheese_purchased
                else:
                    swiss += cheese_purchased
                gold_in_hand -= gold_needed
                spent += gold_needed
                points += added_quantity
                print(f"You earned {added_quantity} XP!\n")
                announcement()
            else:
                print("Cheese Dealer: You don't have enough gold.\n")
                continue

#`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# ````````````````````````````````````````````  HUNT  ````````````````````````````````````````````````````````````````````````````

def hunt(gold, cheese, trap_cheese, enchant, points, attempts, caught_mouse_dictionary, game_over_status):
    global game_time, player_health, box, trap_option, current_trap, king_mouse_caught
    hunt = 0
    if current_trap == None:
        print("How did you forget to bring a trap with you?? smh..\n")
    if box["created"] == False:
        print("You don’t have a Storage Crate yet! Even if you catch anything, you can’t store it!")
        print("Head out to the carpenter first to get yourself one.\n\n")
        user_input = input('Do you still want to continue? ["yes" or "no"] ')
        if user_input.lower() == "no":
            return (gold, points, cheese, attempts, caught_mouse_dictionary, game_over_status)
    while True:
        trap_remain = 0
        for i in trap_option:
            if i[0] == current_trap:
                trap_remain = i[1]
        if trap_remain == 0:
            print("Your trap has broken..")
            break
        
        if box["space"] < 2:
            print("\nWARNING! You don't seem to have enough space in your Storage Crate.\nWithout sufficient space you will be forced to let go of any mouse you catch!\n")
        game_over_status = check_game_over()
        if game_over_status == True:
            break
        print("Day:", game_day, "Time", game_time, "                                      Gold:", str(gold), "XP:", points, "HP:", player_health, "\n")
        check_game_time = int(str(game_time)[:2])                
        if 5 <= check_game_time <= 23:
            risk1, risk2 = 0.1, 0.2  # Daytime risks
        else:
            print("ProTip: The elders say it's best to avoid wondering around once it gets too dark.")
            print("Something lurks in the shadows of these unknown realms after dark.\n")
            user_input_timewise = input("Do you want to still continue to hunt? ['yes' or 'no'] ")
            if user_input_timewise.lower() == "no":
                break
            risk1, risk2 = 0.05, 0.4  # Night risks                                                                                                                       
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
            animal.attack()
            continue    
        if sound_input == '' or sound_input != "yes":
            print("You did not properly sound the horn. Hunt wasted.")
            hunt += 1
            for i in trap_option:
                if i[0] == current_trap:
                    i[1] -= 1
            game_time = increase_time(game_time, 3)
        else:
            print("\n~~ ~ ~~~~ ~~~ ~~ ~~ ~ ~~~~\n")
            if trap_cheese == None:
                hunt += 1
                for i in trap_option:
                    if i[0] == current_trap:
                        i[1] -= 1
                game_time = increase_time(game_time, 1)
                print("Nothing caught. You are out of cheese!")
            else:
                cheese, status = consume_cheese(trap_cheese, cheese)
                if status == False:
                    hunt += 1
                    for i in trap_option:
                        if i[0] == current_trap:
                            i[1] -= 1
                    game_time = increase_time(game_time, 1)
                    print("Nothing happens. You are out of cheese!")
                else:                   
                    mouse = Mouse(trap_cheese, enchant, points)
                    # print("CURRENTLY Cheese list is:", cheese)

                    if mouse.name != None:
                        hunt = 0
                        game_time = increase_time(game_time, 3)
                        if mouse.name == "MouseKing":
                            print(f"The scratch marks are unmistakeable!")
                            # trap limitation
                            if current_trap != "Multilayer Glued-Board Trap":
                                print(f"Drat! Your trap wasn't strong enough to catch the Mouse King! Golden opportunity missed..")
                                time.sleep(3)
                                attempts["Unsuccessful hunt"] += 1
                                continue
                            fight_back = random.random()
                            print(f"The scratch marks are unmistakeable!")
                            time.sleep(2)
                            if fight_back > 0.5:
                                print("Unlucky! You caught the Mouse King but it fought it's way free!")
                                time.sleep(2)
                                print("He can't get away every time. Keep trying!")
                                attempts["Unsuccessful hunt"] += 1
                                continue
                            else:
                                describe = king_mouse_description()
                                show_description(describe)
                                king_mouse_caught = True
                                time.sleep(3)
                                attempts["Successful hunt"] += 1
                                game_over_status = True
                                return (gold, points, cheese, attempts, caught_mouse_dictionary, game_over_status)
                                
                        points += mouse.get_points()
                        # gold += mouse.get_gold()
                        print("``````````````````````````````````````````")
                        print("You caught a {} mouse!".format(mouse.name))
                        print(mouse.get_coat())
                        print("``````````````````````````````````````````")
                        caught_mouse_dictionary[mouse.name] += 1
                        attempts["Successful hunt"] += 1
                        print(f"You earned {mouse.get_points()} XP!")
                        # add_to_box(item, type=None, quantity=1)
                        add_to_box(mouse.name, "mouse")
                    else:
                        #print("H1:", hunt)
                        hunt += 1
                        points += mouse.get_points()
                        print(f"You earned {mouse.get_points()} XP!")
                        attempts["Unsuccessful hunt"] += 1
                        #print("H2:", hunt)
                        print("The wilderness can sometimes be cruel. Hunt unsuccessful.")
                        game_time = increase_time(game_time, 3)
                    
                    for i in trap_option:
                        if i[0] == current_trap:
                            i[1] -= 1

        # print("Gold:", str(gold) + ", Points:", points)
        print()

        announcement()

        if hunt%5 == 0 and hunt != 0:
            print("Looks like you're not having a great hunting session today.")
            user_input4 = input("Do you want to still continue to hunt? ['yes' or 'no'] ")
            if user_input4.lower() == "no":
                break
    return (gold, points, cheese, attempts, caught_mouse_dictionary, game_over_status)


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
    print("=========================================================")
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
    print("=========================================================")

def level_check_2():
    print("=========================================================")
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
    print("=========================================================")

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

# ```````````````````````````````````````` MOUSE FUNCTIONS ```````````````````````````````````````````````````````````````````````

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

def king_mouse_description():
    return """
    The air grows thick with an eerie stillness, as if the very world holds its breath.  
    From the shadows, a slow, rhythmic thudding shakes the ground beneath you.  

    And then—he emerges.  

    A towering figure, cloaked in a tattered regal robe, his fur matted with the remnants of a thousand battles.  
    His eyes, like burning embers, lock onto yours with a gaze that feels ancient, knowing.  

    The **Mouse King** has arrived.  

    He does not scurry like the others—he **marches**, each step a declaration of his dominion. The lesser mice scatter, vanishing into the night, leaving you alone in his presence.  

    A challenge unspoken. A duel inevitable.  

    You steel yourself, gripping the baited trap, your heartbeat deafening in your ears.  

    Then—**SNAP!**  

    Silence.  

    The great Mouse King stands frozen. A moment that stretches into eternity.  

    And then, with a final, defiant glare… he falls.  

    The realm of mice has lost its ruler. But you?  

    You have become **a legend**.
    """

def town_rejoices():
    return """
    The news spreads like wildfire. The **Mouse King is no more.**  

    The Trader is the first to find you, their usual wary expression replaced with a triumphant grin.  
    Trader: 
    "You did it! That menace won’t be ruining trade routes anymore. As promised, I'll get to making arrangements to get you out of here."
    "But just so you know.. "
    He leans in, lowering his voice.  
    "There's someone else who may need your help. I’ll get the details to you soon."
    
    "Meanwhile… enjoy the celebrations."

    ---

    In the marketplace, the Old Carpenter watches you with quiet admiration. They nod approvingly.  
    Old Carpenter: "A strong heart, steady hands.. you remind me of myself, once. I knew you wouldn’t fail."  

    ---

    Near the apothecary, the Witch Doctor stands under the moonlight, eyes closed, a faint smile on their lips.  
    Witch Doctor: "The spirits whisper no more… their restless cries have been silenced. At last, I can rest knowing the darkness is lifting."*  

    ---

    And at the Cheese Shop.. pure chaos. The Cheese Dealer is standing on a crate, waving his arms wildly at an eager crowd.  
    Cheese Dealer: 
    "It was MY CHEESE that led to victory!"
    "You hear that?! No cheap cheese, no victory! I should raise the prices!" 

    Laughter, music, and cheers fill the town.  

    Tonight, you are a HERO. But something deep inside tells you, this is just the beginning.
    """

def decrease_health_while_travel():
    global player_health
    # 50% chance that health won't be decreased
    no_decrease_chance = 0.5
    if random.random() < no_decrease_chance:
        # print("No health decrease during this travel.")
        return  # No health decrease
    # Probabilities for 1 to 5 health decrease (total sum = 1)
    decrease_probabilities = [0.4, 0.3, 0.15, 0.1, 0.05]  # Probabilities for health decrease amounts
    # Randomly choose an index based on the probabilities
    decrease_index = random.choices(range(5), decrease_probabilities)[0]
    # Calculate damage taken (index + 1)
    damage_taken = decrease_index + 1
    player_health -= damage_taken
    # Ensure health doesn't go below 0
    if player_health < 0:
        player_health = 0
    # 5 possible events causing health decrease
    travel_event_messages = [
        "You trip over a sharp rock and scrape your leg, causing you to lose some health!",
        "A sudden drizzle hits, and you're drenched and cold, your health takes a hit.",
        "You stumble into a thorn bush, getting scratched up and hurting your health!",
        "A wild animal scares you, and you fall, bruising yourself badly. Ouch! Health drops.",
        "You accidentally hit a low branch. Your health decreases."
    ]
    # Print the event message that corresponds to the health decrease
    print(travel_event_messages[decrease_index])
    time.sleep(2)
    # print(f"Health decreased by {damage_taken}!")
    # time.sleep(2)

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def consume_item():
    global food, meds_dict, player_health, max_health
    count1 = 0
    str1 = "\nFood options:\n"
    for key, val in food.items():
        str1 = str1 + f"{key}: {val} left\n"
        count1 += val
    str1.strip()
    count2 = 0
    str2 = "\nPotion options\n:"
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
            food_options = ["apple", "banana", "berries", "mushrooms", "frog"]
            if  food[item] > 0:
                food[item] -= 1
                print(f"\nYou consumed {item}. {food[item]} left.\n")
                inc = food_options.index(item)+1
                player_health += inc
                if player_health > max_health:
                    player_health = max_health
                time.sleep(5)
                print(f"You got much needed rest.. {inc} HP restored!\n")
                remove_from_box(item)
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
                remove_from_box(item)
                break
            else:
                print(f"\n{item} is out of stock\n")
        else:
            print(f"\nYou dont have {item} in your Storage Crate\n")

def check_box():
    global box
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
   
# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````



# stats e show days survived
# add achievements
# decrease to 2 difficulty system
# add mood of witch doc for hard mode
# decrease cheese shop timing for hard mode + higher price for premium
# trader give out fake gold in hard mode



# display inventory te item NOT found barbar


def main():
    global trap_option, cheese, trap_cheese, current_trap, food, wood, gold, points, carpenter_visit, game_over, game_time, player_health, max_health
    global box, trader_visit, name, difficulty, king_mouse_caught, doc_visit, game_day, meds_dict, cheese_bought
    global cheese_dealer_visited, called_functions, premium_member, TYPE_OF_MOUSE
    TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")
    CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
    TRAP = (("Wood-and-Spring Trap", 10, 5, 10), ("Reinforced Wood-Cage Trap", 30, 15, 20), ("Multilayer Glued-Board Trap", 50, 50, 15))
    # format: name - wood - gold - lasting duration(turns/hunts)

    start_gold = (200, 150, 125)
    game_over = False
    doc_visit = 0
    trader_visit = 0
    carpenter_visit = 0 
    cheese_dealer_visited = 0                                                                             
    points = 0
    gold = 0
    wood = 0
    player_health = 100
    max_health = 100
    game_time = "09 00"
    game_day = 1
    meds_dict = {"Herbal Remedy": 0, "Bloodroot Elixir": 0, "Witch’s Brew": 0}
    box = {"created": False, "space": 0, "content":{}}
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap_option = [["Wood-and-Spring Trap", 0], ["Reinforced Wood-Cage Trap", 0], ["Multilayer Glued-Board Trap", 0]]
    food = {"apple": 0, "banana": 0, "berries": 0, "mushrooms": 0, "frog": 0}
    caught_mouse_dictionary = {}
    for i in TYPE_OF_MOUSE:
        caught_mouse_dictionary[i] = 0

    minutes_spent = 0
    attempts = {"Successful hunt": 0, "Unsuccessful hunt": 0}
    cheese_bought = {"Cheddar": 0, "Marble": 0, "Swiss": 0}
    start_time = time.time()

    trap_cheese = None
    current_trap = None
    enchant = False
    king_mouse_caught = False
    premium_member = False                                                  # GENJAM

    called_functions = {
        "level_check_1": False,
        "level_check_2": False
    }

    set_name()

    print("Welcome to the Kingdom, Hunter", name+"!")
    print("\nBefore we begin, let's train you up!")
    user_input1 = input('Press "Enter" to start training or "skip" to Start Game: ')

    if user_input1 != 'skip':
        tutorial()

    set_difficulty()

    gold += start_gold[difficulty-1]

    storyline_introduction()

    while True:

        if king_mouse_caught == True:
            game_over = True
            town_rejoices()

        if trap_cheese == None:
            enchant = False
        elif trap_cheese.lower() == "swiss":
            enchant = True
        else:
            enchant = False

        health_status = check_health()
        if health_status == False:
            game_over = True

        if game_over == True:
            if king_mouse_caught == False:
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

        print(f"\nDay: {game_day} Time: {game_time}                             HP: {player_health}\n")
        print("What do ye want to do now, Hunter",name+'?')
        print(get_game_menu())

        while True:
            choose_pro_tip()

            user_input2 = (input("Enter a number between 1 and 12: "))
            if user_input2.isdigit() == True:
                user_input2 = int(user_input2)
            else:
                print("Invalid input.\n\n")
                continue
            if user_input2 < 1 or user_input2 > 12:
                print("Must be between 1 and 12.\n\n")
            else:
                break
        





        if user_input2 == 12:
            exist = check_box()
            if exist:
                print("Taking items out of Storage Crate..\n")
                time.sleep(3)

                status = consume_item()

                print("Putting things back inside Storage Crate..\n\n\n")
                time.sleep(3)
                if status != False:
                    game_time = increase_time(game_time, 1)



        elif user_input2 == 11:
            tutorial()



        elif user_input2 == 10:
            showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts)



        elif user_input2 == 9:
            current_trap = choose_trap(trap_option, current_trap)
            if current_trap != None:
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
            decrease_health_while_travel() 
            game_time = increase_time(game_time, 2)



        elif user_input2 == 7:
            print("Travelling to Witch Doctor...\n\n")
            game_time = increase_time(game_time, 2)
            time.sleep(3)

            visit_witchdoctor()

            print("Returning..\n\n")
            time.sleep(3)  
            decrease_health_while_travel()
            game_time = increase_time(game_time, 2)
            


        elif user_input2 == 6:
            print("Travelling to Trader...\n\n")
            game_time = increase_time(game_time, 2)
            time.sleep(3)

            visit_trader()

            print("Returning..\n\n")
            time.sleep(3)  
            decrease_health_while_travel()
            game_time = increase_time(game_time, 2)
           


        elif user_input2 == 5:
            print("Searching around...\n\n")
            time.sleep(3)

            scavenge_status = scavenge()
            
            if scavenge_status: 
                if check_health():
                    print("Returning..\n\n")
                    time.sleep(3)   
                decrease_health_while_travel()
                game_time = increase_time(game_time, 1)                     



        elif user_input2 == 4:
            print("Looking at cheese in Storage Crate..\n\n")
            time.sleep(3)

            if enchant == True:
                cheese_val = choose_cheese(name, current_trap, cheese, True)
            else:
                cheese_val = choose_cheese(name, current_trap, cheese)
            trap_cheese = cheese_val[1]

            print("Putting things back inside Storage Crate..\n\n")
            if cheese_val[0]:
                game_time = increase_time(game_time, 1)



        elif user_input2 == 3: 
            print("Travelling to Cheese Shop... \n\n")
            time.sleep(3)
            game_time = increase_time(game_time, 2)

            visit_cheese_dealer()
            
            print("Returning..\n\n")
            time.sleep(2)
            decrease_health_while_travel()
            game_time = increase_time(game_time, 2)



        elif user_input2 == 1:
            # show final stats
            print(f"Thanks for joining our adventure, Hunter {name}!")
            time.sleep(3)
            print("\nDon't forget to check out your achievements:\n\n")
            showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts)
            key = input("Enter any key to exit... ")
            break



        else: #user_input = 2
            print("Travelling to Meadow... \n\n")
            time.sleep(3)
            game_time = increase_time(game_time, 2)

            results = hunt(gold, cheese, trap_cheese, enchant, points, attempts, caught_mouse_dictionary, game_over)
            gold = results[0]
            points = results[1]
            cheese = results[2]
            attempts = results[3]
            caught_mouse_dictionary = results[4]
            game_over = results[5]

            if not game_over:
                print("Returning..\n\n")
                time.sleep(2)
                decrease_health_while_travel()
                game_time = increase_time(game_time, 2)
            else:
                continue

if __name__ == '__main__':
    main()
                                                                                                                                     