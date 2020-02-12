# Hangman game!
from  turtle import *
import random

#turtle screen set up
window = Screen()
window.setup(200, 300, 200, 200)

#creating the hanging mans structure
def head():
    goto(0, 0)
    circle(25)

def body():
    right(90)
    forward(75)

def rightArm():
    goto(0, 0)
    forward(15)
    right(45)
    forward(35)

def leftArm():
    penup()
    goto(0, 0)
    left(45)
    pendown()
    forward(15)
    left(45)
    forward(35)

def rightLeg():
    penup()
    goto(0,0)
    pendown()
    right(45)
    forward(75)
    right(45)
    forward(35)


def leftLeg():
    penup()
    goto(0, 0)
    pendown()
    left(45)
    forward(75)
    left(45)
    forward(35)


play = True
attmepts = 0

A = []  # Answer List
L = []  # Input List

#list of words to choose from
word_list = ['hangman', 'anthropology', 'nose',
             'gaurd', 'mother', 'awesome', 'north']

#randomly assign a word to A, and make the word a list
A = list(random.choice(word_list))

#loop through 0 to length of A,
#at index x, add an underscore to that index point of L 
for x in range(0, len(A)):
    L.insert(x, '_')

#run game as along as play is true
while play == True:
    i = 0
    # Ask the user to guess a letter
    letter = str(input("Guess a letter: "))

    #if the input that is entered is nothing,
    #make it an underscore
    if (letter == ''):
        letter = '_'

    # Check to see if that letter is in the Answer
    if (letter not in A[:] or letter == ''):
        print("BAD GUESS!")
        attmepts = attmepts + 1
        print("YOU HAVE %d CHANCES LEFT!" % (6-attmepts))

    for currentletter in A[:]:
        # If the letter the user guessed is found in the answer,
        # set the underscore in the user's answer to that letter
        if (letter in currentletter):
            L[i] = letter
        
        i = i + 1

    # Display what the player has thus far (L) with a space
    # separating each letter
    print(' '.join(str(n) for n in L))

    #Check to see if attempts is equal to 6 incorrect attempts ,
    #if amount of incorrect attempts is 6, then end the game 

    if (attmepts == 1):
        head()
    elif (attmepts == 2):
        body()
    elif (attmepts == 3):
        rightArm()
    elif (attmepts == 4):
        leftArm()
    elif (attmepts == 5):
        rightLeg()
    elif (attmepts == 6):
        leftLeg()

    if (attmepts == 6):
        play = False
        print("BETTER LUCK NEXT TIME!")

    # Test to see if the word has been successfully completed,
    # and if so, end the loop
    if (L == A):
        play = False
        print("GREAT JOB!")
