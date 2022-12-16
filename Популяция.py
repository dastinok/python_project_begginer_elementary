
FIRST = 0
start_amount = int(input('Стартовое кол-во: '))
average_day_raise = int(input('Среднесуточное увеличение(%): '))
day_reproduction = int(input('Кол-во дней размножения: '))

print(f'День\t\tПопуляция')
PERCENT_COEF = average_day_raise / 100

for days in range(FIRST, day_reproduction):
    days += 1
    if days == 1:
        start_amount = start_amount
    else:
        start_amount = (start_amount * PERCENT_COEF) + start_amount

    print(f'{days}\t\t\t{start_amount: .2f}')