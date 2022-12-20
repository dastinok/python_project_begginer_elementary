#Псевдокод:
#1. Поворачиваем черепаху налево 90 градусов и Скорость черепахи
#2. Устанавливаем Переменные:
#A. Количество общих линий
#B. Количество линий в одном цикле = 1
#C. Длина одной линии
#D. Угол поворота
#C. Увеличение линии (удлинение)
#2. Устанавливаем цикл:
#A. Внешний цикл с числом общих линий
#B. Внутренний (вложенный) цикл с Количеством линий в одном цикле:
#B-1. Черепаха движется вперед на Длину одной линии
#B-2. Черепаха разворачивается на Угол поворота
#C. Во Внешнем цикле увеличиваем Длину одной линии на Увеличение линии (удлинение)
#D. Вводим функцию turtle.done() - оставление графического окна открытым

#Pseudocode:
#1. Turn the turtle to the left 90 degrees and the speed of the turtle
#2. Set the Variables:
#A. Number of common lines
#B. Number of lines in one cycle = 1
#C. Length of one line
#D. Angle of rotation
#C. Increasing the line (lengthening)
#2. Setting the cycle:
#A. External loop with the number of common lines
#B. An internal (nested) loop with the number of lines in one loop:
#B-1. The turtle moves forward by the length of one line
#B-2. The turtle turns around at the angle of rotation
#C. In the Outer loop, we increase the Length of one line by Increasing the line (lengthening)
#D. We introduce the turtle.dove() function - drawing up a graphical window open




import turtle

turtle.left(90)

turtle.speed(10)


NUMBERS_LINES = 101
NUMBERS_LINES_1_CYCLE = 1
LENGTH = 10
ANGLES = 90
INCREASE_OF_LINES = 3

for count in range(NUMBERS_LINES):
    for x in range(NUMBERS_LINES_1_CYCLE):
        turtle.forward(LENGTH)
        turtle.left(ANGLES)
    LENGTH += INCREASE_OF_LINES





turtle.done()