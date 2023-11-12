#imports
import random as rn 

#defining the Hangman class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #initialised attributes 
        self.word_list = word_list               # word_list- pre-programmed options for what the word could be
        self.num_lives = num_lives                  # number of lives the player has at the start of the game
        
        #attributes defined using other attributes
        self.word = rn.choice(word_list)                       # word to be guessed, randomly selected from word_list
        self.word_guessed = ["_"]*len(self.word)      # should keep track and display user's guesses so far, e.g. if the user guessed "l" and the word is "apple", display: ['_','_','_', 'l','_']
        self.num_letters = len(set(self.word))           # should display the number of unique letters in the word not yet guessed (i.e. should decrease with each successful guess)
        
        #initial attribute without parameter 
        self.list_of_guesses = []               # a list of the guesses that have already been tried
   
    def check_guess(guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
    def ask_for_input():
        while True: 
            #Input guess for a letter 
            guess = input("Enter a single letter: ")
            #Check guess is a single letter. 
            if (guess.isalpha() and len(guess) == 1) is False:
                print("Invalid letter. Please, enter a single alphabetical character. ")
            #check guess hasn't been guessed before.
            elif guess in list_of_guesses:
                print("You already tried that letter! ")
            else: #if the guess is new and appropriate 
                list_of_guesses.append(guess)
                check_guess(guess)
                

word_list1 = ["blueberry","strawberry","raspberry","peach","tomato"] 
game1 = Hangman(word_list1)


#Hangman.ask_for_input()
ask_for_input() #still says this function not defined (outside of class?)
game1.ask_for_input() #still says takes 0 pos arg but 1 given

                                                        