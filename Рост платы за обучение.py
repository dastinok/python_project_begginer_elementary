
MAX = 6
FIRST = 1
STEP = 1
PERCENT_YEAR = 0.03


pay_year = float(input('Введите плату за год в рубликах: '))

print(f'Год\t\tПлата за обучение')

for year in range(FIRST, MAX, STEP):
    pay_year = (pay_year * PERCENT_YEAR) + pay_year

    print(f'{year}\t\t{pay_year: .2f}')
