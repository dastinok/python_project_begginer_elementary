number = int(input('Введите цифру от 0 до 36: '))
print(f'Вы ввели цифру {number}')


if number == 0:
    print('Зеленый')
elif number >= 37:
    print('Вы вышли за диапазон')

if 0 < number <= 10:
    if number % 2 != 0:
        print('Красный')
    else:
        print('Черный')
if 11 <= number <= 18:
    if number % 2 != 0:
        print('Красный')
    else:
        print('Черный')
if 19 <= number <= 28:
    if number % 2 != 0:
        print('Красный')
    else:
        print('Черный')
if 29 <= number <= 36:
    if number % 2 != 0:
        print('Красный')
    else:
        print('Черный')

