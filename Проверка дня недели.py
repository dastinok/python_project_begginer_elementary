# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

number = int(input('Введите число от 1 до 7: '))
print(f'Вы ввели цифру {number}')

MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

if number == 1:
    print('Понедельник')
elif number == 2:
    print('Вторник')
elif number == 3:
    print('Среда')
elif number == 4:
    print('Четверг')
elif number == 5:
    print('Пятница')
elif number == 6:
    print('Суббота')
elif number == 7:
    print('Воскресенье')
else:
    print('Вы ввели не то число')


