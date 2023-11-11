#Hangman 

import random as rn 

#Select a random target word 
word_list = ["blueberry","strawberry","raspberry","peach","tomato"] 
#print(word_list)
#print(type(word_list))
word = rn.choice(word_list)
#print(word)

#Input guess for a letter 
guess = input("Enter a single letter: ")

#Check guess is a single letter. 
if len(guess) == 1 and guess.lower() in "abcdefghijklmnopqrstuvwxyz":
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
