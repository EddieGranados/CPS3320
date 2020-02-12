# Hangman game!

# Assume the answer is "hangman"
A = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
L = ['_', '_', '_', '_', '_', '_', '_']

play = True
chances = 0
x=0

while play == True:
    i = 0

    # Ask the user to guess a letter
    letter = str(input("Guess a letter: "))

    # Check to see if that letter is in the Answer
    if (letter not in A[:]):
        print("BAD GUESS!")
        chances = chances + 1
        print("YOU HAVE %d CHANCES LEFT!" % (6-chances))
    # elif (letter in A[:]):
    #     continue

    for currentletter in A[:]:
        # If the letter the user guessed is found in the answer,
        # set the underscore in the user's answer to that letter
        if (letter in currentletter):
            L[i] = letter

        i = i + 1

    # Display what the player has thus far (L) with a space
    # separating each letter
    print(' '.join(str(n) for n in L))

    # Test to see if the word has been successfully completed,
    # and if so, end the loop
    if (A == L):
        play = False
        print("GREAT JOB!")

    if (chances == 6):
        print("BETTER LUCK NEXT TIME!")
        play = False

