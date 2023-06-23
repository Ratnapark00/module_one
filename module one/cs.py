import turtle

# Set up the turtle window
window = turtle.Screen()
window.title("Flag of Japan")
window.bgcolor("white")
window.setup(width=600, height=400)

# Create a turtle object
flag = turtle.Turtle()
flag.speed(0)
flag.penup()

# Move the turtle to the starting position
flag.goto(-100, 100)

# Draw the red circle
flag.color("red")
flag.begin_fill()
flag.circle(100)
flag.end_fill()

# Draw the white circle
flag.goto(-90, 90)
flag.color("white")
flag.begin_fill()
flag.circle(90)
flag.end_fill()

# Hide the turtle
flag.hideturtle()

# Exit on click
turtle.done()
