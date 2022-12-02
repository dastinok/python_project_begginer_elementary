

age = float(input('Введите возраст (целое число): '))

BABY = 1
CHILD = 13
TEEN = 20
ADULT = 21

if age <= BABY:
    print('Младенец')
elif CHILD >= age > BABY:
    print('Ребенок')
elif TEEN >= age > CHILD:
    print('Подросток')
else:
    print('Взрослый')
