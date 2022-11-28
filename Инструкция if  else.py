speed = float(input('Введите значение скорости: '))

print(f'Вы ввели {speed} км/ч')

if speed > 24 and speed < 56:
    print('Скорость нормальная')
else:
    print('Скорость аварийная')
