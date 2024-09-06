"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(150)                       # Continuie the last two steps three more times
tina.left(90)                           # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(150)
tina.left(90)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(150)
tina.left(90)

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Why, hello there!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

tina.goto(-50,0)
tina.pendown()
tina.color('red')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(101, steps=50)
tina.end_fill()

tina.goto(-50,0)
tina.pendown()
tina.color('red')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(101, steps=50)
tina.end_fill()


turtle.exitonclick() 




                    # Close the window when we click on it


# Dont forget to check in your code!