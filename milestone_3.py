
import random as rn 
word_list = ["blueberry","strawberry","raspberry","peach","tomato"] 
word = rn.choice(word_list)

print(len(word), len(set(word)))

'''
#checking if guess in word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again. ")

#asking for input and checking validity:
def ask_for_input(): 
    while True: 
        #Input guess for a letter 
        guess = input("Enter a single letter: ")
        #Check guess is a single letter. 
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

#call to check game play
ask_for_input()
'''