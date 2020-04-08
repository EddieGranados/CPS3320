import turtle
import random



# window setup
def createWindow():
    turtle.hideturtle()
    window = turtle.Screen()
    window.title("Turtle Race")
    turtle.bgcolor("light blue")
    turtle.speed(1000)
    turtle.penup()
    turtle.setpos(-250,255)
    turtle.write("See where the arrow lands", font=("Arial", 25, "bold"))



# Create rings for target
def createRings():
    #color dictionary
    ringColors = {
        1: "white",
        2: "white",
        3: "black", 
        4: "black",
        5: "blue",
        6: "blue",
        7: "red",
        8: "red",
        9: "yellow",
        10: "yellow"
    }



    rings = turtle.Turtle()
    rings.hideturtle()
    rings.speed(1000)
    count = 1



    for i in range(160, 0,-16):
        rings.penup()
        if count != 11:
            rings.begin_fill()
            rings.pendown()
            rings.penup()
            rings.goto(0, -i)
            rings.pendown()
            if count == 1 or count == 2:
                rings.color("black", ringColors[count])
            elif count ==3 or count == 4:
                rings.color("white", ringColors[count])
            else:
                rings.color("black", ringColors[count])
            rings.circle(i)
            rings.penup()
            rings.home()
            rings.end_fill()
            count += 1            



#target values
def createValues():
    count = 1
    numbers = turtle.Turtle()
    numbers.ht()
    numbers.penup()

    #left side numbers
    for i in range(-150,0,15):
        numbers.setpos(i,-10)
        numbers.write(count, font=("Arial", 8, "bold"))
        count += 1
        if count == 1 or count == 2:
            numbers.color("black")
        elif count ==3 or count == 4:
            numbers.color("white")
        else:
            numbers.color("black")



def shootArrow():
    #creating arrow
    arrow = turtle.Turtle()
    arrow.ht()
    arrow.penup()
    
    #places arrow
    x = random.randint(-160, 160)
    y = random.randint(-160, 160)
    arrow.setpos(x,y)
    arrow.dot(10,"green")



# finding area between rings
    # areas = []
    # for i in range(160,0,-16):
    #     if i == 0:
    #         break
    #     else:
    #         a1 = 3.14 - (i)**2
    #         a1 = abs(a1)
    #         a2 = 3.14 - (i-16)**2
    #         a2 = abs(a2)
    #         circlesArea = int(a1 - a2)
    #         areas.append(circlesArea) 
            


createWindow()
createRings()
createValues()
shootArrow()
turtle.done()
