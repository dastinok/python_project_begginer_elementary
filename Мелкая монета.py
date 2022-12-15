print('--------Монета до зарплаты--------')
days = int(input('Введите кол-во дней: '))
START = 1
print(f'Дни\t\t\tКопейки\t\t\t\t\tРубли')
CONFERSATION_FACTOR = 0.01
sum_rub = 0.0

for count in range(START, days+1):

    if count <= 2:
        cop = count
        rub = cop * CONFERSATION_FACTOR
    else:
        cop = count ** 2
        rub = cop * CONFERSATION_FACTOR

    sum_rub = sum_rub + rub

    print(f'{count}\t\t\t\t{cop}\t\t\t\t\t{rub: .2f}')
print('---------Итого---------')
print(f'Итоговая сумма в рублях = {sum_rub: .2f} рублей')
