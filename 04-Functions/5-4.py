import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length


# Draw a square
def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)
draw_square(100)
# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
