import time
from globals import *
from mouse_functions import check_mouse_present
from helper import check_box, has_cheese

# ````````````````````````````````` SHOW ALL STATS ```````````````````````````````````````````````````````````````````
# ADD MORE STATS
def showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts, trap_option, doc_visit, carpenter_visit, trader_visit, cheese_dealer_visited, game_day, name):
    # global trap_option, doc_visit, carpenter_visit, trader_visit, cheese_dealer_visited, game_day, name
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


# trap na thakle age check enuf wood ase ki na naile tell to scavenge
def choose_pro_tip(cheese, current_trap, trap_option, trap_cheese, box, wood):
    # global cheese, current_trap, trap_option, trap_cheese, box, wood
    cheese_count = 0
    for i in range(len(cheese)):
        cheese_count += cheese[i][1]
    
    # mouse thakle need to say go to trader first
    flag = check_mouse_present()
    if flag != None:
        print("Pro Tip: You have a mouse in your Storage Crate. Visit the Trader to sell it for gold!")
    else:
        if trap_option[0][1] + trap_option[1][1] + trap_option[2][1] == 0:
            if wood < 3:
                print("Pro Tip: You don't have enough wood to make a trap. Scavenge the forest floor for wood!")
            else:
                print("Pro Tip: Before joining the hunt, you need a trap. Heading to the Carpenter might be a wise idea!")
        else:
            if current_trap == None:
                print("Pro Tip: You still have functional traps. Choose one!")                      
            else:
                if check_box(box) == True:
                    if cheese_count == 0:
                        print("Pro Tip: Before joining the hunt, you need cheese. Heading to the Cheese Shop might be a wise idea!")
                    else:
                        if trap_cheese == None:
                            print("Pro Tip: Select a cheese to place on your trap!")
                        elif has_cheese(trap_cheese, cheese) == 0:
                            print("Pro Tip: Call it a cheesy advice but you know a cheese is only good for a hunt when placed in a trap, right?")
                        else:
                            print("Looking like a pro right there! Ready to hunt?")
