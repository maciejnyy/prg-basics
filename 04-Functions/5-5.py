import turtle
import figures

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    
    t = turtle.Turtle()
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    figures.draw_square(50)
    
    t.penup()
    t.goto(150, 100)
    t.pendown()
    figures.draw_square(50)
    
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    figures.draw_triangle(60)

    t.penup()
    t.goto(150, -100)
    t.pendown()
    figures.draw_triangle(60)
    
    window.mainloop()
