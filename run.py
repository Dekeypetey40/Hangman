# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import statements
import random
from art import *
from simple_term_menu import TerminalMenu


#Art for hangman game taken from Crishorton https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========
7 GUESSES LEFT''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
6 GUESSES LEFT''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
5 GUESSES LEFT''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
4 GUESSES LEFT''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
3 GUESSES LEFT''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
2 GUESSES LEFT''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
1 GUESSES LEFT''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
YOU LOST!''']
def hangman_art(lives):
  return (HANGMANPICS[-lives-1])

#return hangman_lives[-lives-1]






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
        options = ["Easy: 7 guesses", "Medium: 6 guesses", "Hard: 5 guesses"]
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
    guessed_letters = []
    guessed_words = []
    hidden_word = []
    game_over = False
    
      
    for letter in word:     
        hidden_word.append("_")
    while not game_over and lives > 0:
        print(hangman_art(lives))
        print (*hidden_word)
        print(word)
        print(f"\n\nThe word has {len(word)} letters.")
        print("Letters guessed: " + ', '.join(guessed_letters))
        guess = input("Guess a letter or word:\n").lower()
        #code if user guesses a single letter
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"You have already guessed {guess}, try again!")
            elif guess not in word:
                print(f"{guess} is not in the word")
                lives -=1
                guessed_letters.append(guess)
            else:
                #Replacing underscores with correct letters inspired by https://www.youtube.com/watch?v=DLurhc1i5_4&ab_channel=MikhaHarly
                print(f"""{guess} is in the word! Good Job!""")
                guessed_letters.append(guess)
                for position in range (len(word)):
                    letter = word[position]
                    if letter == guess:
                        hidden_word[position] = letter
                    if "_" not in hidden_word:
                        print("YOU WIN!")
                        game_over = True
        elif guess.isalpha() and len(guess) == len(word):
            if guess in guessed_words:
                print(f"You have already guessed {guess}, try again!")
            elif guess != word:
                print(f"{guess} is not the word!")
                lives -=1
                guessed_words.append(guess)
            else:
                print("YOU WIN!")
                game_over = True
                
                
                # print("You have guessed correctly!")
                # guessed_letters.append(guess)
                # hidden_list = list(hidden_word)
                # letter_check = [i for i, letter in enumerate(word)
                #            if letter != "_" and guess == letter]
                # for check in letter_check:
                #     hidden_list = [check] = guess
                # hidden_word = "".join(hidden_list)
                if "_" not in hidden_word:
                    game_over = True
            
    #     guess = input(f"Guess a letter \n")
    #     #code partially taken from stack overflow to replace _ with correct letter
    #     print(hangman_art(lives))
    #     for i, letter in enumerate(word):
    #         if letter != "_" and guess == letter:
    #             print("You have guessed correctly!")
    #             hidden_word[i] = letter
    #             guessed_letters.append(guess)
    #             print("".join(hidden_word))
    #     if guess in guessed_letters:
    #         print(f"You have already guessed {guess}, try again!")
    #     elif guess not in word:
    #         lives -=1
            

    
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








