#Python_TURTLE_NOOBS
#Created by Cephas Cardozo

#imports
import turtle

#variables_global
cephas = turtle.Turtle()

#turtle_color, The values assigned in parenthesis in this statement is first - red (border color), second - blue (fill shape color)
cephas.color("red", "blue")

#begin_commandExecution
#using left or right, the values in the parameters would be considered in degrees

cephas.begin_fill()
cephas.forward(100)
cephas.left(90)
cephas.forward(100)
cephas.left(90)
cephas.forward(100)
cephas.left(90)
cephas.forward(100)
cephas.end_fill()

#PenUp - states that the pen is taken up and is moved in as a imaginary line, and PenDown - states that the pen is back on the plane surface to start drawing from the origin point
#SetHeading can be used to replace 'left' or 'right'

cephas.penup()
cephas.forward(100)
cephas.pendown()

cephas.begin_fill()
cephas.forward(100)
cephas.setheading(90)
cephas.forward(100)
cephas.setheading(90)
cephas.forward(100)
cephas.setheading(90)
cephas.forward(100)
cephas.end_fill()

#stop_Execution
turtle.done()
#End_of_Code