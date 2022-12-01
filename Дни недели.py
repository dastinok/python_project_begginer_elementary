number = int(input('Введите число от 1 до 7(день недели): '))
print(f'Вы ввели цифру {number}')

MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

if number == MONDAY:
    print('Понедельник')
elif number == TUESDAY:
    print('Вторник')
elif number == WEDNESDAY:
    print('Среда')
elif number == THURSDAY:
    print('Четверг')
elif number == FRIDAY:
    print('Пятница')
elif number == SATURDAY:
    print('Суббота')
elif number == SUNDAY:
    print('Воскресенье')
else:
    print('Введите занова')


