

MAX = 26
FIRST = 1
STEP = 1
raising_level = float(input('Введите кол-во мм повышения уровня океана: '))
first_year = raising_level

print(f'Год\t\tКол-во мм')

for year in range(FIRST, MAX, STEP):
    if year == 1:
        raising_level = first_year
    else:
        raising_level = first_year + raising_level


    print(f'{year}\t\t{raising_level: .1f}')