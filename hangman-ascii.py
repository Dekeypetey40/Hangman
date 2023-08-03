

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