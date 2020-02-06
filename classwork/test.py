# print("Hello Universe!")
# print("Hola!")

# user = input("What is your name? ")

# print("Hello there ",user, "!")

#------------------------------x------------------------------

# dollorAmount = float(input("How much dollards do you have: "))

# euro = dollorAmount * 0.91

# print("That is", '{0:.2f}'.format(euro, "dollars."))

#------------------------------x------------------------------

# bitCoin = float(input("How many BitCOins do you have: "))

# dollar = bitCoin * 9335.19

# print("That is", '{0:.2f}'.format(dollar, "dollars."))

# dollar = dollar * (.125)

# print("An eigth is", '{0:.2f}'.format(dollar, "dollars."))

#------------------------------x------------------------------
#turle is a drawing canvas
#libraries and package are interchangable
#most popular libraries NLTK, Beautiful Soup, Pandas, Tweepy, PyGame, Micecraft

from turtle import *


# begin_fill()
# color('Blue')
# left(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# end_fill()
# penup()
# right(90)
# forward(100)
# pendown()
# begin_fill()
# color('Red')
# right(45)
# forward(70)
# right(90)
# forward(75)
# end_fill()
# penup()
# color('Brown')
# goto(0,0)
# left(45)
# forward(50)
# pendown()
# begin_fill()
# forward(20)
# left(90)
# forward(20)
# left(90)
# forward(10)
# left(90)
# forward(20)
# end_fill()

# goto(0, 0)
# goto(0, 100)
# goto(100, 100)
# goto(100, 0)
# goto(0, 0)
# penup()
# goto(0, 100)
# pendown()
# color("red")
# begin_fill()

# done()

#------------------------------x------------------------------

# myAge = int(input("How old are you? "))
# crushAge = int(input("How old is your crush? "))

# limit = ((myAge) / 2) + 7

# if (crushAge < limit):
#     print("Creepy")
# else:
#     print("Ok")
#------------------------------x------------------------------

import random
# countH = 0
# countT = 0

# for i in range(99999):
#     coin = random.choice(['heads', 'tails'])
#    # print(coin)
#     if coin == "tails":
#         countH = countH + 1
#     elif coin == "heads":
#         countT = countT + 1   

# print(countH)
# print(countT)

#------------------------------x------------------------------

firstBet = input("What is your first choice...\n ")
secondBet = input("What is your second choice...\n ")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

if die1 == firstBet and die2 == secondBet:
    print("Correct")
else:
    print("Better luck next time!")

print("What was thrown:", die1, die2)
