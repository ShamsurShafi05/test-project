import random
import time
from ascii_art import *
from creatures import *
from beginning import *
from training import *
from globals import *           # be careful
from menu import *
from helper import *
from mouse_functions import *
from scavenging import *
from carpenter import *
from cheese_dealer import *
from trader import *
from witch import *
from hunting import *
from ending import *


def main():
    global trap_option, cheese, trap_cheese, current_trap, wood, gold, points, carpenter_visit, game_over, game_time, player_health, max_health
    global box, trader_visit, name, difficulty, king_mouse_caught, doc_visit, game_day, meds_dict, cheese_bought
    global cheese_dealer_visited, called_functions, premium_member, TYPE_OF_MOUSE, TRAP, CHEESE_MENU, meds_dict, food
    
    
    # Initialize starting values that need to be reset each game
    start_gold = (200, 150, 125)
    start_time = time.time()
    
    # Set initial game state
    game_over = False
    points = 0
    game_time = "09 00"
    game_day = 1
    player_health = max_health

    name = set_name(name)

    print("Welcome to the Kingdom, Hunter", name+"!")
    print("\nBefore we begin, let's train you up!")
    user_input1 = input('Press "Enter" to start training or "skip" to Start Game: ')

    if user_input1 != 'skip':
        tutorial()

    difficulty, player_health, max_health = set_difficulty(difficulty, player_health, max_health)


    gold += start_gold[difficulty-1]
    wood += 3 

    storyline_introduction(gold)

    while True:


        if king_mouse_caught == True:
            game_over = True
            descr = town_rejoices()
            show_description(descr)

        if trap_cheese == None:
            enchant = False
        elif trap_cheese.lower() == "swiss":
            enchant = True
        else:
            enchant = False

        health_status = check_health(player_health)
        if health_status == False:
            game_over = True

        if game_over == True:
            if king_mouse_caught == False:
                print(f"Thanks for joining our adventure, Hunter {name}! Better luck next time.")
                time.sleep(3)
                print("\nDon't forget to check out your achievements:\n\n")
                showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts, trap_option, doc_visit, carpenter_visit, trader_visit, cheese_dealer_visited, game_day, name)
                # progress
                print("\nStay tuned for upcoming versions~")
                key = input("Enter any key to exit... ")
                break
            else:
                print(f"Congrats on surviving this adventure, Hunter {name}!")
                print("There are moments I doubted you but you surely knew your way in the face of crisis!")
                time.sleep(3)
                print("\nDon't forget to check out your achievements:\n\n")
                showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts, trap_option, doc_visit, carpenter_visit, trader_visit, cheese_dealer_visited, game_day, name)
                print("\nStay tuned for upcoming versions~")
                key = input("Enter any key to exit... ")
                break

        print("\n\nDay:", game_day, "Time", game_time, "                                      Gold:", str(gold), "XP:", points, "HP:", player_health, "\n")
        print("What do ye want to do now, Hunter",name+'?')
        print(get_game_menu())

        while True:
            choose_pro_tip(cheese, current_trap, trap_option, trap_cheese, box, wood)

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
            exist = check_box(box)
            if exist == True or exist == None:
                print("Taking items out of Storage Crate..\n")
                time.sleep(3)

                status = consume_item(food, meds_dict, player_health, max_health)

                print("Putting things back inside Storage Crate..\n\n\n")
                time.sleep(3)
                if status != False:
                    game_time = increase_time(game_time, 1)



        elif user_input2 == 11:
            tutorial()



        elif user_input2 == 10:
            showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts, trap_option, doc_visit, carpenter_visit, trader_visit, cheese_dealer_visited, game_day, name)



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
                if check_health(player_health):
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
            showStats(start_time, minutes_spent, cheese_bought, caught_mouse_dictionary, attempts, trap_option, doc_visit, carpenter_visit, trader_visit, cheese_dealer_visited, game_day, name)
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
                                                                                                                                     