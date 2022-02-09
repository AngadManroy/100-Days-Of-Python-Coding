from dis import dis
from os import system
import random as r
def print_hangman():
    print('''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"           ''')    

if __name__=="__main__":
    print_hangman()
    lis_hangman = ['''+---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    word,display = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split(),[]
    chosen_word = r.choice(word)
    for i in chosen_word:
        display.append('_')
    print(display)
    iscomplete = False #while loop exit condition
    lives = -7 #keeping track of player's lives

    while not iscomplete:
        if lives == -1:
            print("You Lose!")
            system.exit(0)

        guess = input("Guess a letter").lower()
        iscorrect=False
        for i in range(len(chosen_word)):
            if guess==chosen_word[i]:
                iscorrect=True
                display[i] = chosen_word[i]

        if iscorrect == False:
            print("Oops! You guessed a wring letter!")
            lives+=1
        else:
            print("Yay! You guessed the right letter!")
        print(lis_hangman[lives])
        print(display)
        if '_' not in display:
            iscomplete=True
            print("You Win!")
