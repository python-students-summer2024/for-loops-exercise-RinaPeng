# import the turtle module, which is included in the regular Python distribution
import turtle


def create_turtle(stroke_color, bg_color):
    """
    Creates a turtle object, and sets the stroke and background colors.
    This code is given to you for use by the other functions.
    """
    t = turtle.Turtle()
    t.shape("turtle")  # make it look like a turtle
    t.color(stroke_color)  # set the color of the trail left by the turtle

    window = turtle.Screen()  # get access to the window where the turtle will appear
    window.bgcolor(bg_color)  # set the window's background color

    return t


def pick_up_and_move_turtle(t, x, y):
    """
    Pick up and move the turtle to a specific position on the screen.
    The turtle does not leave a trail behind it when picked up and moved.
    """
    t.penup()  # lift up the turtle's 'pen', so it doesn't draw
    t.setposition(x, y)
    t.pendown()  # put down the turtle's 'pen', ready to draw


def print_turtle_position(t):
    """
    Prints out the turtle's x and y coordinates and degree of rotation on the screen.
    """
    print("Turtle at", t.position(), "rotated", t.heading(), "degrees")


def draw_square(t, start_x, start_y, length, rotation_direction, fill_color):
    """
    Draw a square with a given side length, starting from a specific position.
    """
    pick_up_and_move_turtle(t, start_x, start_y)
    t.fillcolor(fill_color)
    t.begin_fill()

    for _ in range(4):
        print_turtle_position(t)
        t.forward(length)
        if rotation_direction == 'left':
            t.left(90)
        else:
            t.right(90)

    t.end_fill()


def draw_star(t, start_x, start_y, length, angle, initial_rotation_direction, fill_color):
    """
    Draw a five-pointed star, starting from a given position.
    """
    pick_up_and_move_turtle(t, start_x, start_y)
    t.fillcolor(fill_color)
    t.begin_fill()

    for _ in range(5):
        print_turtle_position(t)
        t.forward(length)
        if initial_rotation_direction == 'left':
            t.left(angle)  # Turning left with the specified angle for left rotation
            t.forward(length)
            t.right(18)  # Hardcoding the small angle for right turn when initial direction is left
        else:
            t.right(angle)  # Turning right with the specified angle for right rotation
            t.forward(length)
            t.left(48)  # Hardcoding the small angle for left turn when initial direction is right

    t.end_fill()

