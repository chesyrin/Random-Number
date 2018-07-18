# Project #2: Guess the Number
# Randomly generate a number and tell user to guess

import random

print ("Welcome to the Random Number Generator!")
number = random.randint (1,100)
guessed=False

print (number)

while guessed==False:
    # Take the user's input
    answer = input("Please guess the number: ")
    if (answer.isdigit()):
        if ((int)(answer)==number):
            guessed=True
        elif ((int)(answer)<number):
            print ("Too low!")
        else:
            print ("Too high!")
    else:
        print ("Not a number!")
print ("You guessed it!")
