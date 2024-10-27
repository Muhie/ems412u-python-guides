# Muhie Al Haimus
# 7/08/2024
""" Expaination of the program: 
Write a program that generates a random number between 1 and 100 and
then asks the user to guess it. Allow them 5 guesses before the game is “lost”.
Help them by displaying whether the guess is too high or too low after each
attempt. Make sure that if they guess correctly that they WIN! Hint: use the
library random to generate random numbers! """

# import the random library
import random

# generate a random number between 1 and 100

random_number = random.randint(1, 100)

num_guesses = 0
correct = False # this is a boolean variable or a 'flag' for the while loop to exit when the correct guess is made rather than using break.

while num_guesses < 5 and correct != True:   
    guess = int(input("Guess the number between 1 and 100! ")) 
    if guess > random_number and guess < 101: # check if the guess is too high and is between 1 and 100
        print("Your guess is too high!")
        num_guesses = num_guesses + 1
    if guess < random_number and guess > 0: # check if the guess is too low and is between 1 and 100
        print("Your guess is too low!")
        num_guesses = num_guesses + 1
    elif guess < 0: # check if the guess is negative
        print("Invalid guess")
    elif guess > 100: # check if the guess is greater than 100
        print("Invalid guess")
    elif guess == random_number:
        print("You guessed correctly!") 
        correct = True

if correct == False:
    print("You loose haha")


              

