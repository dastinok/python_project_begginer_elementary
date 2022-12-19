import turtle

turtle.setup(800, 800)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
BASE_SIZE = 2

for x in range(BASE_SIZE):

    for c in range(4):
        turtle.forward(200)
        turtle.right(45)

turtle.penup()
turtle.goto(-15, -80)
turtle.pendown()
turtle.write('STOP', font=("Arial", 70, "normal"))
turtle.hideturtle()

turtle.done()




