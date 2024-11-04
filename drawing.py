from turtle import *

def draw_sea():
    speed(13)  # Painting speed control
    bgcolor("blue")
    pensize(10)
    penup()
    setup(650, 350, 100, 100)
    fillcolor("pink")
    begin_fill()
    penup()
    bk(200)
    pendown()
    pencolor("black")

    goto(-100, 100)
    goto(0, 0)
    goto(100, 100)

    goto(100, -100)
    goto(0, 0)
    goto(-100, -100)

    goto(-200, 0)
    goto(-175, 25)
    circle(-22.5, 180)

    seth(-45)
    goto(-200, 0)
    goto(-100, 100)
    goto(-100, -100)

    penup()
    goto(-175, 0)
    dot(10, "black")
    pendown()
    end_fill()
    done()



draw_sea()


