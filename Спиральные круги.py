import turtle

CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)



for x in range(CIRCLES):
    turtle.pencolor('pink')
    turtle.pensize(2)
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()