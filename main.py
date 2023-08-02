"""--------------------------------------------------------------------------
This is a simple program to model the classic rock-paper-scissor  game.
Input: 0 - for rock
       1 - for paper
       2 - for scissor
Output: You win - if the player win
        You lose - if the player lose
        It's a Draw - if it's a draw
--------------------------------------------------------------------------"""

import random
from symbols import *

options = [rock, paper, scissors]
human = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n > ")
game_on = True

try:
    human = int(human)
except ValueError:
    game_on = False

if game_on and (human == 0 or human == 1 or human == 2):
    comp = random.randint(0, 2)

    print("You chose:" + options[human])
    print("Computer chose:" + options[comp])

    result = ""

    if comp == human:
        result = "draw"
    elif human == 0 and comp == 1:
        result = "lose"
    elif human == 1 and comp == 2:
        result = "lose"
    elif human == 2 and comp == 0:
        result = "lose"
    else:
        result = "win"

    if result == "draw":
        print("It's a draw")
    else:
        print(f"You {result}")
else:
    # for integers except 0,1 and 2
    # for non-int characters
    print("Sorry! Not a valid input.")
