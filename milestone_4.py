#imports pre-defined variables and functions, and random module by extension
import milestone_3 as m3 


#defining the Hangman class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = m3.word_list               # word_list- pre-programmed options for what the word could be
        self.num_lives = num_lives                  # number of lives the player has at the start of the game
        self.word = m3.word                         # word to be guessed, randomly selected from word_list
        self.word_guessed = ["_"]*len(m3.word)      # should keep track and display user's guesses so far, e.g. if the user guessed "l" and the word is "apple", display: ['_','_','_', 'l','_']
        self.num_letters = len(set(word))           # should display the number of unique letters in the word not yet guessed (i.e. should decrease with each successful guess)
        self.list_of_guesses = [None]               # a list of the guesses that have already been tried

                                                        