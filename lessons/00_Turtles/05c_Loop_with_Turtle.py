
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.forward(150)                       # Continue the last two steps three more times
tina.left(90)                           # to draw a square

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)

... # Your code here
tina.shape('turtle')
tina.forward(50)
tina.left(72)
tina.forward(50)
tina.left(72)
tina.forward(50)
tina.left(72)
tina.forward(50)
tina.left(72)
tina.forward(50)
tina.left(50)
tina.color("blue")
tina.begin_fill()
tina.circle(30, steps=50)
tina.end_fill()
tina = turtle.Turtle()
turtle.exitonclick()                    # Close the window when we click on it

... # Your code here
