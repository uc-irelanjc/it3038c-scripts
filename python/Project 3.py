import turtle
import random

def rolldice():
    return random.randint(1,6)

window = turtle.Screen()

message = turtle.Turtle()
message.penup()
message.goto(-50,-300)
message.shape('blank')

finishline = turtle.Turtle()
finishline.penup()
finishline.goto(100,300)
finishline.shape('blank')
finishline.pendown()
finishline.right(90)
finishline.forward(500)

greenturtle = turtle.Turtle()
greenturtle.penup()
greenturtle.goto(-200,200) // #There will be 4 more turtle(Blue, yellow, red)to play the race, but I put only the green one.

greenturtle.color('green')
greenturtle.shape('turtle')
greenturtle.pendown()

winner = False
greenturtlepos = 0
redturtlepos = 0
blueturtlepos = 0
purpleturtlepos = 0
turn = 0
while (winner == False):
if turn == 0:
input('Green turtle turn. Press any key to roll the dice. ')
dicevalue = rolldice()
print('Dice value = ', dicevalue)
greenturtle.forward(dicevalue*10)
greenturtlepos = greenturtlepos + dicevalue
if greenturtlepos >= 30:
message.write('The green turtle is the winner',font=("Arial", 16, "normal"))
winner = True
turn = -1

turn = turn +
1

window.exitonclick()