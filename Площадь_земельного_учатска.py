square_meter = float(input('Введите общее кол-во квадратных метров участка: '))

ACRE = 4040.86  # Магическое число

number_of_acres = square_meter / ACRE

print(f'Кол-во акров в этом участке равно {number_of_acres:.2f}')


