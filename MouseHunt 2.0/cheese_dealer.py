import time
from globals import cheese_dealer_visited, game_time, gold, premium_member, cheese_bought, cheese, points, game_day, wood, current_trap, player_health
from helper import announcement, show_description, display_inventory, add_to_box, display_cheese_inventory, get_benefit
from ascii_art import cheese_shop_art, cheese_art


def visit_cheese_dealer():
    global cheese_dealer_visited, game_time, gold, premium_member, cheese_bought, cheese, points, game_day
    # Check current time
    current_hour = int(game_time[:2])    
    # Check if shop is open
    if not premium_member and (current_hour < 8 or current_hour >= 18):
        print("\n\nDay:", game_day, "Time", game_time, "                                      Gold:", str(gold), "XP:", points, "HP:", player_health, "\n")
        print("\nSorry, the shop is closed! Come back between 08:00 and 18:00.") 
        print("Pro Tip: You should engage in other activities to get through the night.\n")       
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

            print("Price per block:\nCheddar - 10 gold\nMarble - 50 gold\nSwiss - 100 gold\n")
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
            display_inventory(wood, gold, cheese, current_trap)
            print()
        else:
            print("\nCheese Dealer:")
            if not premium_member and cheese_dealer_visited%5 == 0:
                msg = (
                    "\nAfter you purchase more than 300 gold worth of items from my shop, you can get a premium membership!\n"
                    "Having one will mean you can visit my shop whenever you want!\n"
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
