import turtle

def draw_square(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()

def draw_triangle(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(3):
        pen.forward(length)
        pen.left(120)
    pen.hideturtle()

def draw_rectangle(length_a, length_b):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
    pen.hideturtle()
