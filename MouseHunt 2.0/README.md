# MouseHunt 2.0

A text-based hunting game where players catch mice using different traps and cheese.

## Project Structure

```
MouseHunt 2.0/
├── MAIN.py                 # Main game loop and initialization
├── ascii_art.py            # ASCII art functions for visual elements
├── beginning.py            # Game start functions
├── carpenter.py            # Carpenter NPC interaction
├── cheese_dealer.py        # Cheese shop functions
├── creatures.py            # Animal and Mouse classes
├── ending.py               # End game scenarios
├── globals.py              # Global variables and constants
├── helper.py               # Utility functions
├── hunting.py              # Hunting mechanic functions
├── menu.py                 # Menu display functions
├── mouse_functions.py      # Mouse-related functions
├── scavenging.py           # Resource gathering functions
├── trader.py               # Trader NPC interaction
├── training.py             # Tutorial functions
└── witch.py                # Witch doctor NPC interaction

```

## Function Directory

### ascii_art.py
- character_art()
- tiger_art()
- wild_boar_art()
- mouse_art variants

### beginning.py
- set_name()
- set_difficulty()
- game_intro()
- is_valid_name()
- is_valid_length()
- is_valid_start()
- is_one_word()
- storyline_introduction()

### helper.py
- show_description()
- check_health()
- increase_time()
- add_to_box()
- remove_from_box()
- get_item_type()
- search_box()
- display_inventory()
- check_game_over()
- consume_cheese()
- level_check_1()
- level_check_2()
- announcement()
- consume_item()
- check_box()
- has_cheese()
- get_benefit()

### mouse_functions.py
- generate_mouse()
- generate_coat()
- loot_lut()

### hunting.p
- hunt()
- choose_cheese()
- choose_trap()

### menu.py
- get_game_menu()
- choose_pro_tip()

[Additional functions and modules to be documented...]
```

````python
# filepath: c:\Users\This PC\Desktop\Thesis\MouseHunt 2.0\.gitignore
# Python
__pycache__/
*.py[cod]
*$py.class

# Distribution/packaging
dist/
build/
*.egg-info/

# Virtual environments
venv/
env/
ENV/

# IDEs and editors
.vscode/
.idea/
*.swp
*.swo

# OS generated files
.DS_Store
Thumbs.db