import time
import random
from globals import player_health

def king_mouse_description():
    return """
    The air grows thick with an eerie stillness, as if the very world holds its breath.  
    From the shadows, a slow, rhythmic thudding shakes the ground beneath you.  

    And then— it emerges.  

    A towering figure, cloaked in a tattered regal robe, its fur matted with the remnants of a thousand battles.  
    Its eyes, like burning embers, lock onto yours with a gaze that feels ancient, knowing.  

    The **Mouse King** has arrived.  

    It does not scurry like the others— it **marches**, each step a declaration of its dominion. The lesser mice scatter, vanishing into the night, leaving you alone in its presence.  

    A challenge unspoken. A duel inevitable.  

    You steel yourself, gripping the baited trap, your heartbeat deafening in your ears.  

    Then— **SNAP!**  

    Silence.  

    The great Mouse King stands frozen. A moment that stretches into eternity.  

    And then, with a final, defiant glare… it falls.  

    The realm of mice has lost its ruler. But you?  

    You have become a LEGEND..
    """


def town_rejoices():
    return """
    The news spreads like wildfire. The **Mouse King is no more.**  

    The Trader is the first to find you, their usual wary expression replaced with a triumphant grin.  
    Trader: 
    "You did it! That menace won’t be ruining trade routes anymore. As promised, I'll get to making arrangements to get you out of here."
    "But just so you know.. "
    He leans in, lowering his voice.  
    "There's someone else who may need your help. I’ll get the details to you soon."
    
    "Meanwhile… enjoy the celebrations."

    ---

    In the marketplace, the Old Carpenter watches you with quiet admiration. They nod approvingly.  
    Old Carpenter: "A strong heart, steady hands.. you remind me of myself, once. I knew you wouldn’t fail."  

    ---

    Near the apothecary, the Witch Doctor stands under the moonlight, eyes closed, a faint smile on their lips.  
    Witch Doctor: "The spirits whisper no more… their restless cries have been silenced. At last, I can rest knowing the darkness is lifting."*  

    ---

    And at the Cheese Shop.. pure chaos. The Cheese Dealer is standing on a crate, waving his arms wildly at an eager crowd.  
    Cheese Dealer: 
    "It was MY CHEESE that led to victory!"
    "You hear that?! No cheap cheese, no victory! I should raise the prices!" 

    Laughter, music, and cheers fill the town.  

    Tonight, you are a HERO. But something deep inside tells you, this is just the beginning.
    """

def decrease_health_while_travel():
    global player_health
    # 50% chance that health won't be decreased
    no_decrease_chance = 0.5
    if random.random() < no_decrease_chance:
        # print("No health decrease during this travel.")
        return  # No health decrease
    # Probabilities for 1 to 5 health decrease (total sum = 1)
    decrease_probabilities = [0.4, 0.3, 0.15, 0.1, 0.05]  # Probabilities for health decrease amounts
    # Randomly choose an index based on the probabilities
    decrease_index = random.choices(range(5), decrease_probabilities)[0]
    # Calculate damage taken (index + 1)
    damage_taken = decrease_index + 1
    player_health -= damage_taken
    # Ensure health doesn't go below 0
    if player_health < 0:
        player_health = 0
    # 5 possible events causing health decrease
    travel_event_messages = [
        "You trip over a sharp rock and scrape your leg, causing you to lose some health!",
        "A sudden drizzle hits, and you're drenched and cold, your health takes a hit.",
        "You stumble into a thorn bush, getting scratched up and hurting your health!",
        "An owl scares you, and you fall, bruising yourself badly. Ouch! Health drops.",
        "You accidentally hit a low branch. Your health decreases."
    ]
    # Print the event message that corresponds to the health decrease
    print(travel_event_messages[decrease_index])
    time.sleep(2)
    # print(f"Health decreased by {damage_taken}!")
    # time.sleep(2)