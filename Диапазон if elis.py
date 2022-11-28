points = int(input('Введите значение точек: '))

print(f'Вы ввели {points}')

if points < 9 or points > 51:
    print('Недопустимые точки. Вне диапазона')
else:
    print('Допустимые точки')