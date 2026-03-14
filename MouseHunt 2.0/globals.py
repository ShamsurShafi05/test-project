"""Global variables used across the game"""

# Game Constants
TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")
CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
TRAP = (("Wood-and-Spring Trap", 3, 5, 10), ("Reinforced Wood-Cage Trap", 5, 15, 20), ("Multilayer Glued-Board Trap", 8, 50, 15))

# Game State
name = ""
difficulty = None
player_health = 100
max_health = 100
game_time = "09 00"
game_day = 1
game_over = False
king_mouse_caught = False

# Player Resources
gold = 0
wood = 0
points = 0

# Inventory
box = {"created": False, "space": 0, "content": {}}
food = {"Apple": 0, "Banana": 0, "Berry": 0, "Mushroom": 0, "Frog": 0}
meds_dict = {"Herbal Remedy": 0, "Bloodroot Elixir": 0, "Witch's Brew": 0}

# Equipment
trap_option = [["Wood-and-Spring Trap", 0], ["Reinforced Wood-Cage Trap", 0], ["Multilayer Glued-Board Trap", 0]]
cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
trap_cheese = None
current_trap = None
enchant = False

# Visit Counters
doc_visit = 0
trader_visit = 0
carpenter_visit = 0
cheese_dealer_visited = 0

# Statistics
caught_mouse_dictionary = {mouse_type: 0 for mouse_type in TYPE_OF_MOUSE}
attempts = {"Successful hunt": 0, "Unsuccessful hunt": 0}
cheese_bought = {"Cheddar": 0, "Marble": 0, "Swiss": 0}
minutes_spent = 0

# Feature Flags
premium_member = False
called_functions = {
    "level_check_1": False,
    "level_check_2": False
}