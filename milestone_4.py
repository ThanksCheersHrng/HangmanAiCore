#imports pre-defined variables and functions, and random module by extension
import milestone_3 as m3 

import random as rn 
word_list = ["blueberry","strawberry","raspberry","peach","tomato"] 
word = rn.choice(word_list)




#defining the Hangman class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #initialised attributes 
        self.word_list = m3.word_list               # word_list- pre-programmed options for what the word could be
        self.num_lives = num_lives                  # number of lives the player has at the start of the game
        
        #attributes defined using other attributes
        self.word = m3.word                         # word to be guessed, randomly selected from word_list
        self.word_guessed = ["_"]*len(m3.word)      # should keep track and display user's guesses so far, e.g. if the user guessed "l" and the word is "apple", display: ['_','_','_', 'l','_']
        self.num_letters = len(set(m3.word))           # should display the number of unique letters in the word not yet guessed (i.e. should decrease with each successful guess)
        
        #initial attribute without parameter 
        self.list_of_guesses = []               # a list of the guesses that have already been tried
   
    def check_guess(guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
    def ask_for_input():
        while True: 
            #Input guess for a letter 
            guess = input("Enter a single letter: ")
            #Check guess is a single letter. 
            if (guess.isalpha() and len(guess) == 1) is False:
                print("Invalid letter. Please, enter a single alphabetical character. ")
            #check guess hasn't been guessed before.
            elif guess in self.list_of_guesses:
                print("You already tried that letter! ")
            else: #if the guess is new and appropriate 
                self.list_of_guesses.append(guess)
                check_guess(guess)
                
## Hangman.ask_for_input() 
#NameError: 'self' not defined for self.list_of_guesses (in function) 
#need to call the word_list from m3 as a Hangman class object. 
#So I tried that and it didn't work, either:
## game1 = Hangman(m3.word_list)
## game1.ask_for_input()
#This time the error was "Hangman.ask_for_input() takes 0 positional arguments but 1 was given" 

Hangman.ask_for_input()



                                                        