import random
import time
from ascii_art import witchdoctor_chamber_art
from helper import show_description, increase_time, add_to_box, announcement
from globals import *

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