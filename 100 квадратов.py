#Псевдокод:
# Импортируем черепаху
# 1. Вводим начальные значения Переменных:
# A. Кол-во сторон 1 квадрата = 4
# B. Кол-во всех квадратов = 100
# C. Длина 1 квадрата
# D. Угол поворота
# E. Коэффициент уменьшения
# 2. Вводим цикл:
# A. Внешний цикл - 100
# B. Вложенный цикл - 4
# B-1. Черепаха двигается вперед на расстоянние Длины 1 квадрата
# B-2. Черепаха поворачивается на Угол поворота
# C. Внешний цикл сокращается на Коэффициент уменьшения
# D. Вводим функцию turtle.done() - оставление графического окна открытым

# Отдельно вначале:
# 1. Устанавливаем размер экрана
# 2. Перо поднимаем
# 3. Устанавливаем черепаху в удобное место на экране (turtle.goto(x,y))
# 4. Перо опускаем
# 5. Поворачиваем черепаху в нужную позицию в соответствии с заданием.
# 6. Устанавливаем скорость (если нужно)

#Pseudocode:
# Importing a turtle
# 1. Enter the initial values of the Variables:
# A. Number of sides of 1 square = 4
# B. Number of all squares = 100
# C. Length of 1 square
# D. Angle of rotation
# E. Reduction coefficient
#2. Enter the loop:
# A. The outer loop is 100
# B. Nested loop - 4
# B-1. The turtle moves forward by the distance of the length of 1 square
# B-2. The turtle turns at the angle of rotation
# C. The outer loop is reduced by the Reduction factor
#D. We introduce the turtle.done() function - leaving the graphical window open

# Separately at the beginning:
# 1. Set the screen size
# 2. We lift the pen
# 3. We install the turtle in a convenient place on the screen (turtle.goto(x,y))
# 4. We lower the pen
# 5. Turn the turtle to the desired position according to the task.
# 6. Set the speed (if necessary)

import turtle

turtle.setup(1200, 1024)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.right(180)
turtle.speed(10)

NUM_ONE_SQUARE = 4
NUM_ALL_SQUARE = 100 # Общее кол-во квадратов
DISTANCE = 516
ANGLE_OF_ROTATION = 90

REDUCTION_RATIO = 5

for count in range(NUM_ALL_SQUARE):
    for x in range(NUM_ONE_SQUARE):
        turtle.forward(DISTANCE)
        turtle.right(ANGLE_OF_ROTATION)
    DISTANCE -= REDUCTION_RATIO

turtle.done()