

weight = float(input('Введите свой вес в кг: '))

print(f'Дни\t\tПотеря кг')

CALORIES_PER_DAY = 500

COEF_LOSE = 0.00013
FIRST = 1
MAX = 181
STEP = 1

for days in range(FIRST, MAX, STEP):

    weight = weight - (CALORIES_PER_DAY * COEF_LOSE)

    print(f'{days}\t\t{weight: .2f}')

