
speed = int(input('Введите скорость т/с в км/ч: '))
hours = int(input('Введите часы движения: '))
START = 1

print()
print('Час\t\tПройденное расстояние')

for counter in range(START, hours + 1):
    distance = speed * counter
    print(f'{counter}\t\t{distance}')