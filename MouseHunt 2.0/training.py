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