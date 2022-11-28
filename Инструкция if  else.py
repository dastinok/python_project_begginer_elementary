speed = float(input('Введите значение скорости: '))

print(f'Вы ввели {speed} км/ч')

if speed > 24 and speed < 56:
    print('Скорость нормальная')
elif speed < 24:
    print('Скорость аварийная')
elif speed > 56:
    print('Скорость аварийная')
elif speed == 24:
    print('Скорость на грани')
elif speed == 56:
    print('Скорость на грани')