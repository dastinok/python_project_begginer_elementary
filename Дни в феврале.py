year = int(input('Введите год: '))
print(f'Вы ввели {year} год')

RATIO_1 = 100
RATIO_2 = 400
RATIO_3 = 4

if year % RATIO_1 == 0:
    if year % RATIO_2 == 0:
        print('Високосный год')
    else:
        print('Год обычный')

if year % RATIO_1 != 0:
    if year % RATIO_3 == 0:
        print('Високосный год')
    else:
        print('Год обычный')
