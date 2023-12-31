# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import statements
import random
from art import *
from simple_term_menu import TerminalMenu
import os
from hangman_ascii import hangman_art


# code taken from
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear():
    """
    This clears the terminal to prevent clutter on it.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    This handles the welcome menu and calls the functions
    to play the game and look at the rules
    """
    clear()
    welcome = text2art("Welcome To\n Hangman", font='doom', chr_ignore=True)
    print(welcome)
    options = ["Play Game", "Rules", "Quit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        main()
    if options[menu_entry_index] == "Play Game":
        word = choose_word()
        lives = choose_difficulty()
        play_game(word, lives)

    elif options[menu_entry_index] == "Rules":
        game_rules()
    elif options[menu_entry_index] == "Quit":
        print("Goodbye!")
        exit()  # using python's built in exit() function to quit the program


def choose_difficulty():
    """
    Gives the user a menu to select the difficulty level.
    Depending on the level selected the user is assigned
    a certain amount of lives
    """
    while True:
        clear()
        print("Select difficulty level")
        options = ["Easy: 7 guesses", "Medium: 6 guesses", "Hard: 5 guesses"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index is None:
            choose_difficulty()
        if options[menu_entry_index] == "Easy: 7 guesses":
            lives = 7
            return lives
        elif options[menu_entry_index] == "Medium: 6 guesses":
            lives = 6
            return lives
        elif options[menu_entry_index] == "Hard: 5 guesses":
            lives = 5
            return lives
        else:
            print("Unknown error occured, please try again")


def choose_word():
    """
    Reads the words.txt file and randomly selects a word from the list
    and returns it for the play_game function to use.
    """
    word = (random.choice(open("words.txt", "r").read().split()))
    return word


def play_game(word, lives):
    """
    Main function to play the hangman game.
    Tells the user how many letters are in the randomly
    chosen word and prompts them to guess.
    If the user inputs a letter already guessed, they
    are prompted to choose a different letter. If the user
    is correct, it replaces underscore(s) with the letter.
    If they are incorrect, the player loses a guess and the hangman
    picture is updated. Waits for player to win or lose to ask
    the player if they want to play again.
    """
    guessed_letters = []
    guessed_words = []
    hidden_word = []
    game_over = False
    message = ""

    for letter in word:
        hidden_word.append("_")
    while not game_over and lives >= 0:
        if lives == 0:
            clear()
            print(hangman_art(lives))
            print(f"\nThe word was {word}\n")
            restart_game()
            break
        elif hidden_word == word or "_" not in hidden_word:
            clear()
            print(hangman_art(lives))
            print(f"\nYOU WIN!\n")
            print(f"The word was {word}\n")
            restart_game()
            break
        else:
            print("An unexpected error occured, please try again")
        clear()
        print(message)
        print(hangman_art(lives))
        print(*hidden_word)
        print(f"\n\nThe word has {len(word)} letters.\n")
        print("Letters guessed: " + ', '.join(guessed_letters) + f"\n")
        print("Words guessed: " + ', '.join(guessed_words) + f"\n")
        guess = input("Guess a letter or word:\n").lower()
# code if user guesses a single letter
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                message = f"You have already guessed {guess}, try again!"
            elif guess not in word:
                message = f"{guess} is not in the word"
                lives -= 1
                guessed_letters.append(guess)
            else:
                # Replacing underscores with correct letters inspired by
                # https://www.youtube.com/watch?v=DLurhc1i5_4&ab_channel=MikhaHarly
                message = f"""{guess} is in the word! Good Job!"""
                guessed_letters.append(guess)
                for position in range(len(word)):
                    letter = word[position]
                    if letter == guess:
                        hidden_word[position] = letter
        # Code if user guesses a word
        elif guess.isalpha() and len(guess) == len(word):
            if guess in guessed_words:
                message = f"You have already guessed {guess}, try again!"
            elif guess != word:
                print(f"{guess} is not the word!")
                lives -= 1
                guessed_words.append(guess)
            else:
                hidden_word = guess
        # Code to catch invalid input
        elif guess.isalpha() and (len(guess) != 1 and len(guess) != len(word)):
            message = (f'Either guess 1 letter or a '
                       f'word with {len(word)} characters')
        else:
            message = "Invalid input, try again!"


def restart_game():
    """
    Asks the player if they want to play again or quit.
    If they want to play again they are taken back to the
    welcome menu. If they choose to quit, the program ends.
    """
    print("Would you like to play again or turn off the game?\n")
    options = ["Play again", "Quit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        restart_game()
    if options[menu_entry_index] == "Play again":
        main()
    elif options[menu_entry_index] == "Quit":
        print("Goodbye!")
    else:
        print("An error occured, please try again.")


def game_rules():
    """
    Show the user the game rules, which explain how to play.
    Include a menu to return to the welcome screen or quit.
    """
    clear()
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
    if menu_entry_index is None:
        game_rules()
    if options[menu_entry_index] == "Quit":
        print("Goodbye!")
    elif options[menu_entry_index] == "Return to Main Menu":
        main()
    else:
        print("An unexpected error occured, please try again.")


main()
