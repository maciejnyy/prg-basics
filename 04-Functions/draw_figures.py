import turtle
from figures import draw_square

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    draw_square(100)
    window.mainloop()
