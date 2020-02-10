
#scarrble letter dictionary
scrabble_tiles = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,
                  'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

def letterScore(n):  # create a function that takes a single letter
    global letter 
    
    letter = str(n.upper()) #create letter variable
    if(letter.capitalize() in scrabble_tiles):  # check if input is a valid input
        print("\nScrabble Tile: %s\nTile Value: %d\n" %(letter, scrabble_tiles[letter]))  # then print equivalent value
    else:
        print("\nScrabble Tile: %s\nTile Value: %s\n" % (letter, "0"))

def wordScore(n):  # create a function that inputs a single word/string
    word = str(n.upper()) #set up word
    score = 0

    for i in range(0,len(word)): #search through range of the length of the word
        if (word[i] != ' '):
            letterScore(word[i])
            score = score + scrabble_tiles[letter]
    print("Word: %s\nScore: %d" % (word, score))
    
wordScore("heLLo")
#wordScore("  -!@#   word  fwdjfhs")
