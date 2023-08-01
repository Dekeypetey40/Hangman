# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import statements
import random
from art import *
from simple_term_menu import TerminalMenu

def main():
    options = ["entry 1", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()


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
