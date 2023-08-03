# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import statements
import random
from art import *
from simple_term_menu import TerminalMenu






def main():
    welcome=text2art("Welcome\n To\n Hangman",font='doom',chr_ignore=True)
    print(welcome)
    options = ["Play Game", "Rules", "Quit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    if options[menu_entry_index] == "Play Game":
        word = choose_word()
        lives = choose_difficulty()
        play_game(word, lives)
        
    elif options[menu_entry_index] == "Rules":
        game_rules()
        
def choose_difficulty():
    while True:
        print("Select difficulty level")
        options = ["Easy: 9 guesses", "Medium: 7 guesses", "Hard: 5 guesses"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Easy: 7 guesses":
            lives = 7
            return lives
        elif options[menu_entry_index] == "Medium: 6 guesses":
            lives = 6
            return lives
        elif options[menu_entry_index] == "Hard: 5 guesses":
            lives = 5
            return lives
        

def choose_word():
    word = (random.choice(open("words.txt","r").read().split()))
    return word


def play_game(word, lives):
    guesses = []
    hidden_word = [" _ "] * len(word)
    game_over = False
    print(f"\n\nThe word has {len(word)} letters.")  
    
    for letter in word:     
        print('_ ', end=' ')
            
    while not game_over and lives > 0:
        
        print(word)
        guess = input(f"Guess a letter \n")
        #code partially taken from stack overflow to replace _ with correct letter
        
        for i, letter in enumerate(word):
            if letter != "_" and guess == letter:
                print("You have guessed correctly!")
                hidden_word[i] = letter
                guesses.append(guess)
                print(guesses)
                print("".join(hidden_word))
        if guess in guesses:
            print(f"You have already guessed {guess}, try again!")
        elif guess not in word:
            lives -=1
            print(f"{guess} is not in the word!\nYou have {lives} lives remaining.")

    

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
#main()
word = choose_word()
lives = 7
play_game(word, lives)







