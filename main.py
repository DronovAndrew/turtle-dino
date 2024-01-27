import turtle

def draw_dinosaur():
    dino = turtle.Turtle()
    dino.shape("turtle")
    dino.color("green")
    dino.speed(2)

    # Рисуем тело динозавра
    dino.penup()
    dino.goto(-10, -40)
    dino.pendown()
    dino.goto(0, -30)
    dino.goto(-10, 0)
    dino.goto(-20, 10)
    dino.goto(-40, 0)
    dino.goto(-50, 10)
    dino.goto(-20, 20)
    dino.goto(-50, 20)
    dino.goto(-40, 40)
    dino.goto(-30, 40)
    dino.goto(-20, 50)
    dino.goto(-10, 50)
    dino.goto(10, 20)
    dino.goto(30, 10)
    dino.goto(60, 40)
    dino.goto(40, 10)
    dino.goto(30, -10)
    dino.goto(10, -20)
    dino.goto(20, -30)
    dino.goto(10, -40)
    dino.goto(-10, -40)

    turtle.done()


# Вызываем функцию для рисования динозавра
draw_dinosaur()