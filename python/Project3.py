#impoting the turtle feature and random number generator
import turtle
import random

#sets up the dice roller
def rolldice():
    return random.randint(1,6)

#sets up the turtle window
window = turtle.Screen()
message = turtle.Turtle()
message.penup()
message.goto(-50,-300)
message.shape('blank')

#adds the finish line to the window
finishline = turtle.Turtle()
finishline.penup()
finishline.goto(100,300)
finishline.shape('blank')
finishline.pendown()
finishline.right(90)
finishline.forward(500)

#adds both turtles to the window
greenturtle = turtle.Turtle()
greenturtle.penup()
greenturtle.goto(-200,200)
greenturtle.color('green')
greenturtle.shape('turtle')
greenturtle.pendown()

redturtle = turtle.Turtle()
redturtle.penup()
redturtle.goto(-200,50)
redturtle.color('red')
redturtle.shape('turtle')
redturtle.pendown()

#defines the rest of the varibles for the start of the game
winner = False
greenturtlepos = 0
redturtlepos = 0
turn = 0

#while loop asks players to roll the dices and moves their turtles towards the finish line based on the number rolled. while loop ends when a turtle crosses the finsh line and winner is announced
while (winner == False):
    if turn == 0:
        input('Player 1 turn. Press any key to roll the dice. ')
        dicevalue = rolldice()
        print('Dice value = ', dicevalue)
        greenturtle.forward(dicevalue*10)
        greenturtlepos = greenturtlepos + dicevalue
    if greenturtlepos >= 30:
        message.write('The green turtle is the winner',font=("Comic Sans MS", 16, "normal"))
        winner = True
        turn = -1
        turn = turn+1
        break
    if turn == 0:
        input('Player 2 turn. Press any key to roll the dice. ')
        dicevalue = rolldice()
        print('Dice value = ', dicevalue)
        redturtle.forward(dicevalue*10)
        redturtlepos = redturtlepos + dicevalue 
    if redturtlepos >= 30:
        message.write('The red turtle is the winner',font=("Comic Sans MS", 16, "normal"))
        winner = True
        turn = -1
        turn = turn+1

#tells the players how to exit the game
print('Click window to end game')
window.exitonclick()