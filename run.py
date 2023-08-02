# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import statements
import random
from art import *
from simple_term_menu import TerminalMenu
from getkey import getkey, keys






def main():
    welcome=text2art("Welcome\n To\n Hangman",font='doom',chr_ignore=True)
    print(welcome)
    options = ["Play Game", "Rules", "Quit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    if options[menu_entry_index] == "Play Game":
        word = choose_word()
        difficulty = choose_difficulty()
        #play_game(word, difficulty)
        play_game(word)
        
    elif options[menu_entry_index] == "Rules":
        game_rules()
        
def choose_difficulty():
    while True:
        print("Select difficulty level")
        options = ["Easy: 9 guesses", "Medium: 7 guesses", "Hard: 5 guesses"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Easy: 9 guesses":
            difficulty = "easy"
            return difficulty
        elif options[menu_entry_index] == "Medium: 7 guesses":
            difficulty = "medium"
            return difficulty
        elif options[menu_entry_index] == "Hard: 5 guesses":
            difficulty = "hard"
            return difficulty
        

def choose_word():
    word = (random.choice(open("words.txt","r").read().split()))
    return word


def play_game(word):
    for letter in word:          
        print('_ ', end=' ')
    print(f"\n\nThe word has {len(word)} letters.")

def game_rules():
    """
    Show the user the game rules, which explain how to play.
    Include a menu to return to the welcome screen or quit.
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
    options = ["Return to Main Menu", "Quit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "Return to Main Menu":
        main()
    #elif options[menu_entry_index] == "Quit":
        #game_rules()
main()







