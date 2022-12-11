MAX = 100
NUMBER = 10
product = 0

while product < MAX:
    number = int(input('Введите число: '))
    print(f'Вы ввели {number}')
    product = number * NUMBER
    print(f'Результат {product}')
else:
    print('Game Over')
