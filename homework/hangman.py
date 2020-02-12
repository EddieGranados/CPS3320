# Hangman game!

import random

play = True
chances = 0

A = [] #Answer List
L = [] #Input List
#list of words to choose from
word_list = ['hangman', 'anthropology', 'nose', 'gaurd', 'mother', 'awesome', 'north']

#randomly assign a word to A, and make the word a list
A = list(random.choice(word_list))

#for 0 to the length of A, at index x, add an underscore to L
for x in range(0,len(A)):
    L.insert(x,'_')

while play == True:
    # Ask the user to guess a letter
    letter = str(input("Guess a letter: "))

    #if the input that is entered is nothing, make it an underscore
    if (letter == ''):
        letter = '_'

    # Check to see if that letter is in the Answer
    if (letter not in A[:] or letter == ''):
        print("BAD GUESS!")
        chances = chances + 1
        print("YOU HAVE %d CHANCES LEFT!" % (6-chances))

    for currentletter in A[:]:
        # If the letter the user guessed is found in the answer,
        # set the underscore in the user's answer to that letter
        if (letter in currentletter):
            L[currentletter.index()] = letter

    # Display what the player has thus far (L) with a space
    # separating each letter
    print(' '.join(str(n) for n in L))

    # Test to see if the word has been successfully completed,
    # and if so, end the loop
    if (chances == 6):
        play = False
        print("BETTER LUCK NEXT TIME!")

    if (L == A):
        play = False
        print("GREAT JOB!")
print(len(A))
