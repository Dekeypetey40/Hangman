# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import statements
import random
from art import *




#Constants
welcome=text2art("Welcome\n To\n Hangman",font='doom',chr_ignore=True)
print(welcome)
def game_rules():
    """
    Show the user the game rules, which explain how to play.
    """
    #clear_screen()
    print(
        f"""
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    The objective is to save the man being hung by guessing the word.
    You may either guess a letter or a full word.
    Guess incorrectly and add a mistake.
    Mistakes lead the man closer to death.
    Guess the word correctly without making too many mistakes
    and the you will save the man!


    Will you be able to save the day?
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        """
    )
    input("Press enter to return to main menu\n")
art_1=art("coffee")
print(art_1)