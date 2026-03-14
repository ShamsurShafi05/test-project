import time
from ascii_art import old_carpenter_shop_art, box_art, trap_art
from helper import show_description, announcement, add_to_box, display_inventory, increase_time
from globals import box, game_time


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
        box["space"] = 25         # Assuming the crate has 25 space with 5 space for the trap
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
                print("Old Carpenter: I did not understand. Enter a number!")
                print()
                continue
            if user_input < 1 or user_input > 3:
                print("Old Carpenter: I did not understand. Enter a number between 1 and 3!")
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
        time.sleep(4)
        print(f"\nYOU GOT A {trap_name.upper()}!\n")
        print("You earned 5 XP!\n")
        increase_time(game_time, 4)
        announcement()


def update_trap_option(trap_option, trap_name, trap_menu):
    for i in range(len(trap_option)):
        if trap_option[i][0] == trap_name:
            trap_option[i][1] += trap_menu[i][3]
    return trap_option


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
        if trap[1] > 0:
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
