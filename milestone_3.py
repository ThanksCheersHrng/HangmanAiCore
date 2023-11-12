
import random as rn 
word_list = ["blueberry","strawberry","raspberry","peach","tomato"] 
word = rn.choice(word_list)

while True: 
    #Input guess for a letter 
    guess = input("Enter a single letter: ")
    #Check guess is a single letter. 
    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print("Good guess! {guess} is in the word.")
else:
    print("Sorry, {guess} is not in the word. Try again.")