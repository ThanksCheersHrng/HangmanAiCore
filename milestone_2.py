import random as rn 

word_list = ["blueberry","strawberry","raspberry","peach","tomato"] 
#print(word_list)
#print(type(word_list))

word = rn.choice(word_list)
#print(word)

guess = input("Enter a single letter: ")


if len(guess) == 1 and guess.lower() in "abcdefghijklmnopqrstuvwxyz":
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
