import random
from globals import *
from helper import announcement, increase_time, add_to_box, show_description
from creatures import Animal



def scavenge():
    global wood, food, game_time, points, player_health, box
    check_game_time = int(str(game_time)[:2])      
    if 5 <= check_game_time <= 23:
        risk1 = 0.1  # Daytime risks
    else:
        risk1 = 0.2  # Night risks
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
    food_options = ["Apple", "Banana", "Berry", "Mushroom", "Frog"]  # Replaced fish with frog
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
            add_to_box("Wood", "Wood", random_index + 1)
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
        animal = Animal("wild boar")
    else:
        animal = None
    if animal:
        animal.attack()

    return True