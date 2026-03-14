import time
from ascii_art import trader_shack_art
from helper import show_description, announcement, remove_from_box
from mouse_functions import loot_lut, check_mouse_present
from globals import *

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

    trader_visit += 1
    if not box["created"]:
        print("\nTrader: You don't seem to have a Storage Crate yet, huh? Swing by that mad ol' carpenter asap!\n")
        return

    while True:
        # Show menu options
        print("\n1. Return to town")
        print("2. Trade mice")
        
        choice = input("\nWhat would you like to do? (Enter 1 or 2)  ").strip()
        
        if choice == "1":
            print("Trader: Come back when you've got more mice to trade!\n")
            return
            
        elif choice == "2":
            current_dict = check_mouse_present()
            if current_dict == None:
                print("Trader: You don't have any mice to trade! Come back after a few more successful hunts.\n")
                return
            
            # Display current inventory
            print("\n----- Your Current Mice -----")
            for mouse, quantity in current_dict.items():
                print(f"{mouse}: {quantity}")
            print("----------------------------")


            # Get mouse selection
            item = input("\nWhich mouse would you like to trade? (or 'back' to menu): ").strip()
            
            if item.lower() == "back":
                continue
                
            if item not in box["content"]:
                print("Trader: I don't see that type of mouse in your crate.\n")
                continue
            
            # Get quantity
            max_quantity = current_dict.get(item, 0)
            quantity = input(f"How many {item} mice? (max {max_quantity}): ").strip()
            
            try:
                quantity = int(quantity)
                if quantity < 1:
                    print("Trader: Please enter a valid quantity.\n")
                    continue
                if quantity > max_quantity:
                    print(f"Trader: You only have {max_quantity} of those!\n")
                    continue
                
                # Process the trade
                earned_gold, earned_points = loot_lut(item)
                gold += earned_gold * quantity
                points += earned_points * quantity
                remove_from_box(item, quantity)
                
                print(f"\nTraded {quantity} {item} mice for {earned_gold * quantity} gold!")
                print(f"You earned {earned_points * quantity} XP!")
                announcement()
                
            except ValueError:
                print("Trader: That's not a valid number!\n")
                continue
        
        else:
            print("Invalid choice. Please enter 1 or 2.\n") 