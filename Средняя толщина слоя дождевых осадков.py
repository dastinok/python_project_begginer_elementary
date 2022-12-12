
total = 0
years = int(input('Количество лет: '))


MONTH = 12
amount = years * MONTH
for x in range(years):
    for i in range(amount):
        fallout = float(input('Кол-во осадков в мм: '))
        total += fallout
    average = total / amount

print(f'Кол-во дождевых осадков в мм - {total: .0f}\n'
      f'Общее кол-во месяцев - {amount: .0f}\n'
      f'Среднее кол-во осадков - {average: .2f}')



