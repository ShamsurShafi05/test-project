import time
from globals import name, difficulty, player_health, max_health, gold
from helper import show_description

def set_name(name):
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
    return name

def game_intro(message):
    # title = "Mousehunt"
    logo = r"""
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


# `````````````````````````` DIFFICULTY LEVEL SET ````````````````````````````````````````````````````````````````````

def set_difficulty(difficulty, player_health, max_health):
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
            return difficulty, player_health, max_health
            break

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

# ```````````````````````````````` START OF STORYLINE TEXTS `````````````````````````````````````````````````````````

def storyline_introduction():
    global gold

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
