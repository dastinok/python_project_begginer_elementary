import turtle

turtle.pensize(2)
turtle.circle(50)
turtle.goto(0, 325)
turtle.write('Север', move=False, align='center', font=("Arial", 16, "normal"))

turtle.goto(0, -250)
turtle.penup()
turtle.goto(0, -275)
turtle.write('Юг', move=False, align='center', font=("Arial", 16, "normal"))

turtle.goto(0, 50)

turtle.pendown()

turtle.goto(325, 50)
turtle.penup()
turtle.goto(365, 40)
turtle.write('Восток', move=False, align='center', font=("Arial", 16, "normal"))

turtle.goto(0, 50)

turtle.pendown()

turtle.goto(-325, 50)
turtle.penup()
turtle.goto(-358, 40)
turtle.write('Запад', move=False, align='center', font=("Arial", 16, "normal"))



turtle.done()