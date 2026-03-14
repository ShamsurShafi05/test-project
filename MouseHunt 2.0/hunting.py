from globals import *
from helper import announcement, increase_time, check_game_over, remove_from_box, add_to_box, has_cheese, consume_cheese, show_description
import random
import time
from creatures import Animal, Mouse
from ending import king_mouse_description

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
        announcement()
        trap_remain = 0
        for i in trap_option:
            if i[0] == current_trap:
                trap_remain = i[1]
        if trap_remain == 0:
            print("Your trap has broken..")
            box = remove_from_box(current_trap, 1)  # Remove broken trap from crate
            current_trap = None  # Reset current_trap to None 
            return box
            break
        
        if box["space"] < 2:
            print("\nWARNING! You don't seem to have enough space in your Storage Crate.\nWithout sufficient space you will be forced to let go of any mouse you catch!\n")
        game_over_status = check_game_over()
        if game_over_status == True:
            break
        print("\n\nDay:", game_day, "Time", game_time, "                                      Gold:", str(gold), "XP:", points, "HP:", player_health, "\n")
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
            if trap_cheese is None or has_cheese(trap_cheese, cheese) == 0:
                hunt += 1
                for i in trap_option:
                    if i[0] == current_trap:
                        i[1] -= 1
                game_time = increase_time(game_time, 1)
                print("Nothing caught. You are out of cheese!")
                continue
            else:
                box = remove_from_box(trap_cheese, 1)
                # need to return

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

        if hunt%5 == 0 and hunt != 0:
            print("Looks like you're not having a great hunting session today.")
            user_input4 = input("Do you want to still continue to hunt? ['yes' or 'no'] ")
            if user_input4.lower() == "no":
                break
    return (gold, points, cheese, attempts, caught_mouse_dictionary, game_over_status)
